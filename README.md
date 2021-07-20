# PySteg

## Overview

Image steganography is the process of hiding information within an image. This program is utilized to hide a text based message within an image. 

## How-To

Just load up `PySteg.py` and execute it. Make 3 directories, `/encrypt`, `/decrypt`, `/export` in the same directory where `PySteg.py` is located.
- Place any PNG image you want to encrypt a message inside the `/encrypt` directory.
- Place any PNG image you want to decrypt a message inside the `/decrypt` directory.
- Any image encrypted with the program will be replicated and saved into the `/export` directory.

The program will work with **multiple** images, so if you place multiple images within a sub directory, it'll work with all of them. It also recognizes the file extension, so if you have a bunch of text files within a sub directory it'll just ignore them.
