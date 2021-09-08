import PySide6

print(PySide6.__version__)

import random
import sys
import os
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtCore import QUrl, Qt, Slot, Property
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QGridLayout, QWidget)
from __feature__ import snake_case, true_property

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
        for i in range(28):
            mess = QPushButton("Messages!")
            self.layout.add_widget(mess, i, 0)
            button = QPushButton(str(i))
            button.position = i
            self.layout.add_widget(button, i, 1)
            button.clicked.connect(self.greet)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Slot()
    def greet(self):
        butt = self.focus_widget()
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
    print(widget.buttons)
    #print(engine)
    #widget.layout.setStyleSheet("width: 450;height:550;")
    widget.show()
    sys.exit(app.exec())
