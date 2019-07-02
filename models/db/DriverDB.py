#######################################################
# 
# DriverDB.py
# Python implementation of the Class DriverDB
# Created on:      23-jun.-2019 6:56:26
# Original author: Betacode
# 
#######################################################
import sys
import os
print(os.path.dirname('.'))
import sqlite3 as sq3

# sys.path.append(os.path.dirname(os.path.abspath('models/db')))
# from IConectorAdapter import IConectorAdapter
# import sys
# for dir in sys.path:
#     print(dir)

class DriverDB:

    def __init__(self):
        self.__conn=sq3.connect(":memory:")
        self.__cursor=self.__conn.cursor()
        

    @property
    def conn(self):
        return self.__conn
    
    @conn.setter
    def conn(self, c):
        self.__conn = c

    @property
    def cursor(self):
        return self.__cursor
    
    @cursor.setter
    def cursor(self, c):
        self.__cursor = c

    def funcname(self, parameter_list):
        pass

    def __getState(self, ):
        pass

    def __getType(self, value):
        pass

    def __parserType(self, type):
        pass

    def save(self, ):
        pass