#######################################################
# 
# UserModel.py
# Python implementation of the Class UserModel
# Created on:      23-jun.-2019 6:56:39
# Original author: Betacode
# 
#######################################################
from db.DriverDB import DriverDB
from IDao import IDao

class UserModel(DriverDB, IDao):
    __MAX_PASSWORD = 20
    __MIN_PASSWORD = 8

    def __init__(self, name, pwd, saldo):
        self.nameuser = name
        self.password = pwd
        self.saldo = saldo

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
    
    def __str__(self):
        return "Holaaa soy un usario :D."


if __name__ == "__main__":
    user = UserModel(name="Pablo", pwd="1234", saldo=100000) # jeje :D

    print("un useeer :) --->", str(user))