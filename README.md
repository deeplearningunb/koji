# Koji
AI that creates game music. 

Named after the japanese music composer [Koji Kondo](https://en.wikipedia.org/wiki/Koji_Kondo), this project aims to create game songs based on common game themes (Super Mario, Sonic, Alex Kid, The Legend of Zelda). 

Our intent is to help non-musicians create songs for their games, and/or help actual musicians to have new ideas too :smiley: 

We're using [Magenta](https://github.com/tensorflow/magenta) to help create melodies.

# Table of Contents
- [Getting started](#getting-started)
	- [Installation](#installation)
	- [Usage](#usage)
	  - [Generating Melodies](#generating-melodies)
	  - [Adding new genres](#adding-new-genres)
- [Creators](#creators)
- [License](#license)

# Getting Started
## Installation
To install Koji just use:

```bash
pip3 install -r requirements.txt
```

## Usage
### Generating Melodies
To create melodies, you should choose the music genre. The current options are: `rpg`, `platformer`, `action`.

The final command looks like this:

```bash
python3 koji.py -g GENRE [-o output-folder]
```

The `output-folder` has a default value of `/tmp/melody_rnn/generated`

### Adding new genres
If you want to add new genres, just create a directory within `data/` with the name of the new genre inside.

So, to create a new genre called `horror` you should crate a directory `data/horror`.

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

# License
Koji is licensed under [MIT](LICENSE).