#######################################################
# 
# Subject.py
# Python implementation of the Class Subject
# Created on:      23-jun.-2019 6:56:35
# Original author: Betacode
# 
#######################################################
# para volver una carpeta atras, de lo contrario no veiramos a controllers
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('')))
import re
from ISubject import ISubject
from IObserver import IObserver, checkobserver

class Subject(ISubject):
    __observers = list() # list<IObserver>()

    @checkobserver()
    def addObserver(self, o):
        self.__observers.append(o)
    @checkobserver()
    def delObserver(self, o):
        self.__observers.pop(o)

    def notify(self):
        for o in self.__observers:
            o.update()

## Utils:
def checksubject(config=None):
    def checks(constructor): # constructor --> def __init__(self, *args, **kwargs): ...
        def w(*args, **kwargs):
            if not args:
                raise Exception('No arguments in the constructor.')

            subject = args[1]
            # print(f"subject {subject.__dict__}")

            if not subject:
                raise Exception('A subject object was expected.')
            
            # verificamos, antes que nada, que el sujeto pasado
            # por parametro herede de la clase Subject.
            if not isinstance(subject, Subject):
                raise Exception(f'{subject.__name__} does not inherit from the Subject class.')
            
            met_subject_parent = iter(
                filter(
                        lambda x: re.findall('^[a-z]+', x),
                        dir(Subject)
                    )
                )
            met_subject = list(
                filter(
                        lambda x: re.findall('^[a-z]+', x),
                        dir(subject)
                    )
                )
            # recorremos cada metodo o y verificamos
            # que estan implementados en el sujeto pasado por
            # parametro.
            for method in met_subject_parent:
                if method not in met_subject:
                    raise Exception(f'{subject.__name__} does not implement the methods {method}.')
            
            # esta todo ok jaja
            r = constructor(*args, **kwargs)
            return r
        return w
    return checks