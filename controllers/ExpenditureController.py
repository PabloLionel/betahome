#######################################################
# 
# ExpenditureController.py
# Python implementation of the Class ExpenditureController
# Created on:      09-jul.-2019 23:21:39
# Original author: Betacode
# 
#######################################################

class ExpenditureController:
    __expenditure = None
    def __init__(self):
        self.__expenditure = None

    @property
    def expenditure(self):
        return self.__expenditure

    @expenditure.setter
    def expenditure(self, e):
        self.__expenditure = e

    def create(self): # crear
        if not self.expenditure:
            self.expenditurel.create()

    def update(self): # actualizar
        self.expenditure.update()

    def find(self,filter=lambda x: x): # leer
        self.expenditure.find(filter)

    def delete(self): # eliminar
        self.expenditure.delete()