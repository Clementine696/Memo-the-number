"""
    Memo the Number!
Kanate Boonsiri     63090500404
Bavornthat Dangtang 63090500412
Katepiss Sriburapa  63090500419
Thitipong Thongkam  63090500424
"""

import sys
from random import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Creat HowToPlayScreen
class Widget2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.widget_layout2 = QGridLayout()
        self.setGeometry(0, 0, 0, 0)

        self.PlayGame = QPushButton('Play')
        self.PlayGame.setFixedSize(140, 40)

        def play_button_clicked():
            # Closing HowToPlay Screen
            widget.close()
            widget2.show()

        self.PlayGame.clicked.connect(play_button_clicked)

        pixmap = QPixmap('Data\HowToPlay.jpg')
        print('size = ', pixmap.size())
        width = pixmap.size().width()
        height = pixmap.size().height()

        self.HowtoPlayImage = QLabel()
        self.HowtoPlayImage.setPixmap(pixmap)
        self.HowtoPlayImage.setGeometry(0, 0, 0, 0)
        self.HowtoPlayImage.resize(width, height)
        self.widget_layout2.addWidget(self.HowtoPlayImage, 0, 0)
        self.widget_layout2.addWidget(self.PlayGame, 0, 1)
        self.setLayout(self.widget_layout2)

        self.setWindowTitle('Memo the Number!')  # Window name
        self.setWindowIcon(QIcon('Data\Dogge.jpg'))  # Icon used by the window.


class Widget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Set Color for Button
        Color_Defult = QPalette()
        Color_Red = QPalette()
        Color_Defult.setColor(QPalette.Button, QColor(255, 0, 0, 255))
        Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 0))

        self.setAutoFillBackground(True)
        self.widget_layout = QGridLayout()
        self.setGeometry(400, 200, 350, 200)

        # Creat Button
        self.Button1 = QPushButton()
        self.Button2 = QPushButton()
        self.Button3 = QPushButton()
        self.Button4 = QPushButton()
        self.Button5 = QPushButton()
        self.Button6 = QPushButton()
        self.Button7 = QPushButton()
        self.Button8 = QPushButton()
        self.Button9 = QPushButton()
        self.ButtonStart = QPushButton('Start')

        # Set Size for Button
        self.Button1.setFixedSize(50, 50)
        self.Button2.setFixedSize(50, 50)
        self.Button3.setFixedSize(50, 50)
        self.Button4.setFixedSize(50, 50)
        self.Button5.setFixedSize(50, 50)
        self.Button6.setFixedSize(50, 50)
        self.Button7.setFixedSize(50, 50)
        self.Button8.setFixedSize(50, 50)
        self.Button9.setFixedSize(50, 50)
        self.ButtonStart.setFixedSize(140, 40)

        # Set Color for Button
        self.Button1.setAutoFillBackground(True)
        self.Button2.setAutoFillBackground(True)
        self.Button3.setAutoFillBackground(True)
        self.Button4.setAutoFillBackground(True)
        self.Button5.setAutoFillBackground(True)
        self.Button6.setAutoFillBackground(True)
        self.Button7.setAutoFillBackground(True)
        self.Button8.setAutoFillBackground(True)
        self.Button9.setAutoFillBackground(True)
        self.ButtonStart.setAutoFillBackground(True)


        # Creat Label
        self.line_edit = QLabel()
        self.line_edit2 = QLabel()
        font = self.line_edit.font()
        font.setPointSize(16)
        self.line_edit.setFont(font)

        font2 = self.line_edit2.font()
        font2.setPointSize(16)
        self.line_edit2.setFont(font2)


        # When the buttons get clicked
        self.ButtonStart.clicked.connect(self.Start_clicked)
        self.Button1.clicked.connect(self.radio1_clicked)
        self.Button2.clicked.connect(self.radio2_clicked)
        self.Button3.clicked.connect(self.radio3_clicked)
        self.Button4.clicked.connect(self.radio4_clicked)
        self.Button5.clicked.connect(self.radio5_clicked)
        self.Button6.clicked.connect(self.radio6_clicked)
        self.Button7.clicked.connect(self.radio7_clicked)
        self.Button8.clicked.connect(self.radio8_clicked)
        self.Button9.clicked.connect(self.radio9_clicked)

        # Add Button to Widget
        self.widget_layout.addWidget(self.Button1, 0, 0)
        self.widget_layout.addWidget(self.Button2, 0, 1)
        self.widget_layout.addWidget(self.Button3, 0, 2)
        self.widget_layout.addWidget(self.Button4, 1, 0)
        self.widget_layout.addWidget(self.Button5, 1, 1)
        self.widget_layout.addWidget(self.Button6, 1, 2)
        self.widget_layout.addWidget(self.Button7, 2, 0)
        self.widget_layout.addWidget(self.Button8, 2, 1)
        self.widget_layout.addWidget(self.Button9, 2, 2)
        self.widget_layout.addWidget(self.ButtonStart, 4, 3)
        self.widget_layout.addWidget(self.line_edit, 5, 3)
        self.widget_layout.addWidget(self.line_edit2, 6, 3)
        self.setLayout(self.widget_layout)

        self.setWindowTitle('Memo the Number!')  # Window name
        self.setWindowIcon(QIcon('Data\Dogge.jpg'))  # Icon used by the window.

        self.TimeCount = 0
        self.Running = 0
        self.InputCount = 0
        self.InputCount2 = 0
        self.InputReady = 0
        self.InputListCheck = 0
        self.CheckWin = 0
        self.MaxScore = 0
        self.CurrentScore = 0
        self.GameOver = 0
        self.RandomNumber = 0
        self.InputClicked = 0
        self.Started = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.ListAns = []
        self.ListInput = []
        self.line_edit.setText("Max score = {0}".format(self.MaxScore))
        self.RandomNumber = randrange(1, 10)
        self.ListAns.append(self.RandomNumber)
        self.RandomNumber = randrange(1, 10)
        self.ListAns.append(self.RandomNumber)

    def Start_clicked(self):
        if self.Started == 1:
            if self.GameOver == 1:
                self.CurrentScore = 0
                self.GameOver = 0
            self.timer.start()
            self.Started = 0
            self.ButtonStart.setText("Wait..")
            self.TimeCount = 0
            self.Running = 1
            self.RandomNumber = randrange(1, 10)
            self.ListAns.append(self.RandomNumber)
        else:
            self.ButtonStart.setText("WAIT!")

    def radio1_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button1.setPalette(Color_Red)
                self.ListInput.append(1)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio2_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button2.setPalette(Color_Red)
                self.ListInput.append(2)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio3_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button3.setPalette(Color_Red)
                self.ListInput.append(3)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio4_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button4.setPalette(Color_Red)
                self.ListInput.append(4)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio5_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button5.setPalette(Color_Red)
                self.ListInput.append(5)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio6_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button6.setPalette(Color_Red)
                self.ListInput.append(6)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio7_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button7.setPalette(Color_Red)
                self.ListInput.append(7)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio8_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button8.setPalette(Color_Red)
                self.ListInput.append(8)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def radio9_clicked(self):
        if self.InputReady == 1:
            if self.InputClicked == 0:
                self.timer.start()
                self.TimeCount = 1.5
                self.InputClicked = 1
                Color_Red = QPalette()
                self.setAutoFillBackground(True)
                self.setPalette(Color_Red)
                Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
                self.Button9.setPalette(Color_Red)
                self.ListInput.append(9)
                self.InputCount += 1
                self.InputCount2 += 1
                self.line_edit2.setText('{0} / {1}'.format(self.InputCount2, len(self.ListAns)))

    def update_time(self):
        Color_Red = QPalette()
        Color_Default = QPalette()
        Color_Purple = QPalette()
        self.setAutoFillBackground(True)
        self.setPalette(Color_Red)
        self.setPalette(Color_Default)
        self.setPalette(Color_Purple)
        Color_Red.setColor(QPalette.Button, QColor(255, 0, 0, 255))
        Color_Default.setColor(QPalette.Button, QColor(255, 0, 0, 0))
        Color_Purple.setColor(QPalette.Button, QColor(65, 21, 186))

        if self.InputReady == 1:
            self.CheckWin = 1
            if len(self.ListAns) == len(self.ListInput):
                for i in range(len(self.ListAns)):
                    if self.ListAns[i] != self.ListInput[i]:
                        self.CheckWin = 0
                if self.CheckWin == 0:
                    self.ButtonStart.setText("Wrong, Try again?")
                    self.GameOver = 1
                    self.ListAns = []
                    self.RandomNumber = randrange(1, 10)
                    self.ListAns.append(self.RandomNumber)
                    self.RandomNumber = randrange(1, 10)
                    self.ListAns.append(self.RandomNumber)
                if self.CheckWin == 1:
                    self.ButtonStart.setText("Continue")
                    self.CurrentScore += 1
                self.Started = 1
                self.ButtonStart.setPalette(Color_Default)
                self.Running = 0
                self.InputCount = 0
                self.InputReady = 0
                self.InputListCheck = 0
                self.ListInput = []
                self.InputCount2 = 0
                self.line_edit2.setText("Your score = {0}".format(self.CurrentScore))
                if self.CurrentScore > self.MaxScore:
                    self.MaxScore = self.CurrentScore
                self.line_edit.setText("Max score = {0}".format(self.MaxScore))

        if self.Running == 1:
            self.Started = 0
            self.ButtonStart.setPalette(Color_Purple)
            self.line_edit.setText("Max score = {0}".format(self.MaxScore))
            self.line_edit2.setText("Remember!")
            if int(self.TimeCount) == len(self.ListAns):
                self.Running = 0
                self.Button1.setPalette(Color_Default)
                self.Button2.setPalette(Color_Default)
                self.Button3.setPalette(Color_Default)
                self.Button4.setPalette(Color_Default)
                self.Button5.setPalette(Color_Default)
                self.Button6.setPalette(Color_Default)
                self.Button7.setPalette(Color_Default)
                self.Button8.setPalette(Color_Default)
                self.Button9.setPalette(Color_Default)
                self.timer.stop()
                self.InputReady = 1
                self.line_edit2.setText('► Your turn!')

        if self.Running == 1:
            if (self.TimeCount * 10) % 2 == 0:
                self.InputListCheck = int(self.TimeCount)
                print(self.InputListCheck, self.ListAns[self.InputListCheck])
                if self.ListAns[self.InputListCheck] == 1:
                    self.Button1.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 2:
                    self.Button2.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 3:
                    self.Button3.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 4:
                    self.Button4.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 5:
                    self.Button5.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 6:
                    self.Button6.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 7:
                    self.Button7.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 8:
                    self.Button8.setPalette(Color_Red)
                elif self.ListAns[self.InputListCheck] == 9:
                    self.Button9.setPalette(Color_Red)
            else:
                self.Button1.setPalette(Color_Default)
                self.Button2.setPalette(Color_Default)
                self.Button3.setPalette(Color_Default)
                self.Button4.setPalette(Color_Default)
                self.Button5.setPalette(Color_Default)
                self.Button6.setPalette(Color_Default)
                self.Button7.setPalette(Color_Default)
                self.Button8.setPalette(Color_Default)
                self.Button9.setPalette(Color_Default)

        self.TimeCount += 0.5
        if self.TimeCount == 2.0:
            if self.InputClicked == 1:
                self.InputClicked = 0
                self.Button1.setPalette(Color_Default)
                self.Button2.setPalette(Color_Default)
                self.Button3.setPalette(Color_Default)
                self.Button4.setPalette(Color_Default)
                self.Button5.setPalette(Color_Default)
                self.Button6.setPalette(Color_Default)
                self.Button7.setPalette(Color_Default)
                self.Button8.setPalette(Color_Default)
                self.Button9.setPalette(Color_Default)
                self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Widget2()
    widget.show()
    widget2 = Widget()
    sys.exit(app.exec_())