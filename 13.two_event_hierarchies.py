from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMenu
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):

    def __init__(self):

        class OpaqueLabel(QLabel):
            def mouseMoveEvent(self, e):
                e.accept()

        class TransparentLabel(QLabel):
            def mouseMoveEvent(self, e):
                e.ignore()

        super().__init__()
        central_widget = QWidget(self)

        v_lay = QVBoxLayout()
        central_widget.setLayout(v_lay)
        h_lay = QHBoxLayout()
        h_lay_widget = QWidget(central_widget)
        h_lay_widget.setLayout(h_lay)

        self.label1 = QLabel(central_widget)
        self.label2 = QLabel(central_widget)
        self.label3 = OpaqueLabel(central_widget)
        self.label3.setText("filters events")
        self.label4 = TransparentLabel(central_widget)
        self.label4.setText("permits events")
        v_lay.addWidget(self.label1)
        v_lay.addWidget(self.label2)
        v_lay.addWidget(h_lay_widget)
        h_lay.addWidget(self.label3)
        h_lay.addWidget(self.label4)

        central_widget.setMouseTracking(True)
        h_lay_widget.setMouseTracking(True)
        self.label1.setMouseTracking(True)
        self.label2.setMouseTracking(True)
        self.label3.setMouseTracking(True)
        self.label4.setMouseTracking(True)
        self.setMouseTracking(True)

        self.setWindowTitle("Gopa")
        self.setCentralWidget(central_widget)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    @staticmethod
    def mouse_evt_str(e):
        mouse_buttons = []
        if e.buttons() & Qt.MouseButton.LeftButton:
            mouse_buttons.append("left")
        if e.buttons() & Qt.MouseButton.RightButton:
            mouse_buttons.append("right")
        elif e.buttons() & Qt.MouseButton.MiddleButton:
            mouse_buttons.append("middle")
        if not mouse_buttons:
            mouse_buttons.append("none")

        return "local: (%d, %d), global: (%d, %d), mouse: (%s)"\
               % (e.position().x(), e.position().y(), e.globalPosition().x(), e.globalPosition().y(),
                  ",".join(mouse_buttons))

    def mouseMoveEvent(self, e):
        self.label1.setText("move | %s" % self.mouse_evt_str(e))

    def mousePressEvent(self, e):
        self.label1.setText("pressed | %s" % self.mouse_evt_str(e))

    def mouseReleaseEvent(self, e):
        self.label1.setText("released | %s" % self.mouse_evt_str(e))

    def on_context_menu(self, pos):
        class MyMenu(QMenu):
            def __init__(self, main_win):
                super().__init__(main_win)
                self.main_win = main_win

            def mouseMoveEvent(self, e):
                self.main_win.label2.setText("in context menu")
                super().mouseMoveEvent(e)

        act1 = QAction("menu 1", self)
        act2 = QAction("menu 2", self)
        act3 = QAction("menu 3", self)
        act1.triggered.connect(self.menu1)
        act2.triggered.connect(self.menu2)
        act3.triggered.connect(self.menu3)

        cntxt_menu = MyMenu(self)
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
window = MainWindow()
window.show()
app.exec()
