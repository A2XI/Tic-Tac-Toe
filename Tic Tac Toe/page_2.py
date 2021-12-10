from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class Page2(QWidget):
    def __init__(self, page1):
        super().__init__()
        self.page1 = page1
        self.initUi()
        self.show_x_score()
        self.show_zero_score()

    def initUi(self):
        self.button1 = self.add_button(175, 125)
        self.button2 = self.add_button(325, 125)
        self.button3 = self.add_button(475, 125)
        self.button4 = self.add_button(175, 275)
        self.button5 = self.add_button(325, 275)
        self.button6 = self.add_button(475, 275)
        self.button7 = self.add_button(175, 425)
        self.button8 = self.add_button(325, 425)
        self.button9 = self.add_button(475, 425)

        self.reset_button = QPushButton(self)
        self.reset_button.setGeometry(275, 25, 250, 85)
        self.reset_button.setStyleSheet("background: transparent;"
                                        f"font-family: Orbitron;"
                                        "font-size: 40px;"
                                        f"color: white;"
                                        f"border: 10px solid #5E054D;"
                                        "border-radius: 42px;}"
                                        "*:hover{"
                                        f"background: #5E054D;"
                                        "}")
        self.reset_button.setText("RESET")
        self.reset_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def add_button(self, x, y):
        button = QPushButton(self)
        button.setGeometry(x, y, 150, 150)
        button.setStyleSheet(self.buttonsStyle("none"))  # the color is set in main - setWinner, different for X and 0
        button.setText(' ')

        return button

    def empty_text_button(self):
        self.button1.setText(' ')
        self.button2.setText(' ')
        self.button3.setText(' ')
        self.button4.setText(' ')
        self.button5.setText(' ')
        self.button6.setText(' ')
        self.button7.setText(' ')
        self.button8.setText(' ')
        self.button9.setText(' ')

    def click_play_again(self):
        self.page1.main.x_turn = True
        self.page1.main.stop_game = False
        self.page1.main.full_squares = 0
        self.page1.main.x = 0
        self.page1.main.zero = 0
        self.page1.main.draw = 0
        self.empty_text_button()
        self.score_x.setText(f"{self.page1.main.x}")
        self.score_zero.setText(f"{self.page1.main.zero}")

    def show_x_score(self):
        self.text_x = QLabel(self)
        self.text_x.setGeometry(0, 250, 175, 100)
        self.text_x.setText('X`s score: ')
        self.text_x.setAlignment((QtCore.Qt.AlignCenter))
        self.text_x.setStyleSheet(f"color: {self.page1.main.text_color};"
                                  "font-size: 30px;"
                                  f"font-family: Tempus Sans ITC;"
                                  "font-weight: bold;")

        self.score_x = QLabel(self)
        self.score_x.setGeometry(25, 335, 125, 85)
        self.score_x.setText(f"{self.page1.main.x}")
        self.score_x.setAlignment(QtCore.Qt.AlignCenter)
        self.score_x.setStyleSheet(f"background: {self.page1.main.squares_hover_color};"
                                   f"color: {self.page1.main.x_color};"
                                   "font-size: 70px;"
                                   f"font-family: Tempus Sans ITC;"
                                   "font-weight: bold;")

        self.top_line_x = QLabel(self)
        self.top_line_x.setGeometry(20, 325, 135, 5)
        self.top_line_x.setStyleSheet(f"background: {self.page1.main.squares_color}")

        self.bottom_line_x = QLabel(self)
        self.bottom_line_x.setGeometry(20, 425, 135, 5)
        self.bottom_line_x.setStyleSheet(f"background: {self.page1.main.squares_color}")

    def show_zero_score(self):
        self.text_zero = QLabel(self)
        self.text_zero.setGeometry(625, 250, 175, 100)
        self.text_zero.setText('0`s score:')
        self.text_zero.setAlignment(QtCore.Qt.AlignCenter)
        self.text_zero.setStyleSheet("font-size: 30px;"
                                     f"font-family: Tempus Sans ITC;"
                                     "font-weight: bold;"
                                     f"color: {self.page1.main.text_color};")

        self.score_zero = QLabel(self)
        self.score_zero.setGeometry(650, 335, 125, 85)
        self.score_zero.setText(f"{self.page1.main.zero}")
        self.score_zero.setAlignment(QtCore.Qt.AlignCenter)
        self.score_zero.setStyleSheet(f"background: {self.page1.main.squares_hover_color};"
                                      f"color: {self.page1.main.zero_color};"
                                      "font-size: 70px;"
                                      f"font-family: Tempus Sans ITC;"
                                      "font-weight: bold;")

        self.top_line_zero = QLabel(self)
        self.top_line_zero.setGeometry(645, 325, 135, 5)
        self.top_line_zero.setStyleSheet(f"background: {self.page1.main.squares_color}")

        self.bottom_line_zero = QLabel(self)
        self.bottom_line_zero.setGeometry(645, 425, 135, 5)
        self.bottom_line_zero.setStyleSheet(f"background: {self.page1.main.squares_color}")

    def buttonsStyle(self, color):
        return (f"color: {color};"
                f"background: {self.page1.main.squares_color};"
                "font-size: 100px;"
                f"font-family: Tempus Sans ITC;"
                "font-weight: bold;"
                "animation: background;}"
                "*:hover{"
                f"background: {self.page1.main.squares_hover_color}"
                ";}")
