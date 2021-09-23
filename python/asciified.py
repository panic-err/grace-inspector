#!/usr/bin/env python

from PIL import Image
import os
import sys
from  subprocess import call


asciicode = " -.-,-:-;-i-r-s-X-A- -5-3-h-M-H-G-S-#-9-B-&-@".split("-")
def asciified(filename):
    if filename != 'asciified.py':
        img = Image.open(filename).convert('LA')
        #filename = filename.split('/')
        for x in filename:
            if '.' in x:
                filename = x
                break
        delname = filename
        filenameSplit = filename.split('.')
        img = img.resize((16,16))
        argument = ("{0}".format("grey")+filenameSplit[1])
        #os.remove('101/'+delname)
        img.save('101/'+argument+".png")

        img = Image.open('101/grey{0}.png'.format(filenameSplit[0]))
        #finalimg = Image.new("LA", (32, 32))
        #grey = img.crop((0, 0, 128, 128))
        grey = img.load()
        os.remove('101/grey{0}.png'.format(filenameSplit[0]))
        #print grey[0,0]
        # Create the final file to be made
        numberFiles = len(os.listdir('101'))
        numberFiles += 1
        filepath = '101/{0}.txt'.format(str(numberFiles))
        finalascii = open(filepath, 'w+')
        #print finalascii
        for column in range(15):
            for row in range(16):
                rowcol = grey[row, column]
                asciinum = int(rowcol[0]/24)

                finalascii.write(asciicode[asciinum])
            finalascii.write("\n")
        return filepath
