#######################################################
# 
# ObserverConcret.py
# Python implementation of the Class ObserverConcret
# Created on:      23-jun.-2019 6:56:33
# Original author: Betacode
# 
#######################################################
# para volver una carpeta atras, de lo contrario no veiramos a controllers
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('')))
import re
from Subject import Subject, checksubject
from SubjectConcret import SubjectConcret
from IObserver import IObserver

class ObserverConcret(IObserver):

    @checksubject()
    def __init__(self, subject=None):
        self.subjectState = subject
    
    def update(self):
        print(self.subjectState.__dict__)

if __name__ == "__main__":
    sujeto = SubjectConcret()
    observer1 = ObserverConcret(sujeto)

    sujeto.increment()
    sujeto.increment()

    sujeto.addObserver(observer1)

    sujeto.increment()
    sujeto.increment()
    sujeto.increment()
