#!/bin.sh

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install pyaudio

python3 -m ensurepip

pip3 --version

pip3 install pyaudio

pip3 install sapling-py

pip3 install speechrecognition

pip3 install flac

pip3 install gtts

pip3 install pygame

