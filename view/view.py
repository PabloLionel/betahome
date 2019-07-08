from .ui.Login import Login
class View:

    def __init__(self, *args, **kwargs):
        self.user = None
        # self.init()
    
    def init(self, user):
        # abrir login.
        Login(user)