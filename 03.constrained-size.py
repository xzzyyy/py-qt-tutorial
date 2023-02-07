from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gopa")
        label = QLabel("Idi nahuy!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setMaximumSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 100))
        self.setCentralWidget(label)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
