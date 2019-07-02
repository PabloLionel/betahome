#######################################################
# 
# IDao.py
# Python implementation of the Class IDao
# Created on:      23-jun.-2019 6:56:30
# Original author: Betacode
# 
#######################################################
from abc import ABCMeta, abstractmethod

class IDataAccessObject(metaclass=ABCMeta):

    @abstractmethod
    def create(self): return NotImplementedError

    @abstractmethod
    def update(self): return NotImplementedError

    @abstractmethod
    def find(self, filter): return NotImplementedError

    @abstractmethod
    def delete(self): return NotImplementedError