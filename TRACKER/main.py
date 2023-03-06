from PyQt5.QtWidgets import *
from PyQt5 import uic
from pynput import keyboard
import os
import mysql.connector
from datetime import datetime
from PyQt5.QtCore import  QTimer


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
        # self.pushButton_2.clicked.connect(exit)
        self.pushButton_2.clicked.connect(self.stoptracking)
        self.actionStop_and_Exit_Tracker.triggered.connect(exit)
    
    
    def db_insertion(self):
        

            sql = """INSERT INTO TrackerSummary (date, start_time, end_time, total_alphanumeric_keys, total_special_keys) VALUES (%s,%s,%s,%s,%s)"""

            self.mycursor.execute(sql, (self.date, self.start_time, self.end_time, self.alphanumeric_key_count,self.special_key_count))
            self.mydb.commit()

            summery_id = self.mycursor.lastrowid
            details_row = list()
            for keys in self.key_pressed:
                details_row.append((keys, summery_id))

            sql = """INSERT INTO TrackerDetails (Keys_pressed, summary_id) VALUES (%s,%s)"""

            self.mycursor.executemany(sql, (details_row))
            self.mydb.commit()
            self.mydb.close()
        
       
    def on_clicked( self ,key ):
        
        
            try:
                text = ("///key [ {0} ] pressed ///".format(
                        key.char))
                f.writelines(text)
                self.alphanumeric_key_count += 1
                    
            except AttributeError:
                text = ("///special key {0} pressed///".format(
                        key))
                f.writelines(text)
                self.special_key_count += 1
                
                f.flush()
            self.key_pressed.append(text) 
            
    def on_release( self, key ):
        
       
            text = ("///key [ {0} ] released ///".format(
                key))
            f.writelines(f'{text} \n')
            f.flush()
            self.key_pressed.append(text)    
     
    def login(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'password':
            self.pushButton_2.setEnabled(True)
            
            
            #############
            message = QMessageBox()
            message.setText('Tracker is Running')
            message.exec_()           
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="tracker",
            password="Tracker@1",
            database="SystemTracker"
            )
            self.mycursor = self.mydb.cursor()
            self.start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.date = datetime.now().date()

            self.key_pressed = list()
            
            self.alphanumeric_key_count = 0
            self.special_key_count = 0
            #########################    
            self.listener = keyboard.Listener(on_press=self.on_clicked, on_release=self.on_release)
            
            self.listener.start()    
        else:
            message = QMessageBox()
            message.setText('Invalid Login')
            message.exec_()
    
    def stoptracking(self):
         self.end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.db_insertion()
         exit()    
    # listener = keyboard.Listener(on_press= on_clicked, on_release=on_release)
    # listener.start()
                  
def main():
    app =  QApplication([])
    window = MyGUI()
    window.show()
    
    key_pressed = list()
    alphanumeric_key_count = 0
    special_key_count = 0
    
    app.exec_()
    f.close()     

   
          
if __name__ == '__main__':
        main()
        
