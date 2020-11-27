import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from First_Section_PageWindow import PageWindow # for initalize every QWidgets object



# [ SECTION 2 ] - Interfacing and Program Logic

class WelcomeWindow(PageWindow):

    # load the user interface file
    def __init__(self):
        
        # parent class initialization (haven't teach you yet :p)
        super(WelcomeWindow, self).__init__()

        # load file
        uic.loadUi('ui/welcome_page.ui',self)

        # connect elements
        self.initUI()

        # set title
        self.setWindowTitle("WelcomeWindow") 

    # connecting elements in user interface file
    def initUI(self):
        self.UiComponents()

    def UiComponents(self):

        # connecting buttons to variables
        self.ok_button = self.findChild(QtWidgets.QPushButton,'start_button')

        # connecting buttons with function
        self.ok_button.clicked.connect(self.goToMainPage)

        # connecting buttons to variables
        self.instruction_button = self.findChild(QtWidgets.QPushButton,'instruction_button')

        # connecting buttons with function
        self.instruction_button.clicked.connect(self.goToInstructionPage)

        # Examples
        #
        # self.button_a = self.findChild(QtWidgets.QPushButton,'a_button')
        # self.button_a.clicked.connect(self.functionA)
        #
        # self.button_b = self.findChild(QtWidgets.QPushButton,'b_button')
        # self.button_b.clicked.connect(self.functionA)
        #
        # self.button_c = self.findChild(QtWidgets.QPushButton,'c_button')
        # self.button_c.clicked.connect(self.functionC)
        
    # functions
    def goToMainPage(self):
        self.goto("main_page")

    def goToInstructionPage(self):
        self.goto("instruction_page")

    # Example Functions
    #
    # def functionA(self):
    #     pass
    #
    # def functionB(self):
    #     pass
    #
    # def functionC(self):
    #     pa