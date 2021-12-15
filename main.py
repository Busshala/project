"""libraries that we need"""

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from currency_converter import CurrencyConverter

import sqlite3

"""my database"""

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()

"""registration window"""


class Ui_RegWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 430)
        MainWindow.setStyleSheet("background-color: #524b4b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 280, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #7d7a7a;\n"
                                      "    border: 2px solid #fc8383;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #fc8383;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #ff4545;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: white;\n"
                                    "color: black;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: white;\n"
                                      "color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 280, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #7d7a7a;\n"
                                        "    border: 2px solid #fc8383;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #fc8383;\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #ff4545;\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 362, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #7d7a7a;\n"
                                        "    border: 2px solid #fc8383;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #fc8383;\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #ff4545;\n"
                                        "    color: black;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Regist"))
        self.label.setText(_translate("MainWindow", "label"))
        self.label_2.setText(_translate("MainWindow", "Registration"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "lineEdit"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "lineEdit_2"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.pushButton_3.setText(_translate("MainWindow", "Admin"))


"""Function what where how my Registration window works"""


class Registration(QtWidgets.QMainWindow, Ui_RegWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Registration')
        self.lineEdit.setPlaceholderText('Login')
        self.lineEdit_2.setPlaceholderText('Password')
        self.pushButton.setText('Registration')
        self.pushButton_2.setText('Login')
        self.setWindowTitle('Reg')
        self.ex = Ui_RegWindow()
        self.pushButton.pressed.connect(self.reg)
        self.pushButton_2.pressed.connect(self.login)
        self.pushButton_3.pressed.connect(self.admin)

    def login(self):
        self.login = Login()
        self.login.show()
        self.hide()

    def reg(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
            self.label.setText(f'Lessss goooo, {user_login}')
            db.commit()
            self.window = Function()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(Function())
            self.window.show()
            self.hide()
        else:
            self.label.setText('Nope! You have an account')

    def admin(self):
        self.window = RegAdm()
        self.ui = Ui_RegAdmWindow()
        self.ui.setupUi(RegAdm())
        self.window.show()
        self.hide()


"""Window for registration for admin"""


class Ui_RegAdmWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 470)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 80, 221, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: 2 px solid rgb(128. 0. 255);\n"
                                    "border-radius: 20px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 160, 221, 61))
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 2 px solid rgb(128. 0. 255);\n"
                                      "border-radius: 20px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 255);\n"
                                      "border: 2px solid;\n"
                                      "border-radius: 30px")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 12, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(170, 0, 255);\n"
                                 "border: 2px solid;\n"
                                 "border-radius: 10px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 350, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 255);\n"
                                        "border: 2px solid;\n"
                                        "border-radius: 30px")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "Admin"))
        self.pushButton_2.setText(_translate("MainWindow", "Return"))


"""Admin can only delete users. Pretty simple, is not it?"""


class RegAdm(QMainWindow, Ui_RegAdmWindow):
    def __init__(self):
        super(RegAdm, self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Login')
        self.lineEdit_2.setPlaceholderText('Password')
        self.pushButton.clicked.connect(self.admin)
        self.pushButton_2.clicked.connect(self.returning)

    def admin(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        if user_login == "Bushala" and user_password == "YandexLyceum":
            self.window = ForAdmin()
            self.ui = Ui_AdminWindow()
            self.ui.setupUi(ForAdmin())
            self.window.show()
            self.hide()
        else:
            return

    def returning(self):
        self.window = Registration()
        self.ui = Ui_RegWindow()
        self.ui.setupUi(Registration())
        self.window.show()
        self.hide()


"""Window for style Admin"""


class Ui_AdminWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 22, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(33, 47, 255);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 162, 611, 331))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "admin"))
        self.pushButton.setText(_translate("MainWindow", "delete people from database"))


"""Admin can only delete users. Pretty simple, is not it?"""


class ForAdmin(QMainWindow, Ui_AdminWindow):
    def __init__(self):
        super(ForAdmin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.delete)

    def delete(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''DELETE from users 
            ''')
        db.commit()

        self.window = Registration()
        self.ui = Ui_RegWindow()
        self.ui.setupUi(Registration())
        self.window.show()
        self.hide()


"""Window for people who already have an acc"""


class Login(QtWidgets.QMainWindow, Ui_RegWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Login')
        self.lineEdit.setPlaceholderText('Login')
        self.lineEdit_2.setPlaceholderText('Password')
        self.pushButton.setText('Login')
        self.pushButton_2.setText('Registration')
        self.setWindowTitle('Log')

        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)
        self.pushButton_3.pressed.connect(self.admin)

    def reg(self):
        self.reg = Registration()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            self.label.setText('You are in!')
            self.window = Function()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(Function())
            self.window.show()
            self.hide()
        else:
            self.label.setText('You cannot')

    def admin(self):
        self.window = RegAdm()
        self.ui = Ui_RegAdmWindow()
        self.ui.setupUi(RegAdm())
        self.window.show()
        self.hide()


"""what you wanted. converter. all what you need. only 50$ per hour."""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(245, 245, 220);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 191))
        self.frame.setStyleSheet("\n"
                                 "background-color: rgb(128, 0, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 221, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/pngwing.com.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 121, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/pngwing.com (1).png"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(180, 110, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit.setFont(font)
        self.exit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                "background-color: rgb(245, 245, 220);\n"
                                "border-radius: 20px solid;")
        self.exit.setObjectName("exit")
        self.input_our = QtWidgets.QLineEdit(self.centralwidget)
        self.input_our.setGeometry(QtCore.QRect(60, 230, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.input_our.setFont(font)
        self.input_our.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: black;\n"
                                     "border-radius: 20;\n"
                                     "border: 1px solid rgb(128, 0, 255);")
        self.input_our.setText("")
        self.input_our.setAlignment(QtCore.Qt.AlignCenter)
        self.input_our.setObjectName("input_our")
        self.input_not_our = QtWidgets.QLineEdit(self.centralwidget)
        self.input_not_our.setGeometry(QtCore.QRect(60, 300, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.input_not_our.setFont(font)
        self.input_not_our.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: black;\n"
                                         "border-radius: 20;\n"
                                         "border: 1px solid rgb(128, 0, 255);")
        self.input_not_our.setText("")
        self.input_not_our.setAlignment(QtCore.Qt.AlignCenter)
        self.input_not_our.setObjectName("input_not_our")
        self.out_our = QtWidgets.QLineEdit(self.centralwidget)
        self.out_our.setGeometry(QtCore.QRect(60, 370, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.out_our.setFont(font)
        self.out_our.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "color: black;\n"
                                   "border-radius: 20;\n"
                                   "border: 1px solid rgb(128, 0, 255);")
        self.out_our.setText("")
        self.out_our.setAlignment(QtCore.Qt.AlignCenter)
        self.out_our.setObjectName("out_our")
        self.outnot_our = QtWidgets.QLineEdit(self.centralwidget)
        self.outnot_our.setGeometry(QtCore.QRect(60, 440, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.outnot_our.setFont(font)
        self.outnot_our.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: black;\n"
                                      "border-radius: 20;\n"
                                      "border: 1px solid rgb(128, 0, 255);")
        self.outnot_our.setText("")
        self.outnot_our.setAlignment(QtCore.Qt.AlignCenter)
        self.outnot_our.setObjectName("outnot_our")
        self.zaconvertiruesh = QtWidgets.QPushButton(self.centralwidget)
        self.zaconvertiruesh.setGeometry(QtCore.QRect(100, 510, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.zaconvertiruesh.setFont(font)
        self.zaconvertiruesh.setStyleSheet("background-color: rgb(128, 0, 255);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border: 2px solid rgb(255, 255, 255);\n"
                                           "border-radius: 10px;")
        self.zaconvertiruesh.setObjectName("zaconvertiruesh")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 600, 201, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 255);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 2px solid rgb(255, 255, 255);\n"
                                      "border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Convertor 2.0"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.zaconvertiruesh.setText(_translate("MainWindow", "Законвертируешь????:)"))
        self.pushButton.setText(_translate("MainWindow", "Сколько у меня денег?"))


"""how converter works?"""


class Function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.input_our.setPlaceholderText("From currency")
        self.input_not_our.setPlaceholderText("I have")
        self.out_our.setPlaceholderText("To currency")
        self.outnot_our.setPlaceholderText("Total")
        self.zaconvertiruesh.clicked.connect(self.converting)
        self.exit.clicked.connect(self.exiting)
        self.pushButton.clicked.connect(self.calcul)

    def converting(self):
        if not bool(self.input_our.text()) or not bool(self.input_not_our.text()) \
                or not bool(self.out_our.text()):
            return
        c = CurrencyConverter()
        self.asd = self.input_our.text()
        self.zxc = int(self.input_not_our.text())
        self.qwe = self.out_our.text()
        outnot_our = round(c.convert(self.zxc, self.asd, self.qwe), 2)

        self.outnot_our.setText(str(outnot_our))

    def calcul(self):
        self.window = Calculation()
        self.ui = Ui_CalcWindow()
        self.setupUi(Calculation())
        self.window.show()

    def exiting(self):
        self.window = Registration()
        self.ui = Ui_RegWindow()
        self.setupUi(Registration())
        self.window.show()
        self.hide()


"""design of my calculator"""


class Ui_CalcWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(268, 398)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 3, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(20, 130, 51, 51))
        self.btn_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(85, 85, 85);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 130, 51, 51))
        self.btn_8.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(140, 190, 51, 51))
        self.btn_6.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 190, 51, 51))
        self.btn_5.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(140, 250, 51, 51))
        self.btn_3.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(20, 190, 51, 51))
        self.btn_4.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(140, 310, 51, 51))
        self.btn_dot.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                   "color: rgb(255, 255, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(20, 250, 51, 51))
        self.btn_1.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 250, 51, 51))
        self.btn_2.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(20, 310, 111, 51))
        self.btn_0.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_0.setObjectName("btn_0")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(140, 130, 51, 51))
        self.btn_9.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(200, 70, 51, 51))
        self.btn_divide.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(255, 170, 0);")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(200, 190, 51, 51))
        self.btn_minus.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(255, 170, 0);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(200, 250, 51, 51))
        self.btn_plus.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(255, 170, 0);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(200, 310, 51, 51))
        self.btn_equal.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(255, 170, 0);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(200, 130, 51, 51))
        self.btn_multiply.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(255, 170, 0);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_ce = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ce.setGeometry(QtCore.QRect(140, 70, 51, 51))
        self.btn_ce.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                  "color: rgb(255, 255, 255);")
        self.btn_ce.setObjectName("btn_ce")
        self.btn_plusminus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plusminus.setGeometry(QtCore.QRect(80, 70, 51, 51))
        self.btn_plusminus.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                         "color: rgb(255, 255, 255);")
        self.btn_plusminus.setObjectName("btn_plusminus")
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setGeometry(QtCore.QRect(20, 70, 51, 51))
        self.btn_c.setStyleSheet("background-color: rgb(85, 85, 85);\n"
                                 "color: rgb(255, 255, 255);")
        self.btn_c.setObjectName("btn_c")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 268, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулячка"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_ce.setText(_translate("MainWindow", "CE"))
        self.btn_plusminus.setText(_translate("MainWindow", "+-"))
        self.btn_c.setText(_translate("MainWindow", "C"))


"""lmao what can do calculator tell me pls"""


class Calculation(QMainWindow, Ui_CalcWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_8.clicked.connect(lambda: self.printing(self.btn_8.text()))
        self.btn_6.clicked.connect(lambda: self.printing(self.btn_6.text()))
        self.btn_5.clicked.connect(lambda: self.printing(self.btn_5.text()))
        self.btn_3.clicked.connect(lambda: self.printing(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.printing(self.btn_4.text()))
        self.btn_dot.clicked.connect(lambda: self.printing(self.btn_dot.text()))
        self.btn_1.clicked.connect(lambda: self.printing(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.printing(self.btn_2.text()))
        self.btn_0.clicked.connect(lambda: self.printing(self.btn_0.text()))
        self.btn_9.clicked.connect(lambda: self.printing(self.btn_9.text()))
        self.btn_7.clicked.connect(lambda: self.printing(self.btn_7.text()))
        self.btn_divide.clicked.connect(lambda: self.printing(self.btn_divide.text()))
        self.btn_minus.clicked.connect(lambda: self.printing(self.btn_minus.text()))
        self.btn_plus.clicked.connect(lambda: self.printing(self.btn_plus.text()))
        self.btn_equal.clicked.connect(self.res)
        self.btn_multiply.clicked.connect(lambda: self.printing(self.btn_multiply.text()))
        self.btn_ce.clicked.connect(self.tet)
        self.btn_plusminus.clicked.connect(self.pm)
        self.btn_c.clicked.connect(self.tet2)
        self.equality = False

    def printing(self, m):
        if self.label.text() == "0":
            self.label.setText(m)
        else:
            self.label.setText(self.label.text() + m)

    def tet(self):
        self.label.setText(self.label.text()[:-1])

    def tet2(self):
        self.label.setText("")

    def pm(self):
        if self.label.text() < str(0):
            self.label.setText(str(abs(int(self.label.text()))))
        else:
            self.label.setText(str(int(self.label.text()) * -1))

    def res(self):
        if self.equality:
            res = eval(self.label.text())
            self.label.setText(str(res))
            self.equality = True

        else:
            err = QMessageBox()
            err.setWindowTitle("Ошибочка!")
            err.setText("Вы что-то попутали")
            err.setIcon(QMessageBox.Warning)
            err.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)
            err.setDetailedText("Ну короче два раза нажали на равно, так не надо!")
            err.buttonClicked.connect(self.smh)
            err.exec_()
        """my program has even errors!!!"""

    def smh(self, btn):
        if btn.text() == "Reset":
            self.label.setText("")
            self.equality = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = QtWidgets.QApplication([])
    window = Registration()
    ex = Function()
    er = Calculation()
    window.show()
    sys.exit(app.exec_())
