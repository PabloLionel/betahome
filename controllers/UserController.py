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

    def create(): # crear
        pass

    def find(filter=lambda x: x): # leer
        pass

    def update(user): # actualizar
        pass

    def delete(id=None): # eliminar
        pass

    def login():
        pass

    def logout():
        pass