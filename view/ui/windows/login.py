import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .main_window import Ui_Form
from .log_window import Ui_MainWindow
from .agregar_cuenta_indi import Ui_agregar_cuenta
from .saldo_plus import Ui_Form_saldo


class MainApplication(QMainWindow, Ui_Form):
    
	def __init__(self, parent = None):
		super(MainApplication, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Inicio.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')	
		self.pushButton_Inicio.clicked.connect(self.cambiarColorInicio)
		self.pushButton_Resumen.clicked.connect(self.cambiarColorResumen)
		self.pushButton_Categorias.clicked.connect(self.cambiarColorCategorias)
		self.pushButton_Historial.clicked.connect(self.cambiarColorHistorial)
		self.pushButton_Estadisticas.clicked.connect(self.cambiarColorEstadisticas)
		self.pushButton_Ayuda.clicked.connect(self.cambiarColorAyuda)
		self.pushButton_ing_cuenta_nueva.clicked.connect(self.abrir_vent_cuenta)
		self.pushButton_agregar_saldo.clicked.connect(self.abrir_ventana_saldo)

	def abrir_vent_cuenta(self):
		self.menu = AddCuenta()
		self.menu.show()

	def abrir_ventana_saldo(self):
		self.menu = AddSaldo()
		self.menu.show()

	def cambiarColorInicio(self):
		self.pushButton_Inicio.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')	
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')

	def cambiarColorResumen(self):
		self.pushButton_Resumen.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')

	def cambiarColorCategorias(self):
		self.pushButton_Categorias.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')

	def cambiarColorHistorial(self):
		self.pushButton_Historial.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')

	def cambiarColorEstadisticas(self):
		self.pushButton_Estadisticas.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Ayuda.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')

	def cambiarColorAyuda(self):
		self.pushButton_Ayuda.setStyleSheet('background-color: #404B61; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 40px')	
		self.pushButton_Inicio.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')	
		self.pushButton_Resumen.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Categorias.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Historial.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')
		self.pushButton_Estadisticas.setStyleSheet('background-color: #6b778d; color: white; font: 57 14pt "Roboto Medium"; border-radius: 6px; text-align: left; padding-left: 30px')


class AddCuenta(QMainWindow, Ui_agregar_cuenta):
	def __init__(self, parent = None):
		super(AddCuenta, self).__init__(parent)
		self.setupUi(self)

class AddSaldo(QMainWindow, Ui_Form_saldo):
	def __init__(self, parent = None):
		super(AddSaldo, self).__init__(parent)
		self.setupUi(self)


class Login(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None, *args, **kwargs):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.controller = kwargs.get("controller")
        self.initUI()
    
    def initUI(self):
        self.btn_ingreso_login.clicked.connect(self.login)
        
        if self.controller.checkUser():
            self.loadWithUser(self.controller.user.usermodel.user_name)
            self.user_in.setText(self.controller.user.usermodel.user_name)
        else:
            self.loadWithOutUser()

        self.show()

    def login(self):
        user = self.user_in.text()
        psw = self.pass_in.text()

        # validar campos de entrada aqui...
        userCorrect, msgUser = self.controller.view.validUserField.isUsernameCorrect(user)
        passCorrect1, msgPass1 = self.controller.view.validUserField.checkLength(len(psw))
        passCorrect2, msgPass2 = self.controller.view.validUserField.isPasswordCorrect(psw)
        
        if not userCorrect:
            print(msgUser)
            return
        if not passCorrect1:
            print(msgPass1)
            return
        if not passCorrect2:
            print(msgPass2)
            return

        if not self.controller.checkUser():
            self.controller.user.signup(user, psw)
            self.openMain()
            return
        
        if self.controller.user.login(user, psw):
            self.openMain()
        else:
            pass

    def loadWithOutUser(self):
        self.Label_bienvenida.hide()

    def loadWithUser(self, name):
        self.Label_bienvenida.setText(name)
        self.user_in.hide()
        self.label_3.hide()

    def openMain(self):
        self.main = MainApplication()
        self.main.show()
        self.close()
    


def login(sys, controller):
    app = QApplication(sys.argv)
    win = Login(controller=controller)
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Login()
    sys.exit(app.exec_())