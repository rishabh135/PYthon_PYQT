import sys
from PyQt4 import QtGui , QtCore


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)








        self.statusBar().showMessage('Ready')



        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(75, 75)
        qbtn.setToolTip("This is a <i> Quit button </i>")

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(150, 150)

        lbl1 = QtGui.QLabel('Eat', self)
        lbl1.move(215, 310)

        lbl2 = QtGui.QLabel('Code', self)
        lbl2.move(305, 405)

        lbl3 = QtGui.QLabel('Learn', self)
        lbl3.move(350, 4700)

        checkbox=QtGui.QCheckBox("Enlarge the Video",self)
        checkbox.move(10,10)
        checkbox.stateChanged.connect(self.enlarged_window)
        
        self.setGeometry(300, 300, 550, 550)
        self.setWindowTitle('Tooltips')




        self.progress=QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("Download" , self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)


        extractAction = QtGui.QAction("Get to Disneyland",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the Appl")
        extractAction.triggered.connect(self.close_application)

        mainMenu = self.menuBar()



        openEditor =QtGui.QAction("&EDITOT" , self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)



        openFile = QtGui.QAction("&OPEN FILE" , self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_open)
        fileMenu= mainMenu.addMenu('&FilE')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)

        saveFile = QtGui.QAction("&OPEN FIL1234" , self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Open Fiuhfdsuohfdsouh")
        saveFile.triggered.connect(self.file_save)
        fileMenu.addAction(saveFile)


        self.show()

    def file_save(self):
        name=QtGui.QFileDialog.getSaveFileName(self,"Save File")
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self , "Open File")
        file = open(name, 'r')
        self.editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def close_application(self):
        print("Yahtzee")
        sys.exit()

    def download(self):
        self.completed=0
        while self.completed <100:
            self.completed+=0.001
            self.progress.setValue(self.completed)

    def enlarged_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(250,350,200,300)

        else:
            self.setGeometry(400,40,202,350)

    def editor(self):
        self.textEdit= QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)



    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit fdsfdsf?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
