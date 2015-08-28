__author__ = 'Rishabh'
import sys

from PyQt4 import QtGui


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts !!!")
        self.setWindowIcon(QtGui.QIcon("\AppData\Local\Temp\imgres.jpg"))

        extractaction = QtGui.QAction("&Get to the Choppah", self)
        extractaction.setShortcut("Ctrl + Q")
        extractaction.setStatusTip("Leave the APP")
        extractaction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractaction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application())
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)
        self.show()

    def close_application(self):
        print("Whoadsadsad ")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
print("fdfdoigerjgoreeeeeeeeeeeeeee")
input("press enter to output")
