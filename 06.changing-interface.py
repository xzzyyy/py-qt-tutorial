from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gopa")

        self.button = QPushButton("Эээ слыш")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)
        self.setMaximumSize(QSize(500, 200))
        self.setMinimumSize(QSize(300, 100))

    def button_clicked(self):
        caption = self.windowTitle()
        if not caption.endswith("!"):
            self.setWindowTitle("Эээ слыш!")
        elif caption.endswith("!!!"):
            self.button.setText("Иди нахуй!")
            self.button.setEnabled(False)
        else:
            self.setWindowTitle(caption + "!")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
