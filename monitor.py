import sys
from PyQt5.QtWidgets import (QApplication,QWidget)
from PyQt5 import Qt


class Print(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        print(event.text())
        # print(event.())

def Display_Tweets(self):
    readtweets = open("Tweetfile", "r")
    tweetlist = readtweets.readlines()
    for x in tweetlist:
        self.plainTextEdit.append(x)
    readtweets.close()   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo =  Print()
    demo.show()
    sys.exit(app.exec_())