from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QShortcut


class Window(QOpenGLWidget):
    frame_rate = 61

    def __init__(self):
        super().__init__()

        fmt = QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QSurfaceFormat.CoreProfile)
        fmt.setSamples(4)
        QSurfaceFormat.setDefaultFormat(fmt)
        self.setFormat(fmt)

        QShortcut(Qt.Key_Escape, self, self.quit)

    def quit(self):
        self.close()

    @classmethod
    def run(cls):
        app = QApplication([])
        main = cls()
        main.show()
        app.exec_()


if __name__ == "__main__":
    Window.run()