from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QShortcut
import moderngl


class Window(QOpenGLWidget):
    frame_rate = 61

    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)

        fmt = QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QSurfaceFormat.CoreProfile)
        fmt.setSamples(4)
        QSurfaceFormat.setDefaultFormat(fmt)
        self.setFormat(fmt)

        QShortcut(Qt.Key_Escape, self, self.quit)

    #-------------
    #open gl logic
    #-------------
    def initializeGL(self):
        self.ctx = moderngl.create_context(require=330)
        self.ctx.clear(0.2, 0.4, 0.6)
        self.ctx.multisample = True
        

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        pass

    

    def quit(self):
        self.close()

    @classmethod
    def run(cls):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app = QApplication([])
        main = cls()
        main.show()
        app.exec_()


if __name__ == "__main__":
    Window.run()
