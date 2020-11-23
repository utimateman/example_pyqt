import sys
from PyQt5 import QtWidgets, uic


# https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/#importing-the-ui-file-in-python

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main_page.ui',self)

        self.ok_button = self.findChild(QtWidgets.QPushButton,'ok_button')
        self.ok_button.clicked.connect(self.changeLabel)

        self.text_input = self.findChild(QtWidgets.QTextEdit, 'text_edit')

        self.label = self.findChild(QtWidgets.QLabel, 'label')
        
        self.show()

    def changeLabel(self):
        input_value = self.text_input.toPlainText()
        print("the button is clicked, the value is:", input_value)
        self.label.setText("Hello " + input_value)
        self.repaint()       


app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec_())
