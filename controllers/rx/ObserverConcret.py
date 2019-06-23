#######################################################
# 
# ObserverConcret.py
# Python implementation of the Class ObserverConcret
# Created on:      23-jun.-2019 6:56:33
# Original author: Betacode
# 
#######################################################
from controllers.rx.SubjectConcret import SubjectConcret
from controllers.rx.IObserver import IObserver

class ObserverConcret(IObserver):
    m_SubjectConcret= SubjectConcret()

    def update():
        pass