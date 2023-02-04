from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MemorizingApp(QMainWindow):

    def __init__(self):
        super(MemorizingApp, self).__init__()

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

window = MemorizingApp()
window.show()

app.exec()
