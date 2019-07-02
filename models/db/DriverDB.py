#######################################################
# 
# DriverDB.py
# Python implementation of the Class DriverDB
# Created on:      23-jun.-2019 6:56:26
# Original author: Betacode
# 
#######################################################
import sqlite3 as sq3

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

    def funcname(parameter_list):
        pass

    def __getState():
        pass

    def __getType(value):
        pass

    def __parserType(type):
        pass

    def save():
        pass