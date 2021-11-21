from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import expanded_list_dialog


def checkout_clicked(app_id):
    expanded_item = expanded_list_dialog.ExpandedItem()
    expanded_item.get_results(int(app_id))
    expanded_item.exec_()


class ListItem(QWidget):

    def __init__(self, parent=None):
        super(ListItem, self).__init__(parent)
        self.setFixedSize(920, 100)

        self.app_id = QLabel(self)
        self.app_id.setVisible(False)

        frame = QFrame(self)
        frame.setGeometry(0, 0, 920, 100)
        frame.setStyleSheet("border: 1px solid grey;")

        self.name_label = QLabel("Example", self)
        self.name_label.setGeometry(10, 10, 700, 30)
        self.name_label.setFont(QFont('SansSerif', 12))

        self.descriptor_label = QLabel("Description", self)
        self.descriptor_label.setGeometry(10, 50, 810, 30)
        self.descriptor_label.setFont(QFont('SansSerif', 10))
        self.descriptor_label.setWordWrap(True)

        checkout_button = QPushButton("Check out", self)
        checkout_button.setGeometry(820, 25, 90, 50)
        checkout_button.setFont(QFont('SansSerif', 12))
        checkout_button.clicked.connect(lambda: checkout_clicked(self.app_id.text()))

    def set_name(self, name):
        self.name_label.setText(name)

    def set_description(self, desc):
        self.descriptor_label.setText(desc)

    def set_id(self, app_id):
        self.app_id.setText(app_id)
