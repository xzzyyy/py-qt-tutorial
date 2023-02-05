from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class ContextMenusWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cur_buttons = Qt.MouseButton.NoButton

        central_widget = QWidget(self)
        central_widget.setMouseTracking(True)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label1 = QLabel(central_widget)
        self.label2 = QLabel(central_widget)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.label1.setMouseTracking(True)
        self.label2.setMouseTracking(True)

        self.setWindowTitle("Gopa")
        self.setMouseTracking(True)
        self.setCentralWidget(central_widget)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def mouse_evt_str(self, e):
        mouse_buttons = []
        if self.cur_buttons & Qt.MouseButton.LeftButton:
            mouse_buttons.append("left")
        if self.cur_buttons & Qt.MouseButton.RightButton:
            mouse_buttons.append("right")
        elif self.cur_buttons & Qt.MouseButton.MiddleButton:
            mouse_buttons.append("middle")
        if not mouse_buttons:
            mouse_buttons.append("none")

        return "local: (%d, %d), global: (%d, %d), mouse: (%s)"\
               % (e.position().x(), e.position().y(), e.globalPosition().x(), e.globalPosition().y(),
                  ",".join(mouse_buttons))

    def mouseMoveEvent(self, e):
        self.cur_buttons = e.buttons()
        self.label1.setText("move | %s" % self.mouse_evt_str(e))

    def mousePressEvent(self, e):
        self.cur_buttons = e.buttons()
        self.label1.setText("pressed | %s" % self.mouse_evt_str(e))

    def mouseReleaseEvent(self, e):
        self.cur_buttons = e.buttons()
        self.label1.setText("released | %s" % self.mouse_evt_str(e))

    def on_context_menu(self, pos):
        act1 = QAction("menu 1", self)
        act2 = QAction("menu 2", self)
        act3 = QAction("menu 3", self)
        act1.triggered.connect(self.menu1)
        act2.triggered.connect(self.menu2)
        act3.triggered.connect(self.menu3)

        cntxt_menu = QMenu(self)
        cntxt_menu.addAction(act1)
        cntxt_menu.addAction(act2)
        cntxt_menu.addAction(act3)
        cntxt_menu.exec(self.mapToGlobal(pos))

    def menu1(self):
        self.label2.setText("menu 1: idi nahuy")

    def menu2(self):
        self.label2.setText("menu 2: tupaya")

    def menu3(self):
        self.label2.setText("menu 3: pizda")


app = QApplication([])

window = ContextMenusWindow()
window.show()

app.exec()
