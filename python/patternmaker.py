#!/usr/bin/env python

import os
import sys
import time
import datetime
from random import *
import curses


def main(win):
       attack = False
       if len(sys.argv) < 2:
           print("Usage is GLITCH --flag statements.\nWhere a flag is one of either --foreground --background or non existent")
           sys.exit(1)
       if sys.argv[1] == '--foreground':
            val = "38"
       elif sys.argv[1] == '--background':
            val = "48"
       else:
           seed(int(float(datetime.datetime.now().microsecond)*25485039845))
           rando = randint(1, 100)
           if rando > 50:
               val = "38"
           else:
               val = "48"
       
       win.nodelay(True)
       key=""
       exit = False
       #win.clear()
       try:
        key = win.getkey()
        if str(key) != '':
            #print("Farewell")
            exit = True
        if str(key) == " ":
            attack = True
            exit = False
       except:
            print('')
            #none
       if exit:
            curses.endwin()
            sys.exit()
       size = os.get_terminal_size()
       #print("\n\n"+str(size.lines))
       p = "\033[0;0H"
       pos = 1
       for line in range(size.lines):

           for word in sys.argv:
            if word == "--foreground" or word == "--background":
             continue
            if "main.py" not in word and "--foreground" not in word and "--background" not in word:
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
                        pos += len(word)         
                        
                        if attack:
                            p += "\033["+str(line)+";"+str(pos)+"H\033[48;2;"+str(calc_red())+";"+str(calc_green())+";"+str(calc_red())+"m"+word+" "
                        else:
                            p += "\033["+str(line)+";"+str(pos)+"H\033["+val+";2;"+str(calc_blue())+";"+str(calc_green())+";"+str(calc_red())+"m"+word+" "
                        print(p+"\n")
                        time.sleep(0.01)
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
       while len(p) > total:
            total += len(word)
            blank += " "
       #print("\033["+str(line)+";0H\033[0m"+blank+"\033[0m")
       p = ""
win = curses.initscr()
curses.echo()
curses.cbreak()
while True:
    
    main(win)
