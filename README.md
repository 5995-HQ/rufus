# rufus
A simple speech recognition bot that can repeat back to you using Apple's built in "say" command


# Setup

Be sure to have [Python3](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/), and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed. 

## Create a virtualenv
`virtualenv venv --python=$(which python)`

## Install packages
`pip install -r brain/requirements.txt`

## Run the script
`python brain/rufus.py`

Start talking! Watch it ___say___ and print what you just said!

It's ___that___ easy. 

## Troubleshooting
Did you happen to encounter this error? 

```
src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
#include "portaudio.h"
         ^
1 error generated.
error: command 'cc' failed with exit status 1
```

Try this to work around it. (Note you'll need [homebrew](https://brew.sh) installed for this to work)

```
brew install portaudio

pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```
