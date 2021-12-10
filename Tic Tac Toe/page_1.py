from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor


class Page1(QWidget):
    x_turn2 = True

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.initUi()

    def initUi(self):
        self.button = QPushButton(self)
        self.button.setGeometry(275, 460, 250, 100)
        self.button.setText("PLAY")
        self.button.setStyleSheet("background: transparent;"
                                  f"font-family: Orbitron;"
                                  "font-size: 40px;"
                                  f"color: white;"
                                  f"border: 10px solid #5E054D;"
                                  "border-radius: 50px;}"
                                  "*:hover{"
                                  f"background: #5E054D"
                                  ";}")
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.icon = QLabel(self)
        self.icon.setGeometry(275, 170, 250, 250)
        self.icon.setScaledContents(True)
        self.icon.setPixmap(QPixmap("img/icon.png"))

        self.welcome_text = QLabel(self)
        self.welcome_text.setGeometry(150, 60, 500, 100)
        self.welcome_text.setText("Welcome to")
        self.welcome_text.setStyleSheet("background: transparent;"
                                        f"font-family: Tempus Sans ITC;"
                                        "font-size: 80px;"
                                        "font-weight: bold;"
                                        f"color: {self.main.text_color}")
        self.welcome_text.setAlignment(QtCore.Qt.AlignCenter)

        self.label_x = QLabel(self)
        self.label_x.setGeometry(-68, 230, 200, 300)
        self.label_x.setText("x")
        self.label_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x.setStyleSheet("background: transparent;"
                                   "font-size: 350px;"
                                   f"color: {self.main.x_color};"
                                   "font-weight: bold;"
                                   f"font-family: Tempus Sans ITC")

        self.label_zero = QLabel(self)
        self.label_zero.setGeometry(668, 250, 200, 300)
        self.label_zero.setText("0")
        self.label_zero.setAlignment(QtCore.Qt.AlignCenter)
        self.label_zero.setStyleSheet("background: transparent;"
                                      "font-size: 260px;"
                                      f"color: {self.main.zero_color};"
                                      "font-weight: bold;"
                                      f"font-family: Tempus Sans ITC")
