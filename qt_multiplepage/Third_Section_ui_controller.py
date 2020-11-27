import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# https://stackoverflow.com/questions/56867107/how-to-make-a-multi-page-application-in-pyqt5
# special thanks for @eyllanesc

# import those interface pages object to main program
from First_Section_PageWindow import PageWindow # for initalize every QWidgets object
from Second_Section_ui_welcome_page import WelcomeWindow
from Second_Section_ui_main_page import MainWindow
from Second_Section_ui_instruction_page import InstructionWindow



# [ SECTION 3 ] - Main Window for the program
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
