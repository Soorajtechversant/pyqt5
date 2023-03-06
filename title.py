from PyQt5 import QtCore, QtGui, QtWidgets
import os
import io
class Ui_titlehere(object):
    def setupUi(self, titlehere):
        titlehere.setObjectName("titlehere")
        titlehere.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(titlehere)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit_srj = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_srj.setEnabled(True)
        self.plainTextEdit_srj.setGeometry(QtCore.QRect(20, 40, 601, 261))
        self.plainTextEdit_srj.setOverwriteMode(True)
        self.plainTextEdit_srj.setCenterOnScroll(True)
        self.plainTextEdit_srj.setObjectName("plainTextEdit_srj")
        titlehere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(titlehere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        titlehere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(titlehere)
        self.statusbar.setObjectName("statusbar")
        titlehere.setStatusBar(self.statusbar)

        self.retranslateUi(titlehere)
        QtCore.QMetaObject.connectSlotsByName(titlehere)
   
    def Display_Tweets(self):
        readtweets = open("prova3.txt", "r")
        tweetlist = readtweets.readlines()
        for x in tweetlist:
            self.plainTextEdit_srj.appendPlainText(x)     
            readtweets.close()
        
    def retranslateUi(self, titlehere):
        _translate = QtCore.QCoreApplication.translate
        titlehere.setWindowTitle(_translate("titlehere", "titleheredude"))
        self.plainTextEdit_srj.setPlainText(_translate("titlehere", ' ' ))
        
        
        binary_file = io.open('prova3.txt', 'r')
        text_file = io.TextIOWrapper(binary_file, encoding='utf-8', newline='')
        print(text_file)
        
        self.plainTextEdit_srj.appendPlainText( text = text_file )
        self.plainTextEdit_srj.setPlaceholderText(_translate("titlehere", "your codes here"))



    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    titlehere = QtWidgets.QMainWindow()
    ui = Ui_titlehere()
    ui.setupUi(titlehere)
    titlehere.show()
    sys.exit(app.exec_())
