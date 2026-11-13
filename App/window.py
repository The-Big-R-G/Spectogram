from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QShortcut
import moderngl
import time


class Window(QOpenGLWidget):
    frame_rate = 61

    def __init__(self):
        super().__init__()
        self.t = None
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
        self.init()
        

    def resizeGL(self, w, h):
        self.size(w, h)

    def paintGL(self):
        now = time.time()
        dt = now - self.t if self.t is not None else 1.0 / self.frame_rate
        self.t = now
        self.draw(dt)

    

    def quit(self):
        self.exit()
        self.close()

    @classmethod
    def run(cls):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app = QApplication([])
        main = cls()
        main.show()
        app.exec_()



    #----------------
    # Interface
    #----------------

    def init(self):
        print("init")

    def size(self,w,h):
        print("size",w,h)

    def draw(self, dt):
        print("draw", dt)

    def exit(self):
        print('exit')

if __name__ == "__main__":
    Window.run()
