
from PyQt5 import QtCore, QtGui, QtWidgets
from showitems import Ui_showing

class Ui_start(object):
    

    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(914, 450)
        self.centralwidget = QtWidgets.QWidget(start)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 70, 231, 71))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.openwindow)
        
   
        
        
        start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 22))
        self.menubar.setObjectName("menubar")
        start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(start)
        self.statusbar.setObjectName("statusbar")
        start.setStatusBar(self.statusbar)

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)
    
    
 
    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "start"))
        self.pushButton.setText(_translate("start", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = QtWidgets.QMainWindow()
    ui = Ui_start()
    ui.setupUi(start)
    start.show()
    sys.exit(app.exec_())
