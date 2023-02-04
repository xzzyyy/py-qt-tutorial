from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt


class MemorizingApp(QMainWindow):

    def __init__(self):
        super(MemorizingApp, self).__init__()

        self.setWindowTitle("Gopa")
        label = QLabel("Idi nahuy!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)


app = QApplication([])

window = MemorizingApp()
window.show()

app.exec()
