from PyQt5 import QtCore, QtGui, QtWidgets, uic
from MainW import Ui_Form

class MyWindow(QtWidgets.QMainWindow):
    def _init_(self):
        super(MyWindow,self)._init_()
        # ui = Ui_Form()
        # ui.setupUi(Form)
        # Form.show()
        uic.loadUi('MainW.ui.xml',self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())