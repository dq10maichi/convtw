#!/usr/bin/env python
# Pillowを使用した画像圧縮プログラム
from PIL import Image,ImageFilter
import sys
import os

quality = 75
width = 1980
args = sys.argv 

def conv(InputFile,OutputFile):
    try:
        im = Image.open(InputFile)
    except IOError:
        pass
    
    resize_im = im.resize((width,int(width / im.width * im.height)),Image.LANCZOS)
    resize_im.save(OutputFile, quality=quality)

def GenerateOutputFileName(InputFile):
    return 'TW_' + InputFile

if __name__ == "__main__":
    args.pop(0)
    for arg in args:
        if os.path.isfile(arg):
            conv(arg,GenerateOutputFileName(arg))   
