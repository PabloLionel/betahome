import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from principal import Ui_Form
from log import Ui_MainWindow


class MainApplication(QMainWindow, Ui_Form):
    
	def __init__(self, parent = None):
		super(MainApplication, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Inicio.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 45px')	
		self.pushButton_Inicio.clicked.connect(self.cambiarColorInicio)
		self.pushButton_Resumen.clicked.connect(self.cambiarColorResumen)
		self.pushButton_Categorias.clicked.connect(self.cambiarColorCategorias)
		self.pushButton_Historial.clicked.connect(self.cambiarColorHistorial)
		self.pushButton_Estadisticas.clicked.connect(self.cambiarColorEstadisticas)
		self.pushButton_Ayuda.clicked.connect(self.cambiarColorAyuda)

	def cambiarColorInicio(self):
		self.pushButton_Inicio.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')	
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')

	def cambiarColorResumen(self):
		self.pushButton_Resumen.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')

	def cambiarColorCategorias(self):
		self.pushButton_Categorias.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')

	def cambiarColorHistorial(self):
		self.pushButton_Historial.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')

	def cambiarColorEstadisticas(self):
		self.pushButton_Estadisticas.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')

	def cambiarColorAyuda(self):
		self.pushButton_Ayuda.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')	
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')	
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; padding-left: 45px')
		

class Login(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.btn_ingreso_login.clicked.connect(self.abrirVentanaPrincipal)

    def abrirVentanaPrincipal(self):
        self.menu = MainApplication()
        self.menu.show()
        self.close()


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())