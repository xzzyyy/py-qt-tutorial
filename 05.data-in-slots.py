from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize


class MemorizingApp(QMainWindow):

    def __init__(self):
        super(MemorizingApp, self).__init__()

        self.setWindowTitle("Gopa")

        self.button = QPushButton("Эээ слыш")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_checked)

        self.setCentralWidget(self.button)
        self.setMaximumSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 100))

    def button_clicked(self):
        self.button.setText(self.button.text() + "!")

    @staticmethod
    def button_checked(checked):
        print("checked:", checked)


app = QApplication([])

window = MemorizingApp()
window.show()

app.exec()
