#######################################################
# 
# UserChangeObserver.py
# Python implementation of the Class UserChangeObserver
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from .rx.IObserver import IObserver
from .UserController import UserController

class UserChangeObserver(IObserver):
    state_UserController= UserController()

    def __init__(self):
        pass

    def update(self):
        pass