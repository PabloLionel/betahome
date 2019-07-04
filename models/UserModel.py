#######################################################
# 
# UserModel.py
# Python implementation of the Class UserModel
# Created on:      23-jun.-2019 6:56:39
# Original author: Betacode
# 
#######################################################
from .models import DataAccessObject

class UserModel(DataAccessObject):
    __MAX_PASSWORD = 20
    __MIN_PASSWORD = 8

    def __init__(self, name, pwd, saldo):
        self.nameuser = name
        self.password = pwd
        self.saldo = saldo

    def create(self, ):
        pass

    def delete(self, ):
        pass

    def find(filter):
        pass

    def isRegisterUser(self, nameuser):
        """+ isRegisterUser(nameuser: str): bool
        """
        pass

    def singUp(self, ):
        pass

    def update(self, ):
        pass
    
    def __str__(self):
        return "Holaaa soy un usario :D."


if __name__ == "__main__":
    user = UserModel(name="Pablo", pwd="1234", saldo=100000) # jeje :D

    print("un useeer :) --->", str(user))