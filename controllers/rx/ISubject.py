#######################################################
# 
# ISubject.py
# Python implementation of the Class ISubject
# Created on:      23-jun.-2019 6:56:32
# Original author: Betacode
# 
#######################################################
from abc import ABCMeta, abstractmethod

class ISubject(metaclass=ABCMeta):
    """Interfaz que implementa las firmas
    necesarias para un Sujeto.
    """
    @abstractmethod
    def addObserver(self, o): return NotImplementedError
    
    @abstractmethod
    def delObserver(self, o): return NotImplementedError

    @abstractmethod
    def notify(self, ): return NotImplementedError