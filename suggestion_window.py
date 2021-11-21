from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import validators

import database_controller
import error_message


class SuggestionWindow(QDialog):

    def __init__(self, parent=None):
        super(SuggestionWindow, self).__init__(parent)
        self.setFixedSize(500, 220)
        self.setWindowTitle("Suggestions")
        self.setModal(True)
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxInformation')))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        username_label = QLabel("Your name:", self)
        username_label.setGeometry(40, 20, 100, 30)
        username_label.setFont(QFont('SansSerif', 12))

        username_entry = QLineEdit(self)
        username_entry.setGeometry(150, 20, 300, 30)
        username_entry.setToolTip("This name will be displayed in the credits if we accept your suggestion")

        appname_label = QLabel("App name:", self)
        appname_label.setGeometry(40, 70, 100, 30)
        appname_label.setFont(QFont('SansSerif', 12))

        appname_entry = QLineEdit(self)
        appname_entry.setGeometry(150, 70, 300, 30)
        appname_entry.setToolTip("The official name of the app")

        applink_label = QLabel("Link to app:", self)
        applink_label.setGeometry(40, 120, 100, 30)
        applink_label.setFont(QFont('SansSerif', 12))

        applink_entry = QLineEdit(self)
        applink_entry.setGeometry(150, 120, 300, 30)
        applink_entry.setToolTip("Copy-paste the link of the app's official website here")

        submit_button = QPushButton("Submit", self)
        submit_button.setGeometry(200, 170, 100, 30)
        submit_button.clicked.connect(lambda: submit_sug())

        def submit_sug():
            username = username_entry.text()
            appname = appname_entry.text()
            applink = applink_entry.text()
            errormsg = error_message.ErrorMessage()

            if not username or not appname or not applink:
                errormsg.seterror("All fields need to be filled out", "Unfilled fields")
                errormsg.exec_()
            elif validators.url(applink):
                data = database_controller.Database()
                data.connect()
                if data.url_validator(applink):
                    data.insert_suggestion(username, appname, applink)
                    self.close()
                else:
                    errormsg.seterror("Link already in our database.\n"
                                      "Try searching it by its name or report an issue if you can't find it",
                                      "Existing URL")
                    errormsg.exec_()
                    self.close()
            else:
                errormsg.seterror("Provided link is invalid", "Invalid URL")
                errormsg.exec_()

