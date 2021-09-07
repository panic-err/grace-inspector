import PySide6

print(PySide6.__version__)

import random
import sys
import os
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl, Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
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

        self.layout = QVBoxLayout(self)
        for i in range(28):
            button = QPushButton(str(i))
            button.position = i
            self.layout.add_widget(button)
            button.clicked.connect(self.greet)
            self.buttons.append(button)

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
    engine = QQmlApplicationEngine()
    qml_file_path = "../qml/window.qml"
    motor = engine.load(qml_file_path)
    button_file_path = "../qml/button.qml"
    buttons = engine.load(button_file_path)
    widget = Hallo()

    widget.show()
    
    sys.exit(app.exec())
