convert_dir_to_note_sequences \
  --input_dir=./data/inputs \
  --output_file=./tmp/notesequences.tfrecord \
  --recursive

melody_rnn_create_dataset \
--config=attention_rnn \
--input=./tmp/notesequences.tfrecord \
--output_dir=./tmp/melody_rnn/sequence_examples \
--eval_ratio=0.10

melody_rnn_train \
--config=attention_rnn \
--run_dir=./tmp/melody_rnn/logdir/run1 \
--sequence_example_file=./tmp/melody_rnn/sequence_examples/training_melodies.tfrecord \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--num_training_steps=100

melody_rnn_generate \
--config=attention_rnn \
--run_dir=./tmp/melody_rnn/logdir/run1 \
--output_dir=./tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--primer_melody="[60]"