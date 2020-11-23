import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


# https://stackoverflow.com/questions/56867107/how-to-make-a-multi-page-application-in-pyqt5


# [ SECTION 1 ] - parent class which provided core function for swapping user interface pages
class PageWindow(QtWidgets.QMainWindow):

    # signaling object
    gotoSignal = QtCore.pyqtSignal(str)

    # signal emiting function
    def goto(self, name):
        self.gotoSignal.emit(name)



# [ SECTION 2 ] - interface pages
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
    #     pass


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


# same idea, just more page
class InstructionWindow(PageWindow):
    def __init__(self):
        super(InstructionWindow, self).__init__()
        uic.loadUi('ui/instruction_page.ui',self)
        self.initUI()
        self.setWindowTitle("InstructionWindow")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        self.ok_button = self.findChild(QtWidgets.QPushButton,'back_button')
        self.ok_button.clicked.connect(self.goToWelcomePage)

    def goToWelcomePage(self):
        self.goto("welcome_page")
 

# [ SECTION 3 ] - Main window pages
class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # like a list that contains user interfaces
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # dictionary to switch pages
        self.m_pages = {}

        self.register(WelcomeWindow(), "welcome_page")
        self.register(MainWindow()   , "main_page")
        self.register(InstructionWindow()   , "instruction_page")

        self.goto("welcome_page")

    # register user interfaces page into the dictionary
    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    # integrate dictionary with user interface function to be able to switch pages
    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.resize(640,480)
    w.show()
    sys.exit(app.exec_())
