from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel("чё смотришь?")
        self.label.setMouseTracking(True)

        self.setWindowTitle("Gopa")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    @staticmethod
    def point_to_str(p):
        return "%d, %d" % (p.x(), p.y())

    def mouseMoveEvent(self, e):
        self.label.setText(self.point_to_str(e.position()))

    def mousePressEvent(self, e):
        self.label.setText("%s, pressed" % self.point_to_str(e.position()))

    def mouseReleaseEvent(self, e):
        self.label.setText("%s, released" % self.point_to_str(e.position()))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
