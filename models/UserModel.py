#######################################################
# 
# UserModel.py
# Python implementation of the Class UserModel
# Created on:      23-jun.-2019 6:56:39
# Original author: Betacode
# 
#######################################################
from models.db.DriverDB import DriverDB
from models.IDao import IDao

class UserModel(DriverDB, IDao):
    __MAX_PASSWORD = 20
    __MIN_PASSWORD = 8
    def __getState():
        pass

    def create():
        pass

    def delete():
        pass

    def find(filter):
        pass

    def isRegisterUser(nameuser):
        """+ isRegisterUser(nameuser: str): bool
        """
        pass

    def singUp():
        pass

    def update():
        pass