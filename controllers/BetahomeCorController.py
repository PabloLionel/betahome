#######################################################
# 
# BetahomeCorController.py
# Python implementation of the Class BetahomeCorController
# Created on:      23-jun.-2019 6:56:24
# Original author: Betacode
# 
#######################################################

class BetahomeCoreController:
    
    def __init__(self):
        self.user = None
        self.dao=None

    def checkUser(self):
        return bool(self.user)

    def close(self):
        pass

    def open(self):
        pass