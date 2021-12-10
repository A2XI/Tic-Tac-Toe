from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


class PopUp(QMessageBox):
    def __init__(self, page3, text, img):
        super().__init__()
        self.page3 = page3
        self.message = QMessageBox()
        self.message.setWindowTitle("Round ended")
        self.message.setStyleSheet(f"font-family: Tempus Sans ITC;"
                                   "font-size: 17px;")
        self.message.setIconPixmap(QtGui.QPixmap(img))
        self.message.setWindowIcon(QtGui.QIcon("img/window_icon.png"))
        self.message.setText(text)
        self.message.setInformativeText("Play again?")
        self.message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.message.buttonClicked.connect(self.clickPopup)

        self.message.exec_()

    def clickPopup(self, button):
        self.page3.page2.page1.main.x_turn = True

        if button.text() == "&Yes":
            self.page3.page2.empty_text_button()
            self.page3.page2.page1.main.full_squares = 0
            self.page3.page2.page1.main.stop_game = False

        elif button.text() == "&No":
            self.page3.page2.page1.main.setCurrentWidget(self.page3)
            self.page3.label2.setText("has won the game!")

            if self.page3.page2.page1.main.x > self.page3.page2.page1.main.zero:
                self.page3.label1.setText("X")
                self.page3.label1.setStyleSheet(f"color: {self.page3.page2.page1.main.x_color};"
                                                "background: transparent;"
                                                "font-size: 80px;"
                                                f"font-family: Tempus Sans ITC;"
                                                "font-weight: bold")
            elif self.page3.page2.page1.main.zero > self.page3.page2.page1.main.x:
                self.page3.label1.setText("0")
                self.page3.label1.setStyleSheet(f"color: {self.page3.page2.page1.main.zero_color};"
                                                "background: transparent;"
                                                "font-size: 80px;"
                                                f"font-family: Tempus Sans ITC;"
                                                "font-weight: bold")
            elif self.page3.page2.page1.main.x == self.page3.page2.page1.main.zero:
                self.page3.label1.setText(" ")
                self.page3.label2.setText("Draw!")

            self.page3.score.setText(f"X`s score:  {self.page3.page2.page1.main.x}\n"
                                     f"0`s score:  {self.page3.page2.page1.main.zero}\n"
                                     f"Draws:  {self.page3.page2.page1.main.draw}")
