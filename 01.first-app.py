from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel

from PyQt6.QtCore import Qt


class FirstAppWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gopa")
        label = QLabel("Idi nahuy!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)


app = QApplication([])

window = FirstAppWindow()
window.show()

app.exec()
