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

class UserModel(DataAccessObject):
    __MAX_PASSWORD = 20
    __MIN_PASSWORD = 8

    def __init__(self, name, pwd, salary, *args, **kwargs):
        DataAccessObject.__init__(self)
        self.init()
        self.user_name = name
        self.password = pwd
        self.salary = salary
        self.id = self.__getId(user_name, password)
    
    @property
        def name_table(self):
            return 'user'

    def __getId(self, user_name, password):
            res = self.driver.selectAll(
                self.name_table,
                ['id','user_name', 'password'],
                'user_name',    # columna a comparar
                user_name       # valor item a filtrar
            )
            for r in res:
                id, _, pwd = r
                if password == pwd:
                    break
            if id:
                return id
            else:
                # a futuro usar loggin.info_warn
                print('[WARN] Id no encontrado, clave incorrecta.')

    def init(self):
        self.driver.runQuery(
            Query(
                f"""
                CREATE TABLE IF NOT EXISTS {self.name_table}(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    user_name VARCHAR (20) NOT null UNIQUE,
                    password VARCHAR (16) NOT null,
                    salary FLOAT
                )
                """
            )
        )

    def create(self, ):
        if self.id == None:
            super().create(
                self.name_table,
                id='rowid',                 # POR SER AUTOINCREMENTAL.
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
                self.name_table,            # nombre de la tabla
                'id',                       # columna a comparar
                self.id,                    # item a comparar
                user_name=self.user_name,   # campos a actualizar:
                password=self.password,
                salary=self.salary,
            )

    def find(self, filter=None):
        if pfilter:
            return super().find(self.name_table, pfilter)
        else:
            return super().find(self.name_table)
        

    def delete(self ):
        if self.id == None:
            self.id = self.__getId(self.user_name, self.password)
        super().delete(self.name_table, id=self.id)


    def isRegisterUser(self, nameuser):
        """+ isRegisterUser(nameuser: str): bool
        """
        pass

    def singUp(self):
        pass

    
    def __str__(self):
        return ":D"


if __name__ == "__main__":
    user = UserModel(name="Pablo", pwd="1234", salary=100000) # jeje :D
    print(":) --->", str(user))