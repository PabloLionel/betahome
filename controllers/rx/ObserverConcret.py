#######################################################
# 
# ObserverConcret.py
# Python implementation of the Class ObserverConcret
# Created on:      23-jun.-2019 6:56:33
# Original author: Betacode
# 
#######################################################
import re
from Subject import Subject, checksubject
from SubjectConcret import SubjectConcret
from IObserver import IObserver

class ObserverConcret(IObserver):

    @checksubject()
    def __init__(self, subject=None):
        self.subjectState = subject
    
    def update(self):
        print(self, self.subjectState.__dict__)

if __name__ == "__main__":
    sujeto = SubjectConcret()

    observer1 = ObserverConcret(sujeto)
    observer2 = ObserverConcret(sujeto)

    sujeto.increment() # 1
    sujeto.increment() # 2

    sujeto.addObserver(observer1)

    sujeto.increment() # (obs1, {...__count: 3})
    sujeto.increment() # (obs1, {...__count: 4})

    sujeto.addObserver(observer2)
    
    sujeto.increment() # (obs1, {...__count: 5}) (obs2, {...__count: 5})
    sujeto.increment() # (obs1, {...__count: 6}) (obs2, {...__count: 6})
