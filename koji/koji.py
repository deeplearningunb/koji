from os import system
import sys, getopt

class Koji():

    def convert_directory():
        inputfile = ''
        outputfile = ''
        try:
           opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            print 'koji.py -i <inputfile> -o <outputfile>'
            sys.exit(2)
        for opt, arg in opts:
           if opt == '-h':
                    print 'test.py -i <inputfile>'
                    sys.exit()
           elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg  
        print 'Input file is "', inputfile
        cmd = 'convert_dir_to_note_sequences \
                --input_dir=./data/inputs \
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

    def generate():

        cmd = 'melody_rnn_generate \
                --config=attention_rnn \
                --run_dir=./tmp/melody_rnn/logdir/run1 \
                --output_dir=./tmp/melody_rnn/generated \
                --num_outputs=10 \
                --num_steps=128 \
                --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
                --primer_melody="[60]"'
            
        system(cmd)

    def run():
        Koji.convert_directory()
        Koji.create_dataset()
        Koji.train()
        Koji.generate()

Koji.run(sys.argv[1:])