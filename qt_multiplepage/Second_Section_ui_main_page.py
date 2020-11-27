import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from First_Section_PageWindow import PageWindow # for initalize every QWidgets object



# [ SECTION 2 ] - Interfacing and Program Logic

# same idea, just more page
class MainWindow(PageWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main_page.ui',self)
        self.initUI()
        self.setWindowTitle("MainWindow")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        self.ok_button = self.findChild(QtWidgets.QPushButton,'back_button')
        self.ok_button.clicked.connect(self.goToWelcomePage)

    def goToWelcomePage(self):
        self.goto("welcome_page")