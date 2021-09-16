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
        self.channel.start_consuming()
        self.routing_key = 'trout'
        self.message = 'init'


if __name__ == "__main__":
    widget = Receiver()

    threading.Thread(target=widget.channel.start_consuming())
