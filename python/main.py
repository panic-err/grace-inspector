import PySide6

print(PySide6.__version__)

import pika
import sys

import random
import sys
import os
from PySide6.QtQuick import QQuickWindow
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtCore import QUrl, Qt, Slot, Property
from PySide6.QtWidgets import (QWidget, QDialog, QVBoxLayout, QApplication, QLineEdit, QLabel, QPushButton, QGridLayout)
from __feature__ import snake_case, true_property

class EmQue():
    def run(self):
        connection = pika.BlockingConnection(pika.ConnnectionParameters(host='weasel:1joker@biggest.dumpster.world'))
        channel = connection.channel()
        channel.exchange_declare(exchange_type('topic'), exchange='topic_logs')
        message = 'trout'
        channel.basic_publish(exchange='topic_logs', routing_key=self.routing_key, body=message)
        print("[x] Sent %r:%r" %(routing_key, self.message) )
        connection.close()

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='weasel:1joker@biggest.dumpster.world'))
        channel = connection.channel()
        channel.exchange_declare(exchange_type('topic'), exchange='topic_logs')

        self.routing_key = sys.argv[1] if len(sys.argv) > 2 else 'trout.*'
        self.message = 'Hallo'
        channel.basic_publish(exchange='topic_logs', routing_key=self.routing_key, body=self.message)
        print("[x] Sent %r:%r" % (routing_key, self.message))
        connection.close()

class Hallo(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.hello =  [
                "hallo",
                "hi",
                "hola"
                ]

        self.buttons = []

        self.resize(1000, 550)
        self.layout = QGridLayout(self)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(28):
            mess = QLineEdit("Messages!")
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 0)
            nameButton = QPushButton("NAME")
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 1)
            button = QPushButton(str(i))
            button.setStyleSheet("color:orange;")
            button.position = i
            self.layout.add_widget(button, i, 2)
            button.clicked.connect(self.greet)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QLabel(nameDetail)
            self.nameDetailLayout.add_widget(labelDetail)
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Slot()
    def greet(self):
        butt = self.focus_widget()
        self.nameDetail.resize(450, 500)
        self.nameDetail.setStyleSheet("color:pink;")
        self.nameDetail.show()
        print(butt.position)
    @Slot()
    def boop():
        print("boop")
        #self.message.text = random.choice(self.hello)


if __name__ == "__main__":
    app = QApplication([])
    #QtWebEngine.initialize()
    """
    engine = QQmlApplicationEngine()
    qml_file_path = "../qml/window.qml"
    motor = engine.load(qml_file_path)
    button_file_path = "../qml/button.qml"
    buttons = engine.load(button_file_path)"""
    widget = Hallo()
    #print(widget.buttons)
    #print(engine)
    #widget.layout.setStyleSheet("width: 450;height:550;")
    widget.show()
    sys.exit(app.exec())
