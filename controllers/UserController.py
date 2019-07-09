#######################################################
# 
# UserController.py
# Python implementation of the Class UserController
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from .rx.Subject import Subject
from models.UserModel import UserModel

class UserController(Subject):
    __usermodel = None
    def __init__(self, user=None):
        self.usermodel = user

    @property
    def usermodel(self):
        return self.__usermodel

    @usermodel.setter
    def usermodel(self, m):
        self.__usermodel = m
        self.notify()

    def create(self): # crear
        if not self.usermodel:
            self.usermodel.create()

    def update(self): # actualizar
        self.usermodel.update()

    def find(self,filter=lambda x: x): # leer
        self.usermodel.find(filter)

    def delete(self): # eliminar
        self.usermodel.delete()

    def signup(self, name, psw, salary=0):
        self.usermodel = UserModel(name, psw, salary)
        self.usermodel.create()

    def login(self, name, psw):
        return self.usermodel.password == psw

    def logout(self):
        pass