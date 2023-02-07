from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        cont = QWidget()
        cont.setLayout(layout)

        self.setWindowTitle("Gopa")
        self.setCentralWidget(cont)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
