# Koji
AI that creates game music. 

Named after the japanese music composer [Koji Kondo](https://en.wikipedia.org/wiki/Koji_Kondo), this project aims to create game songs based on common game themes (Super Mario, Sonic, Alex Kid, The Legend of Zelda).

We're using [Magenta](https://github.com/tensorflow/magenta) to help create melodies.

# Summary
<!-- TO DO  -->

# Installation
To install Koji just use:

```bash
pip3 install -r requirements.txt
```

# Usage
## Generating Melodies
To create melodies, you should choose the music style. The current options are: `rpg`, `platformer`, `action`.

The final command looks like this:

```bash
python3 koji.py STYLE [output-folder]
```

The `output-folder` has a default value of `/tmp/melody_rnn/generated`

## Adding new styles
If you want to add new styles, just create a directory within `data/` with the name of the new style inside.

So, to create a new style called `horror` you should crate a directory `data/horror`.

After adding MIDI files within `horror`, you can run:

```bash
python3 koji.py horror
```

# Creators
* Álax Alves
* Arthur Assis
* Lucas Martins
* Matheus Richard
* Thalisson Melo
