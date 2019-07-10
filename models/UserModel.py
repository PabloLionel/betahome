#######################################################
# 
# UserModel.py
# Python implementation of the Class UserModel
# Created on:      23-jun.-2019 6:56:39
# Original author: Betacode
# 
#######################################################
try:
    from .dao import DataAccessObject
    from .db.Query import Query
except:
    from dao import DataAccessObject 
    from db.Query import Query

class UserModel(DataAccessObject):
    def __init__(self, name, pwd, salary, *args, **kwargs):
        DataAccessObject.__init__(self)
        self.init()
        self.user_name = name
        self.password = pwd
        self.salary = salary
        self.id = self.__getId(name, pwd)
    
    def name_table():
        return 'user'

    def __getId(self, user_name, password):
            res = self.find()
            id = None
            for r in res:
                id, _, pwd, _ = r
                if password == pwd:
                    break
            if id != None:
                return id
            else:
                # a futuro usar loggin.info_warn
                print('[WARN] Id no encontrado, clave incorrecta.')

    def init(self):
        self.driver.runQuery(
            Query(
                f"""
                CREATE TABLE IF NOT EXISTS {UserModel.name_table()} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name VARCHAR (20) NOT null UNIQUE,
                    password VARCHAR (16) NOT null,
                    salary FLOAT
                )
                """
            )
        )

    def create(self):
        if self.id == None:
            super().create(
                UserModel.name_table(),
                # id=...,                 # POR SER AUTOINCREMENTAL.
                user_name=self.user_name,
                password=self.password,
                salary=self.salary,
            )
            self.id = self.__getId(self.user_name, self.password)

    def update(self):
        if self.id == None:
            self.create()
        else:
            super().update(
                UserModel.name_table(),     # nombre de la tabla
                'id',                       # columna a comparar
                self.id,                    # item a comparar
                user_name=self.user_name,   # campos a actualizar:
                password=self.password,
                salary=self.salary,
            )

    def find(self, pfilter=None):
        if pfilter:
            return super().find(UserModel.name_table(), pfilter)
        else:
            return super().find(UserModel.name_table())
        
    def delete(self ):
        if self.id == None:
            self.id = self.__getId(self.user_name, self.password)
        super().delete(UserModel.name_table(), id=self.id)

    def isRegisterUser(self, nameuser):
        """+ isRegisterUser(nameuser: str): bool
        """
        pass
    

if __name__ == "__main__":
    user = UserModel(name="Pablo", pwd="1234", salary=100000) # jeje :D
    