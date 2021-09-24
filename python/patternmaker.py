
#!/usr/bin/env python

import os
import sys
import time
import datetime
from random import *
import curses


def colour(toColour):
       attack = False
       seed(int(float(datetime.datetime.now().microsecond)*25485039845))
       rando = randint(1, 100)
       if rando > 50:
               val = "38"
       else:
               val = "48"
       
       key=""
       exit = False
       #print("\n\n"+str(size.lines))
       p = ""
       pos = 1
       def calc_red():
            red = randint(1, 255)
            if red < 0:
                red = 0
            return red
       def calc_green():
            green = randint(1, 255)
            if green < 0:
                green = 0
            return green
       def calc_blue():
            blue = randint(1, 255)
            if blue < 0:
                blue = 0
            return blue
       p += "\x1b["+val+";2;"+str(calc_blue())+";"+str(calc_green())+";"+str(calc_red())+"m"+toColour+" "
       #print(p+"\n")
       #time.sleep(0.01)
       pos = 0
       if not attack:
           p += " \033[0m"
           p += "\033[0m\n"
       else:
           p += "\n"
       blank = ""
       pos = 0
       total = 0
       print(p)
       #print("\033["+str(line)+";0H\033[0m"+blank+"\033[0m")

       return p
while True:
    
    print(colour("word"))
