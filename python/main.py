import PySide6

print(PySide6.__version__)

import random
import sys

from PySide6.QtCore import Qt, Slot
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
        self.button = QPushButton("Click me!")
        self.message = QLabel("Hallo world")
        self.message.alignment = Qt.AlignCenter

        self.layout = QVBoxLayout(self)
        self.layout.add_widget(self.message)
        self.layout.add_widget(self.button)

        self.button.clicked.connect(self.greet)

    @Slot()
    def greet(self):
        self.message.text = random.choice(self.hello)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Hallo()
    widget.show()

    sys.exit(app.exec_())
