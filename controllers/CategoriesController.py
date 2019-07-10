#######################################################
# 
# CategoriesController.py
# Python implementation of the Class CategoriesController
# Created on:      10-jul.-2019 23:21:39
# Original author: Betacode
# 
#######################################################

class CategoriesController:
    __categoriesmodel = None
    def __init__(self, categories=None):
        self.__categoriesmodel = categories

    @property
    def categoriesmodel(self):
        return self.__categoriesmodel

    @categoriesmodel.setter
    def categorymodel(self, m):
        self.__categoriesmodel = m
        self.notify()

    def create(self): # crear
        if not self.categoriesmodel:
            self.categoriesmodel.create()

    def update(self): # actualizar
        self.categoriesmodel.update()

    def find(self,filter=lambda x: x): # leer
        self.categoriesmodel.find(filter)

    def delete(self): # eliminar
        self.categoriesmodel.delete()