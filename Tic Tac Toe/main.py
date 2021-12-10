"""
Trivial Tic-Tac-Toe Game
"""

import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5 import QtGui
from page_1 import Page1
from page_2 import Page2
from page_3 import Page3
from pop_up import PopUp


class MainWindow(QStackedWidget):
    def __init__(self, x_color, zero_color, text_color, squares_color, game_background):
        super().__init__()
        self.x_color = x_color
        self.zero_color = zero_color
        self.text_color = text_color
        self.squares_color = squares_color
        self.game_background = game_background
        self.squares_hover_color = self.set_hover_color()
        self.x = 0
        self.zero = 0
        self.draw = 0
        self.full_squares = 0
        self.stop_game = False
        self.x_turn = True

        self.initUi()

    def initUi(self):
        self.setFixedSize(800, 600)
        self.setWindowIcon(QtGui.QIcon("img/window_icon.png"))
        self.setWindowTitle("Tic-Tac-Toe")
        self.setStyleSheet(f"background: {self.game_background};")

        self.showPage1()
        self.showPage2()
        self.showPage3()

        self.initButtonsClick()

    def showPage1(self):
        self.page1 = Page1(self)
        self.addWidget(self.page1)
        self.setCurrentWidget(self.page1)

    def showPage2(self):
        self.page2 = Page2(self.page1)
        self.addWidget(self.page2)

    def showPage3(self):
        self.page3 = Page3(self.page2)
        self.addWidget(self.page3)

    def showPopUp(self, text, img):
        self.popup = PopUp(self.page3, text, img)

    def initButtonsClick(self):
        self.page2.button1.clicked.connect(lambda: self.squareClick(self.page2.button1))
        self.page2.button2.clicked.connect(lambda: self.squareClick(self.page2.button2))
        self.page2.button3.clicked.connect(lambda: self.squareClick(self.page2.button3))
        self.page2.button4.clicked.connect(lambda: self.squareClick(self.page2.button4))
        self.page2.button5.clicked.connect(lambda: self.squareClick(self.page2.button5))
        self.page2.button6.clicked.connect(lambda: self.squareClick(self.page2.button6))
        self.page2.button7.clicked.connect(lambda: self.squareClick(self.page2.button7))
        self.page2.button8.clicked.connect(lambda: self.squareClick(self.page2.button8))
        self.page2.button9.clicked.connect(lambda: self.squareClick(self.page2.button9))

        self.page1.button.clicked.connect(lambda: self.setCurrentWidget(self.page2))

        self.page2.reset_button.clicked.connect(self.page2.click_play_again)

        self.page3.button_play_again.clicked.connect(self.page2.click_play_again)
        self.page3.button_play_again.clicked.connect(lambda: self.setCurrentWidget(self.page2))

    def squareClick(self, button):
        if not self.stop_game:
            if self.x_turn and button.text() == ' ':
                button.setText('X')
                button.setStyleSheet(self.page2.buttonsStyle(self.x_color))
                self.x_turn = False
                self.full_squares += 1
            elif not self.x_turn and button.text() == ' ':
                button.setText('0')
                button.setStyleSheet(self.page2.buttonsStyle(self.zero_color))
                self.x_turn = True
                self.full_squares += 1
        self.gameLogic()

    def gameLogic(self):
        self.setWinner(self.page2.button1, self.page2.button2, self.page2.button3)
        self.setWinner(self.page2.button4, self.page2.button5, self.page2.button6)
        self.setWinner(self.page2.button7, self.page2.button8, self.page2.button9)

        self.setWinner(self.page2.button1, self.page2.button4, self.page2.button7)
        self.setWinner(self.page2.button2, self.page2.button5, self.page2.button8)
        self.setWinner(self.page2.button3, self.page2.button6, self.page2.button9)

        self.setWinner(self.page2.button1, self.page2.button5, self.page2.button9)
        self.setWinner(self.page2.button3, self.page2.button5, self.page2.button7)

        if self.full_squares == 9 and not self.stop_game:
            self.stop_game = True
            self.full_squares = 0
            self.draw += 1
            self.showPopUp("It`s a draw\t", "img/winner_draw.png")

    def setWinner(self, a, b, c):
        if not self.stop_game:
            if a.text() == 'X' and b.text() == 'X' and c.text() == 'X':
                self.stop_game = True
                self.x += 1
                self.page2.score_x.setText(f"{self.x}")
                self.showPopUp("X has won this round!", "img/winner_X.png")

            elif a.text() == '0' and b.text() == '0' and c.text() == '0':
                self.stop_game = True
                self.zero += 1
                self.page2.score_zero.setText(f"{self.zero}")
                self.showPopUp("0 has won this round!", "img/winner_0.png")

    def set_hover_color(self):
        dec = int(self.squares_color[1:], 16)
        enlighten = 921374  # add this number to int(squares_color) to lighten the hover color
        dec += enlighten
        color = hex(dec)
        return '#' + color[2:].upper()


if __name__ == "__main__":
    x_color = "#2B1DF6"     # how x will be colored on playboard
    zero_color = "#C32134"  # how zero will be colored on playboard
    text_color = "white"    # informative text of game
    squares_color = "#E7DC75"   # playboard background
    game_background = "#000000" # game background

    app = QApplication(sys.argv)
    window = MainWindow(x_color, zero_color, text_color, squares_color, game_background)
    window.show()
    sys.exit(app.exec_())
