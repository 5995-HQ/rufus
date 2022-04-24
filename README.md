# rufus
A simple speech recognition bot that can repeat back to you using Apple's built in "say" command


# Setup

Be sure to have [Python3](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/), and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed. 

## Create a virtualenv and activate it
`virtualenv venv --python=$(which python3)`

`source venv/bin/activate`

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

## Still broken?

You probably have `homebrew`'s path in `/opt/` instead. In that case:

```
pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio
```
If you got this error:
```
raise OSError("FLAC conversion utility not available - consider installing the FLAC command line application by running `apt-get install flac` or your operating system's equivalent")
OSError: FLAC conversion utility not available - consider installing the FLAC command line application by running `apt-get install flac` or your operating system's equivalent
```
Run this:
`brew install flac` 

