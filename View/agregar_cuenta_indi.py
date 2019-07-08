# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar_cuenta_indi.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_agregar_cuenta(object):
    def setupUi(self, agregar_cuenta):
        agregar_cuenta.setObjectName("agregar_cuenta")
        agregar_cuenta.resize(350, 300)
        agregar_cuenta.setMaximumSize(QtCore.QSize(350, 300))
        self.frame = QtWidgets.QFrame(agregar_cuenta)
        self.frame.setGeometry(QtCore.QRect(0, 0, 350, 300))
        self.frame.setMaximumSize(QtCore.QSize(350, 300))
        self.frame.setStyleSheet("background-color: #17223b;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget_saldo_mas = QtWidgets.QWidget(self.frame)
        self.widget_saldo_mas.setGeometry(QtCore.QRect(10, 10, 330, 280))
        self.widget_saldo_mas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        self.widget_saldo_mas.setObjectName("widget_saldo_mas")
        self.label = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label.setGeometry(QtCore.QRect(0, 10, 331, 30))
        self.label.setStyleSheet("font: 25 16pt \"Roboto Thin\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox_categoria_ingreso = QtWidgets.QComboBox(self.widget_saldo_mas)
        self.comboBox_categoria_ingreso.setGeometry(QtCore.QRect(120, 70, 190, 25))
        self.comboBox_categoria_ingreso.setStyleSheet("font: 10pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color:#6b778d;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.comboBox_categoria_ingreso.setObjectName("comboBox_categoria_ingreso")
        self.label_2 = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 90, 25))
        self.label_2.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 90, 25))
        self.label_3.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 90, 25))
        self.label_4.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.lineEdit_Nombre_cuenta_ingreso = QtWidgets.QLineEdit(self.widget_saldo_mas)
        self.lineEdit_Nombre_cuenta_ingreso.setGeometry(QtCore.QRect(120, 110, 190, 25))
        self.lineEdit_Nombre_cuenta_ingreso.setStyleSheet("font: 10pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color:#6b778d;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.lineEdit_Nombre_cuenta_ingreso.setObjectName("lineEdit_Nombre_cuenta_ingreso")
        self.lineEdit_monto_cuenta_ingreso = QtWidgets.QLineEdit(self.widget_saldo_mas)
        self.lineEdit_monto_cuenta_ingreso.setGeometry(QtCore.QRect(120, 150, 190, 25))
        self.lineEdit_monto_cuenta_ingreso.setStyleSheet("font: 10pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color:#6b778d;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.lineEdit_monto_cuenta_ingreso.setObjectName("lineEdit_monto_cuenta_ingreso")
        self.label_5 = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 90, 25))
        self.label_5.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.checkBox_cuota_si_no = QtWidgets.QCheckBox(self.widget_saldo_mas)
        self.checkBox_cuota_si_no.setGeometry(QtCore.QRect(130, 190, 31, 25))
        self.checkBox_cuota_si_no.setStyleSheet("")
        self.checkBox_cuota_si_no.setText("")
        self.checkBox_cuota_si_no.setObjectName("checkBox_cuota_si_no")
        self.label_6 = QtWidgets.QLabel(self.widget_saldo_mas)
        self.label_6.setGeometry(QtCore.QRect(150, 190, 111, 25))
        self.label_6.setStyleSheet("font: 12pt \"Roboto Light\";\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_cant_cuotas = QtWidgets.QComboBox(self.widget_saldo_mas)
        self.comboBox_cant_cuotas.setEnabled(False)
        self.comboBox_cant_cuotas.setGeometry(QtCore.QRect(260, 190, 51, 25))
        self.comboBox_cant_cuotas.setStyleSheet("font: 10pt \"Roboto Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color:#6b778d;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 6px;")
        self.comboBox_cant_cuotas.setObjectName("comboBox_cant_cuotas")
        self.pushButton_list_ingreso_cuenta = QtWidgets.QPushButton(self.widget_saldo_mas)
        self.pushButton_list_ingreso_cuenta.setGeometry(QtCore.QRect(230, 240, 81, 25))
        self.pushButton_list_ingreso_cuenta.setStyleSheet("background-color: #6b778d;\n"
"border-radius: 6px;\n"
"font: 87 8pt \"Roboto Black\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_list_ingreso_cuenta.setObjectName("pushButton_list_ingreso_cuenta")

        self.retranslateUi(agregar_cuenta)
        self.checkBox_cuota_si_no.clicked['bool'].connect(self.comboBox_cant_cuotas.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(agregar_cuenta)

    def retranslateUi(self, agregar_cuenta):
        _translate = QtCore.QCoreApplication.translate
        agregar_cuenta.setWindowTitle(_translate("agregar_cuenta", "Dialog"))
        self.label.setText(_translate("agregar_cuenta", "Ingresá una nueva cuenta"))
        self.label_2.setText(_translate("agregar_cuenta", "Categoría:"))
        self.label_3.setText(_translate("agregar_cuenta", "Nombre:"))
        self.label_4.setText(_translate("agregar_cuenta", "Monto:"))
        self.lineEdit_monto_cuenta_ingreso.setPlaceholderText(_translate("agregar_cuenta", "$00000.00"))
        self.label_5.setText(_translate("agregar_cuenta", "Cuotas:"))
        self.label_6.setText(_translate("agregar_cuenta", "Cantidad:"))
        self.pushButton_list_ingreso_cuenta.setText(_translate("agregar_cuenta", "Listo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agregar_cuenta = QtWidgets.QDialog()
    ui = Ui_agregar_cuenta()
    ui.setupUi(agregar_cuenta)
    agregar_cuenta.show()
    sys.exit(app.exec_())
