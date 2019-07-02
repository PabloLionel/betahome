#######################################################
# 
# UserController.py
# Python implementation of the Class UserController
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from rx.Subject import Subject


class UserController(Subject):

    def __init__(self, user):
        self.usermodel = user    

    def create(self): # crear
        pass

    def find(self,filter=lambda x: x): # leer
        pass

    def update(self,user): # actualizar
        pass

    def delete(self,id=None): # eliminar
        pass

    def login(self):
        pass

    def logout(self):
        pass