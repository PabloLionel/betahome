import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MainWindow import Ui_MainWindow
from Saldo import Ui_Dialog

class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainApplication, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_agregar_saldo_3.clicked.connect(self.abrirVentana)


    def abrirVentana(self):
        self.ventanaSaldo = VentanaSaldo(self)
        self.ventanaSaldo.show()





class VentanaSaldo(QDialog, Ui_Dialog):

    def __init__(self, parent = None):
        super(VentanaSaldo, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_aceptar_ingreso_saldo.clicked.connect(self.entradaSaldo)
        self.pushButton_cancelar_ingreso_saldo.clicked.connect(self.cancelar)



    def cancelar(self):

        eleccion = QMessageBox(self)
        eleccion.setWindowTitle('Cancelar')
        eleccion.setText('¿Desea cancelar el ingreso?')
        eleccion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = eleccion.button(QMessageBox.Yes)
        buttonY.setText('Si')
        buttonN = eleccion.button(QMessageBox.No)
        buttonN.setText('No')
        eleccion.exec_()

        if eleccion.clickedButton() == buttonY:
            self.close()

        else:
            pass

    def entradaSaldo(self):

        entrada = self.campo_ingreso_saldo.text()


        """self.campo_ingreso_saldo.setValidator(QDoubleValidator(
            0.01,  # bottom
            50000.00,  # top
            2,  # decimals
        )
        )"""
        if re.match("^\d+\.?(\d{1,2})$", entrada):
            # str.replace()
            # entrada = entrada.replace("\d$",".00")
            self.parent().Label_Saldo_3.setText(entrada)

            self.close()







if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())