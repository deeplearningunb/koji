from os import system
from os import listdir
from os.path import exists
import sys, getopt

class Koji():

    def genre_path(genre):
        path = "data/inputs/"+genre
        if(exists(path)):
            return path
        else:
            print("koji.py: the genre \'" + genre + "\' is not implemented yet.")
            print("to add a new genre https://github.com/deeplearningunb/koji#adding-new-genres read this tutorial.")
            sys.exit(2) 

    def convert_directory(path):
        cmd = 'convert_dir_to_note_sequences \
                --input_dir=' + path + ' \
                --output_file=./tmp/notesequences.tfrecord \
                --recursive'

        system(cmd)

    def create_dataset():
        cmd = 'melody_rnn_create_dataset \
                --config=attention_rnn \
                --input=./tmp/notesequences.tfrecord \
                --output_dir=./tmp/melody_rnn/sequence_examples \
                --eval_ratio=0.10'

        system(cmd)

    def train():

        cmd = 'melody_rnn_train \
                --config=attention_rnn \
                --run_dir=./tmp/melody_rnn/logdir/run1 \
                --sequence_example_file=./tmp/melody_rnn/sequence_examples/training_melodies.tfrecord \
                --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
                --num_training_steps=1000'

        system(cmd)

    def generate(outdir):

        if outdir is None:
            outdir = './tmp/melody_rnn/generated'
        cmd = 'melody_rnn_generate \
                --config=attention_rnn \
                --run_dir=./tmp/melody_rnn/logdir/run1 \
                --output_dir=' + outdir + ' \
                --num_outputs=10 \
                --num_steps=128 \
                --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
                --primer_melody="[60]"'
            
        system(cmd)

    def run(argv):
        genre = None
        outdir = None
        try:
           opts, args = getopt.getopt(argv,"hg:o:",["genre=","outdir="])
        except getopt.GetoptError:
            print ('koji.py -g <genre> [-o <outdir>]')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                    print ('koji.py -g <genre> [-o <outdir>]')
                    print('Implemented genres:')
                    dirs = listdir("data/inputs/")
                    for genre in dirs:
                        print(' ', '-',genre) 
                    sys.exit()
            elif opt in ("-g", "--ifile"):
                genre = arg
            elif opt in ("-o", "--ofile"):
                outdir = arg  
        
        if(genre is None):
            print('koji.py -g <genre> [-o <outdir>]')
            sys.exit(2)

        path = Koji.genre_path(genre)

        Koji.convert_directory(path)
        Koji.create_dataset()
        Koji.train()
        Koji.generate(outdir)

Koji.run(sys.argv[1:])