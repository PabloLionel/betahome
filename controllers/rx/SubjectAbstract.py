#######################################################
# 
# SubjectAbstract.py
# Python implementation of the Class SubjectAbstract
# Created on:      23-jun.-2019 6:56:35
# Original author: Betacode
# 
#######################################################
from controllers.rx.ISubject import ISubject
from controllers.rx.IObserver import IObserver

class SubjectAbstract(ISubject):
    m_IObserver= IObserver()

    def addObserver(o):
        pass

    def delObserver(o):
        pass

    def notify():
        pass