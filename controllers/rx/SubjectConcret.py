#######################################################
# 
# SubjectConcret.py
# Python implementation of the Class SubjectConcret
# Created on:      23-jun.-2019 6:56:36
# Original author: Betacode
# 
#######################################################
from Subject import Subject

class SubjectConcret(Subject):

    def __init__(self):
        self.__count = 0

    # setters & getters
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, c):
        self.__count = c
        self.notify()
        
    def increment(self, inc=1):
        self.count += inc