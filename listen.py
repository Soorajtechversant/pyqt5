from PyQt5 import QtCore  , QtGui , QtWidgets , uic
from start import *



class PostDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_start() #code from designer!!
        self.ui.setupUi(self)

        self.ui.plainTextEdit.installEventFilter(self)

    def eventFilter(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            print(event.text())
            # do some stuff ...
            return True # means stop event propagation
        
        else:
            return QtGui.QDialog.eventFilter(self, event)
        