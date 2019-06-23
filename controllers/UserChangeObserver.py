#######################################################
# 
# UserChangeObserver.py
# Python implementation of the Class UserChangeObserver
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from controllers.rx.IObserver import IObserver
from controllers.UserController import UserController

class UserChangeObserver(IObserver):
    m_UserController= UserController()


    def update():
        pass