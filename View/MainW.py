# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainW.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        self.frame_main_w = QtWidgets.QFrame(Form)
        self.frame_main_w.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame_main_w.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_main_w.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main_w.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_w.setObjectName("frame_main_w")
        self.menu_frame = QtWidgets.QFrame(self.frame_main_w)
        self.menu_frame.setGeometry(QtCore.QRect(0, -1, 200, 611))
        self.menu_frame.setStyleSheet("background-color: #17223b;")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.menu_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 201, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_Menu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_Menu.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_Menu.setContentsMargins(0, 0, 1, 150)
        self.verticalLayout_Menu.setSpacing(2)
        self.verticalLayout_Menu.setObjectName("verticalLayout_Menu")
        self.frame_Saldo = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_Saldo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        self.frame_Saldo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Saldo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Saldo.setObjectName("frame_Saldo")
        self.Label_Saldo = QtWidgets.QLabel(self.frame_Saldo)
        self.Label_Saldo.setGeometry(QtCore.QRect(5, 9, 140, 40))
        self.Label_Saldo.setStyleSheet("font: 87 10pt \"Roboto Black\";")
        self.Label_Saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Saldo.setObjectName("Label_Saldo")
        self.pushButton_agregar_saldo = QtWidgets.QPushButton(self.frame_Saldo)
        self.pushButton_agregar_saldo.setGeometry(QtCore.QRect(150, 10, 35, 35))
        self.pushButton_agregar_saldo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_agregar_saldo.setStyleSheet("image: url(:/newPrefix/icons8-positive-48.png);")
        self.pushButton_agregar_saldo.setText("")
        self.pushButton_agregar_saldo.setObjectName("pushButton_agregar_saldo")
        self.verticalLayout_Menu.addWidget(self.frame_Saldo)
        self.frame_Deuda = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_Deuda.setStyleSheet("background-color: rgb(255, 103, 104);\n"
"border-radius: 6px;")
        self.frame_Deuda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Deuda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Deuda.setObjectName("frame_Deuda")
        self.Label_Deuda = QtWidgets.QLabel(self.frame_Deuda)
        self.Label_Deuda.setGeometry(QtCore.QRect(10, 18, 181, 20))
        self.Label_Deuda.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Roboto Black\";")
        self.Label_Deuda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Label_Deuda.setScaledContents(False)
        self.Label_Deuda.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Deuda.setWordWrap(False)
        self.Label_Deuda.setIndent(-1)
        self.Label_Deuda.setObjectName("Label_Deuda")
        self.verticalLayout_Menu.addWidget(self.frame_Deuda)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_Menu.addWidget(self.line)
        self.pushButton_Inicio = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Inicio.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Inicio.sizePolicy().hasHeightForWidth())
        self.pushButton_Inicio.setSizePolicy(sizePolicy)
        self.pushButton_Inicio.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_Inicio.setFont(font)
        self.pushButton_Inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Inicio.setStyleSheet("background-color: #6b778d;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Roboto Medium\";\n"
"border-radius: 6px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-google-home-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Inicio.setIcon(icon)
        self.pushButton_Inicio.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Inicio.setObjectName("pushButton_Inicio")
		#EVENTO PRUEBA
		self.pushButton_Inicio.clicked.connect(cambioPantalla)
		#FIN
        self.verticalLayout_Menu.addWidget(self.pushButton_Inicio)
        self.pushButton_Resumen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Resumen.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Resumen.sizePolicy().hasHeightForWidth())
        self.pushButton_Resumen.setSizePolicy(sizePolicy)
        self.pushButton_Resumen.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_Resumen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Resumen.setStyleSheet("background-color: #6b778d;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Roboto Medium\";\n"
"border-radius: 6px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-spreadsheet-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Resumen.setIcon(icon1)
        self.pushButton_Resumen.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Resumen.setObjectName("pushButton_Resumen")
        self.verticalLayout_Menu.addWidget(self.pushButton_Resumen)
        self.pushButton_Categorias = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Categorias.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Categorias.sizePolicy().hasHeightForWidth())
        self.pushButton_Categorias.setSizePolicy(sizePolicy)
        self.pushButton_Categorias.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_Categorias.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Categorias.setStyleSheet("background-color: #6b778d;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Roboto Medium\";\n"
"border-radius: 6px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-sorting-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Categorias.setIcon(icon2)
        self.pushButton_Categorias.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Categorias.setObjectName("pushButton_Categorias")
        self.verticalLayout_Menu.addWidget(self.pushButton_Categorias)
        self.pushButton_Historial = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Historial.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Historial.sizePolicy().hasHeightForWidth())
        self.pushButton_Historial.setSizePolicy(sizePolicy)
        self.pushButton_Historial.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_Historial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Historial.setStyleSheet("background-color: #6b778d;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Roboto Medium\";\n"
"border-radius: 6px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-statistics-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Historial.setIcon(icon3)
        self.pushButton_Historial.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Historial.setObjectName("pushButton_Historial")
        self.verticalLayout_Menu.addWidget(self.pushButton_Historial)
        self.pushButton_Estadisticas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Estadisticas.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Estadisticas.sizePolicy().hasHeightForWidth())
        self.pushButton_Estadisticas.setSizePolicy(sizePolicy)
        self.pushButton_Estadisticas.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_Estadisticas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Estadisticas.setStyleSheet("background-color: #6b778d;\n"
"color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Roboto Medium\";\n"
"border-radius: 6px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-doughnut-chart-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Estadisticas.setIcon(icon4)
        self.pushButton_Estadisticas.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Estadisticas.setCheckable(False)
        self.pushButton_Estadisticas.setChecked(False)
        self.pushButton_Estadisticas.setAutoRepeat(False)
        self.pushButton_Estadisticas.setAutoExclusive(False)
        self.pushButton_Estadisticas.setObjectName("pushButton_Estadisticas")
        self.verticalLayout_Menu.addWidget(self.pushButton_Estadisticas)
        self.pushButton_Ayuda = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Ayuda.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Ayuda.sizePolicy().hasHeightForWidth())
        self.pushButton_Ayuda.setSizePolicy(sizePolicy)
        self.pushButton_Ayuda.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_Ayuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Ayuda.setStyleSheet("background-color: #6b778d;\n"
"font: 57 14pt \"Roboto Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 6px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons8-help-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Ayuda.setIcon(icon5)
        self.pushButton_Ayuda.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_Ayuda.setObjectName("pushButton_Ayuda")
        self.verticalLayout_Menu.addWidget(self.pushButton_Ayuda)
        self.inicio_frame = QtWidgets.QFrame(self.frame_main_w)
        self.inicio_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.inicio_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inicio_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inicio_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inicio_frame.setObjectName("inicio_frame")
        self.label_2 = QtWidgets.QLabel(self.inicio_frame)
        self.label_2.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.inicio_frame)
        self.label_4.setGeometry(QtCore.QRect(270, 40, 31, 16))
        self.label_4.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_4.setObjectName("label_4")
        self.resumen_frame = QtWidgets.QFrame(self.frame_main_w)
        self.resumen_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.resumen_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resumen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resumen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resumen_frame.setObjectName("resumen_frame")
        self.label_7 = QtWidgets.QLabel(self.resumen_frame)
        self.label_7.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_7.setStyleSheet("background: transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.resumen_frame)
        self.label_8.setGeometry(QtCore.QRect(270, 40, 51, 16))
        self.label_8.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_8.setObjectName("label_8")
        self.categorias_frame = QtWidgets.QFrame(self.frame_main_w)
        self.categorias_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.categorias_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categorias_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.categorias_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.categorias_frame.setObjectName("categorias_frame")
        self.label_11 = QtWidgets.QLabel(self.categorias_frame)
        self.label_11.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_11.setStyleSheet("background: transparent;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.categorias_frame)
        self.label_12.setGeometry(QtCore.QRect(270, 40, 71, 16))
        self.label_12.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_12.setObjectName("label_12")
        self.estadisticas_frame = QtWidgets.QFrame(self.frame_main_w)
        self.estadisticas_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.estadisticas_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.estadisticas_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.estadisticas_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.estadisticas_frame.setObjectName("estadisticas_frame")
        self.label_13 = QtWidgets.QLabel(self.estadisticas_frame)
        self.label_13.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_13.setStyleSheet("background: transparent;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.estadisticas_frame)
        self.label_14.setGeometry(QtCore.QRect(270, 40, 81, 16))
        self.label_14.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_14.setObjectName("label_14")
        self.ayuda_frame = QtWidgets.QFrame(self.frame_main_w)
        self.ayuda_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.ayuda_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ayuda_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ayuda_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ayuda_frame.setObjectName("ayuda_frame")
        self.label_15 = QtWidgets.QLabel(self.ayuda_frame)
        self.label_15.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_15.setStyleSheet("background: transparent;")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.ayuda_frame)
        self.label_16.setGeometry(QtCore.QRect(270, 40, 41, 16))
        self.label_16.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_16.setObjectName("label_16")
        self.historial_frame = QtWidgets.QFrame(self.frame_main_w)
        self.historial_frame.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.historial_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.historial_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historial_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historial_frame.setObjectName("historial_frame")
        self.label_17 = QtWidgets.QLabel(self.historial_frame)
        self.label_17.setGeometry(QtCore.QRect(50, -30, 983, 982))
        self.label_17.setStyleSheet("background: transparent;")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/newPrefix/Logo_oficial_vector_bl.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.historial_frame)
        self.label_18.setGeometry(QtCore.QRect(270, 40, 61, 16))
        self.label_18.setStyleSheet("font: 87 8pt \"Roboto Black\";")
        self.label_18.setObjectName("label_18")
        self.menu_frame.raise_()
        self.ayuda_frame.raise_()
        self.categorias_frame.raise_()
        self.estadisticas_frame.raise_()
        self.historial_frame.raise_()
        self.inicio_frame.raise_()
        self.resumen_frame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BetaSave"))
        self.Label_Saldo.setText(_translate("Form", "Saldo: $00000.00"))
        self.Label_Deuda.setText(_translate("Form", "Deuda: $00000.00"))
        self.pushButton_Inicio.setText(_translate("Form", "Inicio"))
        self.pushButton_Resumen.setText(_translate("Form", "Resumen"))
        self.pushButton_Categorias.setText(_translate("Form", "Categorías"))
        self.pushButton_Historial.setText(_translate("Form", "Historial"))
        self.pushButton_Estadisticas.setText(_translate("Form", "Estadísticas"))
        self.pushButton_Ayuda.setText(_translate("Form", "Ayuda"))
        self.label_4.setText(_translate("Form", "INICIO"))
        self.label_8.setText(_translate("Form", "RESUMEN"))
        self.label_12.setText(_translate("Form", "CATEGORIAS"))
        self.label_14.setText(_translate("Form", "ESTADISTICAS"))
        self.label_16.setText(_translate("Form", "AYUDA"))
        self.label_18.setText(_translate("Form", "HISTORIAL"))


import Img_rc
