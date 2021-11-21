import webbrowser
import database_controller
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import issue_report
import list_entry_widget
import suggestion_window
import error_message


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
    database = database_controller.Database()

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

        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(110, 30, 800, 30)
        self.search_button = QPushButton(self)
        self.search_button.setGeometry(910, 29, 50, 32)
        self.search_button.setIcon(QIcon('./images/search_icon.png'))
        self.search_button.clicked.connect(lambda: self.searching(self.search_bar.text()))

        self.vbox = QVBoxLayout()
        container = QWidget()

        if not self.database.connect():
            errorbox = error_message.ErrorMessage()
            errorbox.seterror("Couldn't connect to the internet", "Connection failed")
            errorbox.exec_()
            sys.exit()

        self.list_all()
        container.setLayout(self.vbox)

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(20, 70, 960, 520)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidgetResizable(False)
        scroll_area.setWidget(container)

    def list_all(self):
        # Gets the list of apps from the database
        app_list = self.database.get_all_apps()

        # Lists all apps of the database
        for i in app_list:
            widget = list_entry_widget.ListItem()
            widget.set_id(str(i[0]))
            widget.set_name(i[1])
            widget.set_description(i[3])
            self.vbox.addWidget(widget, alignment=Qt.AlignmentFlag.AlignTop)

    def searching(self, term):
        appl = self.database.search_app(term)

        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().setParent(None)

        if not appl:
            self.list_all()
        else:
            widget = list_entry_widget.ListItem()
            widget.set_id(str(appl[0]))
            widget.set_name(appl[1])
            widget.set_description(appl[3])
            self.vbox.addWidget(widget, alignment=Qt.AlignmentFlag.AlignTop)

        print("Searched: "+term)


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    landing_page = LandingPage()
    landing_page.show()
    exit_code = appctxt.app.exec()  # 2. Invoke appctxt.app.exec()
    landing_page.database.disconnect()
    sys.exit(exit_code)
