import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# Parent class which provided core function for swapping user interface pages
class PageWindow(QtWidgets.QMainWindow):

    # signaling object
    gotoSignal = QtCore.pyqtSignal(str)

    # signal emiting function
    def goto(self, name):
        self.gotoSignal.emit(name)

