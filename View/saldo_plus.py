# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saldo_plus.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 250)
        Form.setMinimumSize(QtCore.QSize(350, 250))
        Form.setMaximumSize(QtCore.QSize(350, 250))
        Form.setStyleSheet("border-radius:4px;")
        self.widget_agregar_saldo = QtWidgets.QWidget(Form)
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
        self.widget_saldo_mas = QtWidgets.QWidget(self.widget_agregar_saldo)
        self.widget_saldo_mas.setGeometry(QtCore.QRect(10, 10, 330, 230))
        self.widget_saldo_mas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        self.widget_saldo_mas.setObjectName("widget_saldo_mas")
        self.campo_ingreso_saldo = QtWidgets.QLineEdit(self.widget_saldo_mas)
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
        self.label = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label.setGeometry(QtCore.QRect(0, 40, 331, 30))
        self.label.setStyleSheet("font: 25 16pt \"Roboto Thin\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.checkBox_sueldo = QtWidgets.QCheckBox(self.widget_saldo_mas)
        self.checkBox_sueldo.setGeometry(QtCore.QRect(140, 160, 70, 17))
        self.checkBox_sueldo.setStyleSheet("font: 25 10pt \"Roboto Thin\";")
        self.checkBox_sueldo.setObjectName("checkBox_sueldo")
        self.label_ingreso_incorrecto_saldo = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_ingreso_incorrecto_saldo.setGeometry(QtCore.QRect(0, 130, 331, 20))
        self.label_ingreso_incorrecto_saldo.setStyleSheet("font: 25 10pt \"Roboto Light\";\n"
"color:  rgb(255, 103, 104);")
        self.label_ingreso_incorrecto_saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ingreso_incorrecto_saldo.setObjectName("label_ingreso_incorrecto_saldo")
        self.widget.raise_()
        self.widget_saldo_mas.raise_()
        self.pushButton_aceptar_ingreso_saldo.raise_()
        self.pushButton_cancelar_ingreso_saldo.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ingreso de saldo"))
        self.pushButton_aceptar_ingreso_saldo.setText(_translate("Form", "Aceptar"))
        self.pushButton_cancelar_ingreso_saldo.setText(_translate("Form", "Cancelar"))
        self.campo_ingreso_saldo.setPlaceholderText(_translate("Form", "$00000.00"))
        self.label.setText(_translate("Form", "Ingresá un monto"))
        self.checkBox_sueldo.setText(_translate("Form", "Sueldo"))
        self.label_ingreso_incorrecto_saldo.setText(_translate("Form", "* Ingresá un monto válido!"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
