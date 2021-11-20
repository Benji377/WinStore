import webbrowser
import database_controller
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import issue_report
import list_entry_widget
import suggestion_window


# Opens a new window when the user wants to submit a suggestion
def suggest_click():
    sug = suggestion_window.SuggestionWindow()
    sug.exec_()


# Opens a new window that helps the user report issues
def report_click():
    rep = issue_report.ReportMessage()
    rep.exec_()


# Is the main window of the program
class LandingPage(QMainWindow):
    databse = database_controller.Database()

    def __init__(self, parent=None):
        super(LandingPage, self).__init__(parent)
        self.setWindowTitle("WinStore")
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QIcon('./images/icon.png'))

        github_action = QAction("Github", self)
        github_action.triggered.connect(lambda: webbrowser.open("https://github.com/Benji377"))

        suggest_action = QAction("Suggest an app", self)
        suggest_action.triggered.connect(lambda: suggest_click())

        report_action = QAction("Report an issue", self)
        report_action.triggered.connect(lambda: report_click())

        menu_bar = self.menuBar()
        menu_bar.addAction(github_action)
        menu_bar.addAction(suggest_action)
        menu_bar.addAction(report_action)

        title_label = QLabel("WinStore", self)
        title_label.setFont(QFont('SansSerif', 10))
        title_label.setGeometry(20, 30, 90, 30)
        title_label.setFont(QFont('SansSerif', 15))

        search_bar = QLineEdit(self)
        search_bar.setGeometry(110, 30, 800, 30)
        search_button = QPushButton(self)
        search_button.setGeometry(910, 29, 50, 32)
        search_button.setIcon(QIcon('./images/search_icon.png'))

        vbox = QVBoxLayout()
        container = QWidget()

        # Gets the list of apps from the database
        app_list = self.databse.get_all_apps()

        # Lists all apps of the database
        for i in app_list:
            widget = list_entry_widget.ListItem()
            widget.set_id(str(i[0]))
            widget.set_name(i[1])
            widget.set_description(i[3])
            vbox.addWidget(widget)

        container.setLayout(vbox)

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(20, 70, 960, 520)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidgetResizable(False)
        scroll_area.setWidget(container)


# Starts the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    landing_page = LandingPage()
    landing_page.show()
    sys.exit(app.exec_())
