import PySide6

print(PySide6.__version__)

import pika
import sys
import time

import threading
import random
import sys
import os

from PySide6.QtQuick import QQuickWindow
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtCore import QUrl, Qt, Slot, Property
from PySide6.QtWidgets import (QWidget, QDialog, QVBoxLayout, QApplication, QLineEdit, QLabel, QPushButton, QGridLayout)
from __feature__ import snake_case, true_property

class Receiver():

    def consumeCallback(self, ch, method, properties, body):
        print("[x], %r:%r" % (method.routing_key, body))
        bodyStr = str(body)
        if "EXIT" in bodyStr:
            print("bye!")
            self.connection.close()
            sys.exit()

    def emission(self, pos):
        message = self.greeters[pos].text
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )


    def __init__(self):

        creds = pika.PlainCredentials(sys.argv[1], sys.argv[2])
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[3], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        result = self.channel.queue_declare('', exclusive=True)

        queue_name = result.method.queue

        binding_keys = 'trout'
        self.channel.queue_bind(exchange='topicex', queue=queue_name, routing_key=binding_keys)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.consumeCallback, auto_ack=True)
        #self.channel.start_consuming()
        self.routing_key = 'trout'
        self.message = 'init'

class Heartbeat(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        creds = pika.PlainCredentials(sys.argv[1], sys.argv[2])

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[3], 5672, '/', creds))
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



    def emission(self, pos):
        message = self.greeters[pos].text
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )
        

    def __init__(self):
        #t = threading.Thread(Heartbeat.__init__)
        #t.start()
        creds = pika.PlainCredentials(sys.argv[1], sys.argv[2])
        bep = Heartbeat()
        bep.start()
        #self.connection = bep.connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[3], 5672, '/', creds))
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
        self.resize(1000, 550)
        self.layout = QGridLayout(self)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(28):
            mess = QLineEdit("Messages!")
            self.greeters.append(mess)
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 0)
            nameButton = QPushButton("NAME")
            nameButton.clicked.connect(self.name_detail)
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 1)
            button = QPushButton(str(i))
            button.setStyleSheet("color:orange;")
            self.position = i
            button.position = i
            self.layout.add_widget(button, i, 2)
            button.clicked.connect(self.greet)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QPushButton(nameDetail)
            #labelDetail.clicked.connect(self.emission)
            self.nameDetailLayout.add_widget(labelDetail)
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Property(QWidget)
    def conn():
        return self.connection
    @Slot()
    def name_detail(self):
        self.nameDetail.resize(450, 500)
        self.nameDetail.setStyleSheet("color:pink;")
        self.nameDetail.show()
    @Slot()
    def greet(self):
        butt = self.focus_widget()
        self.emission(butt.position)
        print("Butt  number"+str(butt.position)) 
        print(self.greeters[butt.position].text)
        print(butt.position)
    @Slot()
    def boop():
        print("boop")
        #self.message.text = random.choice(self.hello)


if __name__ == "__main__":
    app = QApplication([])
    
    widget = RocketWrite()
    recv = Receiver()
    #This is because consuming messages is a blocking function
    t = threading.Thread(target=recv.channel.start_consuming)
    widget.show()
    t.start()
    #bip = threading.Thread(target=Heartbeat.__init__)
    #bip.start()
    app.exec()
    #This is because app.exec() was just wrapped in sys.exit()
    #and I need to do some closing
    #
    widget.connection.close()
    sys.exit()
