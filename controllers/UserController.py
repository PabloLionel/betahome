#######################################################
# 
# UserController.py
# Python implementation of the Class UserController
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from .rx.Subject import Subject

class UserController(Subject):

    def __init__(self, user=None):
        self.usermodel = user

    def create(self): # crear
        if not self.usermodel:
            self.usermodel.create()

    def update(self): # actualizar
        
        self.usermodel.update()

    def find(self,filter=lambda x: x): # leer
        self.usermodel.find(filter)

    def delete(self): # eliminar
        self.usermodel.delete()

    def login(self):
        pass

    def logout(self):
        pass