from PyQt5 import QtCore, QtGui, QtWidgets
import sudokuUI
from sudokuUI import Ui_Main_Window as UI
from PyQt5.QtWidgets import QMessageBox
import webbrowser
import time

class Ui_MainWindow(object):

    def __init__(self):
        self.website = "https://github.com/Pratyush-exe"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(107, 31, 251, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(r"images\sudoku.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-20, -10, 521, 821))
        self.background.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.quesList = QtWidgets.QComboBox(self.centralwidget)
        self.quesList.setGeometry(QtCore.QRect(64, 156, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.quesList.setFont(font)
        self.quesList.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                    "color: rgb(79, 79, 79);\n"
                                    "padding-left:15px;\n"
                                    "selection-background-color: rgb(255, 242, 0);\n"
                                    "selection-color: black;\n"
                                    "")
        self.quesList.setFrame(False)
        self.quesList.setObjectName("quesList")

        for i in range(20):
            self.quesList.addItem("")

        self.begin_button = QtWidgets.QPushButton(self.centralwidget)
        self.begin_button.setGeometry(QtCore.QRect(61, 210, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.begin_button.setFont(font)
        self.begin_button.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                        "color: rgb(79, 79, 79);\n"
                                        "border-radius: 10px;")
        self.begin_button.setObjectName("begin_button")
        self.animation_speed = QtWidgets.QComboBox(self.centralwidget)
        self.animation_speed.setGeometry(QtCore.QRect(251, 156, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.animation_speed.setFont(font)
        self.animation_speed.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                           "color: rgb(79, 79, 79);\n"
                                           "padding-left:15px;\n"
                                           "selection-background-color: rgb(255, 242, 0);\n"
                                           "selection-color: black;")
        self.animation_speed.setFrame(False)
        self.animation_speed.setObjectName("animation_speed")

        for j in range(11):
            self.animation_speed.addItem("")

        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(60, 270, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.about_button.setFont(font)
        self.about_button.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                        "color: rgb(79, 79, 79);\n"
                                        "border-radius: 10px;")
        self.about_button.setObjectName("about_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(62, 216, 351, 41))
        self.label.setStyleSheet("background-color:rgb(251, 207, 0);\n"
                                 "color: rgb(79, 79, 79);\n"
                                 "border-radius: 10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 277, 351, 31))
        self.label_2.setStyleSheet("background-color:rgb(251, 207, 0);\n"
                                   "color: rgb(79, 79, 79);\n"
                                   "border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(64, 161, 161, 31))
        self.label_3.setStyleSheet("background-color:rgb(251, 207, 0);\n"
                                   "color: rgb(79, 79, 79);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(251, 161, 161, 31))
        self.label_4.setStyleSheet("background-color:rgb(251, 207, 0);\n"
                                   "color: rgb(79, 79, 79);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.background.raise_()
        self.logo.raise_()
        self.label.raise_()
        self.begin_button.raise_()
        self.label_2.raise_()
        self.about_button.raise_()
        self.label_3.raise_()
        self.quesList.raise_()
        self.label_4.raise_()
        self.animation_speed.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.begin_button.clicked.connect(self.begin)
        self.about_button.clicked.connect(lambda: webbrowser.open_new(self.website))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def begin(self):
        if self.quesList.currentText() == "QuestionList" or self.animation_speed.currentText() == "Speed (ms)":
            msg = QMessageBox()
            msg.setWindowTitle("sudoku")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("    You haven't selected a \"QuestionList\" or \"Speed (ms)\"")
            msg.exec_()

        else:
            self.Mainwindow = QtWidgets.QMainWindow()
            self.ui = UI(int(self.quesList.currentText().split("Q")[-1]) - 1, int(self.animation_speed.currentText()))
            self.ui.setupUi(self.Mainwindow)
            sudokuUI.history = []
            self.Mainwindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quesList.setCurrentText(_translate("MainWindow", "QuestionList"))
        self.quesList.setItemText(0, _translate("MainWindow", "QuestionList"))
        self.quesList.setItemText(1, _translate("MainWindow", "Q1"))
        self.quesList.setItemText(2, _translate("MainWindow", "Q2"))
        self.quesList.setItemText(3, _translate("MainWindow", "Q3"))
        self.quesList.setItemText(4, _translate("MainWindow", "Q4"))
        self.quesList.setItemText(5, _translate("MainWindow", "Q5"))
        self.quesList.setItemText(6, _translate("MainWindow", "Q6"))
        self.quesList.setItemText(7, _translate("MainWindow", "Q7"))
        self.quesList.setItemText(8, _translate("MainWindow", "Q8"))
        self.quesList.setItemText(9, _translate("MainWindow", "Q9"))
        self.quesList.setItemText(10, _translate("MainWindow", "Q10"))
        self.quesList.setItemText(11, _translate("MainWindow", "Q11"))
        self.quesList.setItemText(12, _translate("MainWindow", "Q12"))
        self.quesList.setItemText(13, _translate("MainWindow", "Q13"))
        self.quesList.setItemText(14, _translate("MainWindow", "Q14"))
        self.quesList.setItemText(15, _translate("MainWindow", "Q15"))
        self.quesList.setItemText(16, _translate("MainWindow", "Q16"))
        self.quesList.setItemText(17, _translate("MainWindow", "Q17"))
        self.quesList.setItemText(18, _translate("MainWindow", "Q18"))
        self.quesList.setItemText(19, _translate("MainWindow", "Q19"))
        self.quesList.setItemText(20, _translate("MainWindow", "Q20"))
        self.begin_button.setText(_translate("MainWindow", "Begin"))
        self.animation_speed.setCurrentText(_translate("MainWindow", "Speed (ms)"))
        self.animation_speed.setItemText(0, _translate("MainWindow", "Speed (ms)"))
        self.animation_speed.setItemText(1, _translate("MainWindow", "100"))
        self.animation_speed.setItemText(2, _translate("MainWindow", "200"))
        self.animation_speed.setItemText(3, _translate("MainWindow", "300"))
        self.animation_speed.setItemText(4, _translate("MainWindow", "400"))
        self.animation_speed.setItemText(5, _translate("MainWindow", "500"))
        self.animation_speed.setItemText(6, _translate("MainWindow", "600"))
        self.animation_speed.setItemText(7, _translate("MainWindow", "700"))
        self.animation_speed.setItemText(8, _translate("MainWindow", "800"))
        self.animation_speed.setItemText(9, _translate("MainWindow", "900"))
        self.animation_speed.setItemText(10, _translate("MainWindow", "1000"))
        self.about_button.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"images\icon.ico"))
    MainWindow.setWindowTitle("sudoku")
    MainWindow.show()
    sys.exit(app.exec_())
