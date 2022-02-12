import PySide6

print(PySide6.__version__)

import pika
import sys
import time
import psycopg2

import threading
import random
import sys
import os
from random import *
import datetime

from PySide6.QtQuick import QQuickWindow
from PySide6.QtGui import Qt
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtCore import QUrl, Qt, Slot, Property
from PySide6.QtWidgets import (QWidget, QProgressBar, QFrame, QDialog, QVBoxLayout, QApplication, QLineEdit, QLabel, QPushButton, QGridLayout)
from __feature__ import snake_case



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

       p += "\\x1b["+val+";2;"+str(calc_blue())+";"+str(calc_green())+";"+str(calc_red())+"m"+toColour+" "
       #print(p+"\n")
       #time.sleep(0.01)
       pos = 0
       if not attack:
           p += " \\033[0m"
           p += "\033[0m"
       else:
           p += ""
       blank = ""
       pos = 0
       total = 0
       print(p)
       #print("\033["+str(line)+";0H\033[0m"+blank+"\033[0m")

       return p

class InputBox(QWidget):

    def calc_red(self):
        red = randint(1, 255)
        if red < 0:
            red = 0
        self.red = str(red)
        return red
    def calc_green(self):
        green = randint(1, 255)
        if green < 0:
            green = 0
        self.green = str(green)
        return green
    def calc_blue(self):
        blue = randint(1, 255)
        if blue < 0:
            blue = 0
        self.blue = str(blue)
        return blue

    def reconnect(self):
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body="bip")
        print("[x] Sent %r:%r" % (self.routing_key, "bip"))


    def emission(self, pos):
        self.calc_red()
        self.calc_green()
        self.calc_blue()
        message = "PACKAGE:"+self.red+":"+self.green+":"+self.blue+":"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text = self.greeters[pos].text
        #self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )



    def emissionNoColour(self, pos):
        message = "PACKAGE::::"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text() = self.greeters[pos].text()
        #self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )



    def __init__(self):
        #t = threading.Thread(Heartbeat.__init__)
        #t.start()
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])
        bep = Heartbeat()
        bep.start()
        #self.connection = bep.connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')
        #bep = Heartbeat()
        #t = threading.Thread(bep.run)
        #t.start()
        #bep.start()
        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
        self.message = 'init'
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body=self.message)
        print("[x] Sent %r:%r" % (self.routing_key, self.message))


        QWidget.__init__(self)
        self.hello =  [
                "hallo",
                "hi",
                "hola"
                ]

        self.buttons = []
        self.greeters = []
        self.senders = []
        self.resize(800, 150)
        self.layout = QGridLayout(self)
        self.layout.set_horizontal_spacing(0)
        self.layout.set_vertical_spacing(0)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(1):
            self.set_window_title("Input Bar")
            mess = QLineEdit("Messages!")
            mess.position = i
            mess.set_max_length(60)
            mess.returnPressed.connect(self.greet)
            self.greeters.append(mess)
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 0)
            nameButton = QPushButton(sys.argv[2])
            nameButton.clicked.connect(self.name_detail)
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 1)
            button = QPushButton(str(i))
            button.setStyleSheet("color:orange;")
            #self.position = i
            button.position = i
            self.layout.add_widget(button, i, 2)
            send = QPushButton("SEND")
            send.setStyleSheet("color:aqua;")
            send.position = i
            send.clicked.connect(self.greetNoColour)
            button.clicked.connect(self.greet)
            self.senders.append(send)
            self.layout.add_widget(send, i, 3)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.setStyleSheet("background-color:#b767bc;")
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QPushButton(nameDetail)
            #labelDetail.clicked.connect(self.emission)
            self.nameDetailLayout.add_widget(labelDetail)

        self.established = False
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Property(QWidget)
    def conn():
        return self.connection
    @Slot()
    def name_detail(self):
        #code for showing a string in an array
        if not self.established:
            filename = '101/1.txt'
            out = []
            outString = ""
            count = 0
            with open(filename) as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    outString += lines[i]
                count += 1
            #print(outString)
            l = QLabel(outString)

            self.nameDetail.layout().add_widget(l)
            l.show()
            self.established = True
        #self.nameDetail.setText(outString)
        self.nameDetail.resize(450, 500)
        self.nameDetail.setStyleSheet("background:black;font:Courier New;color:pink;")
        self.nameDetail.show()
    @Slot()
    def greet(self):
        butt = self.focus_widget()
        try:
            self.emissionNoColour(butt.position)
        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emissionNoColour(butt.position)
            for b in self.greeters:
                #print(b.position)
                if b.position == butt.position:
                    print("Triggered")
                    #b.setFocus()
                    b.set_text("")

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)
    @Slot()
    def greetNoColour(self):
        butt = self.focus_widget()
        try:
            self.emissionNoColour(butt.position)

        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emissionNoColour(butt.position)

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)

    @Slot()
    def boop():
        print("boop")
        #self.message.text = random.choice(self.hello)

class Receiver(QWidget):

    def consumeCallback(self, ch, method, properties, body):
        print("[x], %r:%r" % (method.routing_key, body))
        bodyStr = str(body)
        print("In loop?")
        if "bip" in bodyStr:
            return
        deconBody = bodyStr.split(":")
        if len(deconBody) < 6:
            bodyStr = "PACKAGE::::"+"::"
            deconBody = bodyStr.split(":")
        if len(deconBody) > 6:
            print("Illegal character found")
            subBody = ""
            for i in range(len(deconBody)):
                if i >= 5:
                    subBody += deconBody[i]
            deconBody[5] = subBody
        if "DRILL" in deconBody[5] and len(deconBody) < 6:
            if self.spacers[int(deconBody[4])-1].coord <= 10:
                self.spacers[int(deconBody[4])-1].coord -= 1
                self.spacers[int(deconBody[4])-1].setValue(self.spacers[int(deconBody[4])-1].coord)
            elif self.spacers[int(deconBody[4])-1].coord > 10:
                self.spacers[int(deconBody[4])-1].coord = 10
            return
        if "SURFACE" in deconBody[5] and len(deconBody) < 6:
            if self.spacers[int(deconBody[4])-1].coord >= 0:
                self.spacers[int(deconBody[4])-1].coord += 1
                self.spacers[int(deconBody[4])-1].setValue(self.spacers[int(deconBody[4])-1].coord)
            elif self.spacers[int(deconBody[4])-1].coord < 0:
                self.spacers[int(deconBody[4])-1].coord = 0
            return
        print(deconBody[0][2:])
        mess = deconBody[5][:-1]
        if deconBody[0][2:] == "PACKAGE":
            print("PACKAGE GET")
            print(deconBody[4])
            #print(deconBody)
            self.greeters[int(deconBody[4])-1].setText(mess)
        if "EXIT" in bodyStr:
            print("bye!")
            self.connection.close()
            sys.exit()
    @Slot()
    def dig(self):
        butt = self.focus_widget()
        if self.spacers[butt.position].coord <= 10:
            self.spacers[butt.position].coord -= 1
            self.spacers[butt.position].setValue(self.spacers[butt.position].coord)
        elif self.spacers[butt.position].coord > 10:
            self.spacers[butt.position].coord = 10
    @Slot()
    def surface(self):
        butt = self.focus_widget()
        if self.spacers[butt.position].coord >= 0:
            self.spacers[butt.position].coord += 1
            self.spacers[butt.position].setValue(self.spacers[butt.position].coord)
        elif self.spacers[butt.position].coord < 0:
            self.spacers[butt.position].coord = 0


    def emission(self, pos):
        message = self.greeters[pos].text()
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )


    def __init__(self):
        #t = threading.Thread(Heartbeat.__init__)
        #t.start()
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])
        #self.connection = bep.connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')
        #bep = Heartbeat()
        #t = threading.Thread(bep.run)
        #t.start()
        #bep.start()
        result = self.channel.queue_declare('')

        queue_name = result.method.queue
        self.position = 0
        self.routing_key = 'trout'
        self.message = 'init'
        #self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body=self.message)
        print("[x] Sent %r:%r" % (self.routing_key, self.message))


        QWidget.__init__(self)
        self.hello =  [
                "hallo",
                "hi",
                "hola"
                ]

        self.buttons = []
        self.greeters = []
        self.senders = []
        self.spacers = []
        self.diggers = []
        self.surfacers = []
        self.resize(1115, 550)
        self.layout = QGridLayout(self)
        self.layout.set_horizontal_spacing(0)
        self.layout.set_vertical_spacing(0)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(28):
            self.set_window_title("Main")
            if i >= 6:
                mess = QLineEdit("Messages!")
                mess.position = i
                mess.coord = 8
            else:
                mess = QLabel("HEADER")
                mess.position = i
                mess.coord = 8
                mess.set_alignment(Qt.AlignBottom | Qt.AlignCenter)
                mess.setText("HEADER")
                mess.setStyleSheet("margin:0 auto;")
                mess.show()
            #mess.returnPressed.connect(self.greet)
            self.greeters.append(mess)
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 0, 2, 1)
            if mess.coord < 10:
                spacer = QProgressBar()
                spacer.coord = 8
                spacer.setMaximum(10)
                spacer.set_format("")
                if i < 10:
                    spacer.setStyleSheet("background-color:#bc6797;")
                    self.layout.add_widget(spacer, i, 6)

                    self.spacers.append(spacer)
            if i < 10:
                nameButton = QPushButton("+")
                nameButton.position = i
                nameButton.clicked.connect(self.surface)
            else:
                nameButton = QPushButton("NAME")
            #nameButton.clicked.connect(self.name_detail)
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 4)
            if i < 10:
                button = QPushButton("-")
                button.position = i
                button.clicked.connect(self.dig)
            else:
                button = QPushButton(str(i))
            if i == 10:
                b = QPushButton("Messages as they are added\n0:0:0:0:0:0:0:0:0:0")
                #this should be added to a collection
                self.layout.add_widget(b, i, 6, 28, 1)
            button.setStyleSheet("color:red;")
            #self.position = i
            button.position = i
            self.layout.add_widget(button, i, 5)
            if i < 6:
                head = QPushButton("GLOBAL")
                head.setStyleSheet("background-color:orange;")
                head.position = i
                self.senders.append(head)
                self.layout.add_widget(head, i, 3)
            else:
                print("And a small green alien that only homer can see")
                send = QPushButton("SEND")
                send.setStyleSheet("color:aqua;")
                send.position = i
                #send.clicked.connect(self.greetNoColour)
                #button.clicked.connect(self.greet)
                self.senders.append(send)
                #self.layout.add_widget(send, i, 3)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.setStyleSheet("background-color:#bc6797;")
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QPushButton(nameDetail)
            #labelDetail.clicked.connect(self.emission)
            self.nameDetailLayout.add_widget(labelDetail)

        self.established = False

        #creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        #self.channel = self.connection.channel()
        #self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        #result = self.channel.queue_declare('', exclusive=True)

        #queue_name = result.method.queue

        binding_keys = 'trout'
        self.channel.queue_bind(exchange='topicex', queue=queue_name, routing_key=binding_keys)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.consumeCallback, auto_ack=True)
        self.routing_key = 'trout'
        self.message = 'init'
        self.show()
        #self.channel.start_consuming()

class Heartbeat(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
    def run(self):
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body="bip")
        print("[x] Sent %r:%r" % (self.routing_key, "bip"))
        while True:
            time.sleep(20)
            self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body="bip")
            print("[x] Sent %r:%r" % (self.routing_key, "bip"))

class RocketWrite(QWidget):
    def calc_red(self):
        red = randint(1, 255)
        if red < 0:
            red = 0
        self.red = str(red)
        return red
    def calc_green(self):
        green = randint(1, 255)
        if green < 0:
            green = 0
        self.green = str(green)
        return green
    def calc_blue(self):
        blue = randint(1, 255)
        if blue < 0:
            blue = 0
        self.blue = str(blue)
        return blue

    def reconnect(self):
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body="bip")
        print("[x] Sent %r:%r" % (self.routing_key, "bip"))


    def emission(self, pos):
        self.calc_red()
        self.calc_green()
        self.calc_blue()
        message = "PACKAGE:"+self.red+":"+self.green+":"+self.blue+":"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text = self.greeters[pos].text
        #self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )



    def emissionNoColour(self, pos):
        message = "PACKAGE::::"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text() = self.greeters[pos].text()
        #self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )



    def __init__(self):
        #t = threading.Thread(Heartbeat.__init__)
        #t.start()
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])
        bep = Heartbeat()
        bep.start()
        #self.connection = bep.connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')
        #bep = Heartbeat()
        #t = threading.Thread(bep.run)
        #t.start()
        #bep.start()
        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
        self.message = 'init'
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body=self.message)
        print("[x] Sent %r:%r" % (self.routing_key, self.message))


        QWidget.__init__(self)
        self.hello =  [
                "hallo",
                "hi",
                "hola"
                ]

        self.buttons = []
        self.greeters = []
        self.senders = []
        self.resize(800, 150)
        self.layout = QGridLayout(self)
        self.layout.set_horizontal_spacing(0)
        self.layout.set_vertical_spacing(0)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(6):
            self.set_window_title("Global headers")
            mess = QLineEdit("Messages!")
            mess.position = i
            mess.set_max_length(60)
            mess.returnPressed.connect(self.greet)
            self.greeters.append(mess)
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 0)
            nameButton = QPushButton(sys.argv[2])
            nameButton.clicked.connect(self.name_detail)
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 1)
            button = QPushButton(str(i))
            button.setStyleSheet("color:orange;")
            #self.position = i
            button.position = i
            self.layout.add_widget(button, i, 2)
            send = QPushButton("SEND")
            send.setStyleSheet("color:aqua;")
            send.position = i
            send.clicked.connect(self.greetNoColour)
            button.clicked.connect(self.greet)
            self.senders.append(send)
            self.layout.add_widget(send, i, 3)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.setStyleSheet("background-color:#bc6797;")
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QPushButton(nameDetail)
            #labelDetail.clicked.connect(self.emission)
            self.nameDetailLayout.add_widget(labelDetail)

        self.established = False
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Property(QWidget)
    def conn():
        return self.connection
    @Slot()
    def name_detail(self):
        #code for showing a string in an array
        if not self.established:
            filename = '101/1.txt'
            out = []
            outString = ""
            count = 0
            with open(filename) as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    outString += lines[i]
                count += 1
            #print(outString)
            l = QLabel(outString)

            self.nameDetail.layout().add_widget(l)
            l.show()
            self.established = True
        #self.nameDetail.setText(outString)
        self.nameDetail.resize(450, 500)
        self.nameDetail.setStyleSheet("background:black;font:Courier New;color:pink;")
        self.nameDetail.show()
    @Slot()
    def greet(self):
        butt = self.focus_widget()
        try:
            self.emission(butt.position)
            for b in self.greeters:
                #print(b.position)
                if b.position == butt.position + 1:
                    #print("Triggered")
                    b.setFocus()
                    b.set_text("")
        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emission(butt.position)
            for b in self.greeters:
                #print(b.position)
                if b.position == butt.position + 1:
                    #print("Triggered")
                    b.setFocus()
                    b.set_text("")

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)
    @Slot()
    def greetNoColour(self):
        butt = self.focus_widget()
        try:
            self.emissionNoColour(butt.position)

        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emissionNoColour(butt.position)

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)

    @Slot()
    def boop():
        print("boop")
        #self.message.text = random.choice(self.hello)


if __name__ == "__main__":
    if len(sys.argv) != 4 :
        print("Usage is python main.py <username> <password> <url of rabbitmq server> <db name> <db user>")
        sys.exit()


    #create the database Connection
    #conn = psycopg2.connect("dbname="+sys.argv[4]+" user="+sys.argv[5])
    #cur = conn.cursor()

    #cur.execute("SELECT * FROM threads")

    #records = cur.fetchall()
    #print(records)

    app = QApplication([])

    widget = RocketWrite()
    recv = Receiver()
    input = InputBox()
    #This is because consuming messages is a blocking function
    #tt = threading.Thread(target=input.channel.start_consuming)
    t = threading.Thread(target=recv.channel.start_consuming)
    widget.show()
    input.show()
    t.start()


    #tt.start()
    #bip = threading.Thread(target=Heartbeat.__init__)
    #bip.start()
    app.exec()
    #This is because app.exec() was just wrapped in sys.exit()
    #and I need to do some closing
    #
    widget.connection.close()
    sys.exit()
