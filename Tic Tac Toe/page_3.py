from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore


class Page3(QWidget):
    def __init__(self, page2):
        super().__init__()
        self.page2 = page2
        self.initUi()

    def initUi(self):
        self.label1 = QLabel(self)
        self.label1.setGeometry(160, 50, 70, 100)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.label2 = QLabel(self)
        self.label2.setGeometry(230, 50, 410, 100)
        self.label2.setStyleSheet("background: transparent;"
                                  f"color: {self.page2.page1.main.text_color};"
                                  "font-size: 50px;"
                                  "font-family: Tempus Sans ITC;"
                                  "font-weight: bold")

        self.icon = QLabel(self)
        self.icon.setGeometry(450, 175, 250, 250)
        self.icon.setPixmap(QPixmap("img/icon.png"))
        self.icon.setScaledContents(True)

        self.score = QLabel(self)
        self.score.setGeometry(100, 200, 300, 200)
        self.score.setStyleSheet("background: transparent;"
                                 f"color: {self.page2.page1.main.text_color};"
                                 "font-size: 50px;"
                                 f"font-family: Tempus Sans ITC;"
                                 "font-weight: bold")

        self.button_play_again = QPushButton(self)
        self.button_play_again.setGeometry(225, 450, 350, 100)
        self.button_play_again.setText("PLAY AGAIN")
        self.button_play_again.setStyleSheet("background: transparent;"
                                             f"font-family: Orbitron;"
                                             "font-size: 40px;"
                                             f"color: white;"
                                             f"border: 10px solid #5E054D;"
                                             "border-radius: 50px;}"
                                             "*:hover{"
                                             f"background: #5E054D"
                                             ";}")
        self.button_play_again.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
