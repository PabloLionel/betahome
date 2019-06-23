#######################################################
# 
# IObserver.py
# Python implementation of the Class IObserver
# Created on:      23-jun.-2019 6:56:31
# Original author: Betacode
# 
#######################################################
import re
from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):
    """Interfaz que implementa las firmas
    necesarias para un Observador.
    """
    @abstractmethod
    def update(self): return NotImplementedError

## Utils

def checkobserver(config=None):
    def checks(met): # method --> def __init__(self, observer): ...
        def w(*args, **kwargs):
            if not args:
                raise Exception('No arguments in the constructor.')

            observer = args[1]
            # print(f"observer {observer.__dict__}")

            if not observer:
                raise Exception('A ObserverConcrete class was expected.')
            # verificamos, antes que nada, que el sujeto pasado
            # por parametro herede de la clase IObserver.
            if not isinstance(observer, IObserver):
                raise Exception(f'{observer.__name__} does not inherit from the observerAbstract class.')
            
            met_observer_parent = iter(
                filter(
                        lambda x: re.findall('^[a-z]+', x),
                        dir(IObserver)
                    )
                )
            met_observer = list(
                filter(
                        lambda x: re.findall('^[a-z]+', x),
                        dir(observer)
                    )
                )
            # recorremos cada metodo abstracto y verificamos
            # que estan implementados en el sujeto pasado por
            # parametro.
            for method in met_observer_parent:
                if method not in met_observer:
                    raise Exception(f'{observer.__name__} does not implement the abstract methods {method}.')
            
            # esta todo ok jaja
            r = met(*args, **kwargs)
            return r
        return w
    return checks