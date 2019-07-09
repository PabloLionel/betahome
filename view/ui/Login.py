from view.ui.UserInterface import UserInterface

class LoginWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_ingreso_login.clicked.connect(Login.login) # self.abrirVentanaPrincipal)

    def loadWithOutUser(self):
        self.Label_bienvenida.hide()
        return (self.user_in.text, self.pass_in.text)

    def loadWithUser(self, name):
        self.Label_bienvenida.setText(name)
        self.user_in.hide()
        self.label_3.hide()

    def openMain(self):
        self.abrirVentanaPrincipal()


class Login:
    """
    Parameters
    ----------
    user: UserController

    Returns
    -------
    None

    Default
    -------
    Login() # error
    """
    def __init__(self, user):
        self.login = LoginWindow()
        self.user = user
        if self.user != None:
            print(user.usermodel)
            self.login.loadWithUser(user.usermodel.user_name)            
        self.login.show()

    def login(): # static method
        name, pws = self.login.loadWithOutUser()
        if UserInterface.isUsernameCorrect(name) and UserInterface.isPasswordCorrect(pws):
            self.login.openMain()
            self.user
        else:
            pass