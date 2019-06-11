# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 495)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 250, 171, 25))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblUsuario = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUsuario.setObjectName("lblUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblUsuario)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 280, 191, 25))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblContrasnia = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblContrasnia.setObjectName("lblContrasnia")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblContrasnia)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 310, 191, 54))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1071, 671))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.468, y1:0.006, x2:1, y2:1, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Fira Sans Compressed")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 254, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame.raise_()
        self.formLayoutWidget.raise_()
        self.formLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblUsuario.setText(_translate("Dialog", "Usuario: "))
        self.lblContrasnia.setText(_translate("Dialog", "Contraseña:"))
        self.pushButton.setText(_translate("Dialog", "Iniciar Sesión"))
        self.pushButton_2.setText(_translate("Dialog", "Registrar"))
        self.label.setText(_translate("Dialog", "LOGIN - BC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

