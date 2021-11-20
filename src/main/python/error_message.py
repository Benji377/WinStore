from PyQt5.QtWidgets import *


class ErrorMessage(QMessageBox):

    def __init__(self, parent=None):
        super(ErrorMessage, self).__init__(parent)
        self.setIcon(QMessageBox.Critical)
        # Default icon from PyQt database
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxCritical')))
        self.setWindowTitle("Error")
        self.setText("Error")

    def seterror(self, mess=None, ti=None):
        self.setText(mess)
        self.setWindowTitle(ti)
