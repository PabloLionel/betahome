# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Saldo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 250)
        self.widget_agregar_saldo = QtWidgets.QWidget(Dialog)
        self.widget_agregar_saldo.setGeometry(QtCore.QRect(0, 0, 350, 250))
        self.widget_agregar_saldo.setMaximumSize(QtCore.QSize(350, 250))
        self.widget_agregar_saldo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        self.widget_agregar_saldo.setObjectName("widget_agregar_saldo")
        self.pushButton_aceptar_ingreso_saldo = QtWidgets.QPushButton(self.widget_agregar_saldo)
        self.pushButton_aceptar_ingreso_saldo.setGeometry(QtCore.QRect(80, 200, 75, 25))
        self.pushButton_aceptar_ingreso_saldo.setStyleSheet("background-color: #6b778d;\n"
"border-radius: 6px;\n"
"font: 87 8pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_aceptar_ingreso_saldo.setObjectName("pushButton_aceptar_ingreso_saldo")
        self.pushButton_cancelar_ingreso_saldo = QtWidgets.QPushButton(self.widget_agregar_saldo)
        self.pushButton_cancelar_ingreso_saldo.setGeometry(QtCore.QRect(195, 200, 75, 25))
        self.pushButton_cancelar_ingreso_saldo.setStyleSheet("border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Roboto Black\";\n"
"color: #6b778d;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color:#6b778d;")
        self.pushButton_cancelar_ingreso_saldo.setObjectName("pushButton_cancelar_ingreso_saldo")
        self.widget = QtWidgets.QWidget(self.widget_agregar_saldo)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 251))
        self.widget.setStyleSheet("background-color: #17223b;")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget_agregar_saldo)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 330, 230))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        self.widget_2.setObjectName("widget_2")
        self.campo_ingreso_saldo = QtWidgets.QLineEdit(self.widget_2)
        self.campo_ingreso_saldo.setGeometry(QtCore.QRect(50, 100, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_ingreso_saldo.sizePolicy().hasHeightForWidth())
        self.campo_ingreso_saldo.setSizePolicy(sizePolicy)
        self.campo_ingreso_saldo.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color:#6b778d;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.campo_ingreso_saldo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.campo_ingreso_saldo.setInputMask("")
        self.campo_ingreso_saldo.setMaxLength(20)
        self.campo_ingreso_saldo.setFrame(True)
        self.campo_ingreso_saldo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.campo_ingreso_saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_ingreso_saldo.setObjectName("campo_ingreso_saldo")



        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 310, 30))
        self.label.setStyleSheet("font: 25 16pt \"Roboto Thin\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(130, 140, 70, 17))
        self.checkBox.setStyleSheet("font: 25 10pt \"Roboto Thin\";")
        self.checkBox.setObjectName("checkBox")
        self.widget.raise_()
        self.widget_2.raise_()
        self.pushButton_aceptar_ingreso_saldo.raise_()
        self.pushButton_cancelar_ingreso_saldo.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_aceptar_ingreso_saldo.setText(_translate("Dialog", "Aceptar"))
        self.pushButton_cancelar_ingreso_saldo.setText(_translate("Dialog", "Cancelar"))
        self.campo_ingreso_saldo.setPlaceholderText(_translate("Dialog", "$00000.00"))
        self.label.setText(_translate("Dialog", "Ingresá un monto"))
        self.checkBox.setText(_translate("Dialog", "Sueldo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
