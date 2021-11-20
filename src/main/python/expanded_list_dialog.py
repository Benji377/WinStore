import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import database_controller


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


class ExpandedItem(QDialog):
    def __init__(self, parent=None):
        super(ExpandedItem, self).__init__(parent)
        self.setFixedSize(500, 700)
        self.setWindowTitle("Example")
        self.setModal(True)
        self.setWindowIcon(QIcon('./images/icon.png'))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.banner_label = QLabel(self)
        self.banner_label.setGeometry(0, 0, 500, 100)

        self.title_label = QLabel(self)
        self.title_label.setGeometry(10, 120, 480, 30)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setOpenExternalLinks(True)

        descrip_label = QLabel("Description:", self)
        descrip_label.setGeometry(20, 160, 460, 30)
        descrip_label.setFont(QFont('SansSerif', 12))

        self.description_label = QLabel(self)
        self.description_label.setGeometry(20, 190, 460, 200)
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(Qt.AlignTop)
        self.description_label.setFont(QFont('SansSerif', 10))

        deta_label = QLabel("Details:", self)
        deta_label.setGeometry(20, 400, 460, 30)
        deta_label.setFont(QFont('SansSerif', 12))

        self.details_label = QLabel(self)
        self.details_label.setGeometry(20, 430, 460, 30)
        self.details_label.setWordWrap(True)
        self.details_label.setAlignment(Qt.AlignTop)
        self.details_label.setFont(QFont('SansSerif', 10))

        self.credits_label = QLabel(self)
        self.credits_label.setGeometry(20, 660, 460, 30)
        self.credits_label.setAlignment(Qt.AlignRight)
        self.credits_label.setFont(QFont('SansSerif', 10))

    def get_results(self, app_id):
        data = database_controller.Database()
        appl = data.get_app_by_id(app_id)

        write_file(appl[2], 'temp.jpg')
        pfile = QPixmap('temp.jpg')
        self.banner_label.setPixmap(pfile)
        os.remove('temp.jpg')

        url_link = "<a href=\"" + appl[4] + "\"> <font face=SansSerif size=12 color=black>" + appl[1] + "</font> </a>"
        self.title_label.setText(url_link)
        self.description_label.setText(appl[3])
        self.details_label.setText(appl[6])
        self.credits_label.setText(appl[5])
