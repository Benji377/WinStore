from PyQt5.QtWidgets import *


class ReportMessage(QMessageBox):

    def __init__(self, parent=None):
        super(ReportMessage, self).__init__(parent)
        self.setIcon(QMessageBox.Information)
        # Default icon from PyQt database
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxInformation')))
        self.setWindowTitle("Report an issue")
        self.setText("If you find any issue in using the app or have any other questions don't hesitate "
                     "to contact me!\nSpam mail will be permanently banned\n\n"
                     "Email: demetzbenjamin23@gmail.com")
