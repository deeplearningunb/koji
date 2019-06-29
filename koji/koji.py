from os import system
from os import listdir
from os.path import exists
import sys, getopt

class Koji():
    def __init__(self):
        self.genre = None
        self.outdir = None
        self.steps = '1000'
        self.eval_ratio = '0.1'
        self.num_outputs = '10'

    def genre_path(self):
        path = "data/inputs/" + self.genre
        if(exists(path)):
            return path
        else:
            print("koji.py: the genre \'" + self.genre + "\' is not implemented yet.")
            print("to add a new genre https://github.com/deeplearningunb/koji#adding-new-genres read this tutorial.")
            sys.exit(2)

    def convert_directory(self, path):
        cmd = 'convert_dir_to_note_sequences \
                --input_dir=' + path + ' \
                --output_file=./tmp/notesequences.tfrecord \
                --recursive'

        system(cmd)

    def create_dataset(self):
        cmd = 'melody_rnn_create_dataset \
                --config=attention_rnn \
                --input=./tmp/notesequences.tfrecord \
                --output_dir=./tmp/melody_rnn/sequence_examples \
                --eval_ratio=' + self.eval_ratio

        system(cmd)

    def train(self):

        cmd = 'melody_rnn_train \
                --config=attention_rnn \
                --run_dir=./tmp/melody_rnn/logdir/run1 \
                --sequence_example_file=./tmp/melody_rnn/sequence_examples/training_melodies.tfrecord \
                --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
                --num_training_steps=' + self.steps

        system(cmd)

    def generate(self, dir):

        if dir is None:
            dir = './tmp/melody_rnn/generated'
        cmd = 'melody_rnn_generate \
                --config=attention_rnn \
                --run_dir=./tmp/melody_rnn/logdir/run1 \
                --output_dir=' + dir + ' \
                --num_outputs='+ self.num_outputs + '\
                --num_steps=128 \
                --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
                --primer_melody="[60]"'

        system(cmd)

    def validate_args(self, argv):
        try:
           return getopt.getopt(argv,"hg:o:s:e:n:",["genre=","outdir=","steps=","eval_ratio=","num_outputs="])
        except getopt.GetoptError:
            print ('koji.py -g <genre> [-o <outdir> -s <steps> -e <eval ratio> -n <number of outputs>]')
            sys.exit(2)

    def set_attributes(self, opts):
        for opt, arg in opts:
            if opt == '-h':
                print ('koji.py -g <genre> [-o <outdir> -s <steps> -e <eval ratio> -n <number of outputs>]')
                print('Implemented genres:')
                dirs = listdir("data/inputs/")
                for genre in dirs:
                    print(' ', '-',genre)
                    sys.exit()
            elif opt in ("-g", "--genre"):
                self.genre = arg
            elif opt in ("-o", "--outdir"):
                self.outdir = arg
            elif opt in ("-s", '--steps'):
                self.steps = arg
            elif opt in ("-e", "--eval_ratio"):
                self.eval_ratio = arg
            elif opt in ("-n", "--num_outputs"):
                self.num_outputs = arg

    def validate_genre(self):
        if(self.genre is None):
            print('koji.py -g <genre> [-o <outdir> -s <steps> -e <eval ratio> -n <number of outputs>]')
            sys.exit(2)

    def run(self, argv):
        opts, args = self.validate_args(argv)
        self.set_attributes(opts)
        self.validate_genre()

        path = self.genre_path()
        self.convert_directory(path)
        self.create_dataset()
        self.train()
        self.generate(self.outdir)

koji = Koji()
koji.run(sys.argv[1:])
