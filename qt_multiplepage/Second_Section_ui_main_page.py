import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from First_Section_PageWindow import PageWindow # for initalize every QWidgets object

# [ SECTION 4 ] - Logic Part
from Fourth_Section_logic_controller import LogicController

# [ SECTION 2 ] - Interfacing and Program Logic

# same idea, just more page
class MainWindow(PageWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main_page.ui', self)
        self.initUI()
        self.setWindowTitle("MainWindow")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        # initilize and connecting components

        self.ok_button = self.findChild(QtWidgets.QPushButton,'back_button')
        self.ok_button.clicked.connect(self.goToWelcomePage)
        
        self.food_name_label = self.findChild(QtWidgets.QLabel, 'food_name_label')

        self.record_button = self.findChild(QtWidgets.QPushButton,'record_button')
        self.record_button.clicked.connect(self.randomMenu)

    def goToWelcomePage(self):
        self.goto("welcome_page")

    
    def randomMenu(self):
        # calling logic part object
        lc = LogicController()
        food_name = lc.saveFoodRecords()

        # update user interface (ui)
        self.food_name_label.setText(food_name)