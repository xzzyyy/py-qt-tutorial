import random
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize


TITLES = [
    "pizda",
    "gopa",
    "idi nahuy",
    "zaebal",
    "pidor",
    "sosi",
    "poka"
]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gopa")
        self.windowTitleChanged.connect(self.title_changed)

        self.button = QPushButton("Эээ слыш")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)
        self.setMaximumSize(QSize(500, 200))
        self.setMinimumSize(QSize(300, 100))

    def button_clicked(self):
        self.setWindowTitle(random.choice(TITLES))

    def title_changed(self, new_title):
        print("new title:", new_title)
        if new_title == TITLES[-1]:
            self.button.setDisabled(True)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
