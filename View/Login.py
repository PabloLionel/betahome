# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        MainWindow.setMaximumSize(QtCore.QSize(801, 601))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_frame = QtWidgets.QFrame(self.centralwidget)
        self.login_frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.login_frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.465, y1:0.397727, x2:0.863, y2:0.898, stop:0 rgba(34, 39, 45, 255), stop:1 rgba(75, 72, 51, 255));")
        self.login_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setLineWidth(1)
        self.login_frame.setMidLineWidth(0)
        self.login_frame.setObjectName("login_frame")
        self.label = QtWidgets.QLabel(self.login_frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 15))
        self.label.setMaximumSize(QtCore.QSize(100, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStatusTip("")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background: transparent;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/bbeta1.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login_frame)
        self.label_2.setGeometry(QtCore.QRect(250, -30, 983, 982))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Label_bienvenida = QtWidgets.QLabel(self.login_frame)
        self.Label_bienvenida.setGeometry(QtCore.QRect(140, 220, 520, 56))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Label_bienvenida.setFont(font)
        self.Label_bienvenida.setAutoFillBackground(False)
        self.Label_bienvenida.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 38pt \"Roboto Black\";\n"
"\n"
"\n"
"")
        self.Label_bienvenida.setScaledContents(False)
        self.Label_bienvenida.setObjectName("Label_bienvenida")
        self.pass_in = QtWidgets.QLineEdit(self.login_frame)
        self.pass_in.setGeometry(QtCore.QRect(262, 320, 261, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_in.sizePolicy().hasHeightForWidth())
        self.pass_in.setSizePolicy(sizePolicy)
        self.pass_in.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(2, 31, 84);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.pass_in.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.pass_in.setInputMask("")
        self.pass_in.setMaxLength(20)
        self.pass_in.setFrame(True)
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_in.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_in.setObjectName("pass_in")
        self.btn_ingreso_login = QtWidgets.QPushButton(self.login_frame)
        self.btn_ingreso_login.setGeometry(QtCore.QRect(350, 390, 90, 25))
        self.btn_ingreso_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ingreso_login.setStyleSheet("font: 12pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.397727, x2:0.863, y2:0.898, stop:0 rgba(107, 144, 153), stop:1 rgba(29, 104, 110));")
        self.btn_ingreso_login.setObjectName("btn_ingreso_login")
        self.user_in = QtWidgets.QLineEdit(self.login_frame)
        self.user_in.setGeometry(QtCore.QRect(262, 270, 261, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_in.sizePolicy().hasHeightForWidth())
        self.user_in.setSizePolicy(sizePolicy)
        self.user_in.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(2, 31, 84);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.user_in.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_in.setInputMask("")
        self.user_in.setMaxLength(20)
        self.user_in.setFrame(True)
        self.user_in.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.user_in.setAlignment(QtCore.Qt.AlignCenter)
        self.user_in.setObjectName("user_in")
        self.label_2.raise_()
        self.user_in.raise_()
        self.label.raise_()
        self.Label_bienvenida.raise_()
        self.pass_in.raise_()
        self.btn_ingreso_login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingreso"))
        self.Label_bienvenida.setText(_translate("MainWindow", "Bienvenido \"Usuario\"!"))
        self.pass_in.setPlaceholderText(_translate("MainWindow", "Ingresa tu contraseña"))
        self.btn_ingreso_login.setText(_translate("MainWindow", "Ingresar"))
        self.user_in.setPlaceholderText(_translate("MainWindow", "Ingresa tu Nombre"))


import Img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
