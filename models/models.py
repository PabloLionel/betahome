try:
    from .dao import DataAccessObject
    from .UserModel import UserModel
except:
    from dao import DataAccessObject
    from UserModel import UserModel
    
class Model:
    def __init__(self):
        self.user = None