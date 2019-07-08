#######################################################
# 
# BetahomeCorController.py
# Python implementation of the Class BetahomeCorController
# Created on:      23-jun.-2019 6:56:24
# Original author: Betacode
# 
#######################################################
from .UserController import UserController

class BetahomeCoreController:

    def __init__(self, view, model):
        self.view = view
        self.user = UserController(model.user)

    def checkUser(self):
        return bool(self.view.user and self.model.user)

    def close(self):
        pass

    def open(self):
        if self.checkUser():
            pass
        else: 
            self.view.loadUser()

    # def getUserData(self, *args, **kwargs):
    #     pass
