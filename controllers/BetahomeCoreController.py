#######################################################
# 
# BetahomeCorController.py
# Python implementation of the Class BetahomeCorController
# Created on:      23-jun.-2019 6:56:24
# Original author: Betacode
# 
#######################################################
from controllers.UserController import UserController
from controllers.CategoryController import CategoryController

class BetahomeCoreController:

    def __init__(self, view, model):
        # A diferencia de otras objetos
        # el controlador conoce a la vista
        # y el modelo.
        self.view = view
        self.model = model
        # de aquí en más, al igual que las demas
        # entidades se instancian sus propios objetos
        # a manejar.
        self.user = UserController(model.user)
        self.category = CategoryController(model.category)

    def checkUser(self):
        return bool(self.user.usermodel)

    def close(self):
        pass

    def open(self):
        pass

