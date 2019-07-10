from sqlite3 import InternalError
try:
    from .IDao import IDataAccessObject
    from .db.DriverDB import DriverDB, sq3
    from .db.Query import Query
except:
    from IDao import IDataAccessObject
    from db.DriverDB import DriverDB
    from db.Query import Query

class DataAccessObject(IDataAccessObject):
    def __init__(self, drive=DriverDB()): # inyectamos un driver db
        self.driver = drive

    def checkTable(self, table_name):
        exists_table = self.driver.runQuery(
            Query(
                f'SELECT EXISTS(SELECT name FROM sqlite_master WHERE type="table" AND name="{table_name}" LIMIT 1)',
                save=False,
                get_all=False
            )
        )[0]
        if not exists_table:
            raise InternalError('The table name does not exist.')

    def create(self, table_name, *args, **kwargs): # cambiar por insert_crreate.
        self.checkTable(table_name)
        return self.driver.runQuery(
            Query(
                f'INSERT INTO {table_name} (' + ','.join(kwargs.keys()) + ') VALUES (' + ','.join(['?' for _ in kwargs]) + ')',
                data=tuple(kwargs.values()),
                get_all=False,
                save=True
            )
        )
    
    def update(self, table_name, column_compare, item, *args, **kwargs):
        self.checkTable(table_name)
        return self.driver.runQuery(
            Query(
                f'UPDATE {table_name} SET ' + ','.join([k + '=?' for k in kwargs]) + f' WHERE {column_compare}={item}',
                data=tuple(kwargs.values()),
                get_all=False
            )
        )
    
    def find(self, table_name, pfilter=lambda *a: True):
        self.checkTable(table_name)
        return list(
            filter(
                pfilter,
                self.driver.selectAll(table_name)
            )
        )
    
    def delete(self, table_name, *args, **kwargs):
        self.checkTable(table_name)
        for k, v in kwargs.items():
            column=k
            item=v
            break
        return self.driver.runQuery(
            Query(
                f'DELETE FROM {table_name} WHERE {column}=?',
                data=(item,),
                save=True,
                get_all=False
            )
        )


if __name__ == "__main__":
    # prueba objeto query
    table_name = "cualquiera"
    column = "otra"
    item = 1
    q = Query(
                f'DELETE FROM {table_name} WHERE {column}=?',
                data=(item,),
                save=False,
                many=True,
                get_all=False
            )
    # print(q.__dict__)
    # demo:
    class DemoDAO(DataAccessObject):
        def __init__(self, user_name, password, salary, *args, **kwargs):
            DataAccessObject.__init__(self)
            self.init()
            self.user_name = user_name
            self.password = password
            self.salary = salary
            self.id = self.__getId(user_name, password)

        @property
        def name_table(self):
            return 'user'

        def __getId(self, user_name, password):
            res = self.driver.selectAll(
                self.name_table,
                ['id','user_name', 'password']
            )
            id = None
            for r in res:
                id, _, pwd = r
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
                    CREATE TABLE IF NOT EXISTS {self.name_table}(
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        user_name VARCHAR (20) NOT null UNIQUE,
                        password VARCHAR (16) NOT null,
                        salary FLOAT
                    )
                    """
                )
            )
        def create(self):
            if self.id == None:
                super().create(self.name_table,
                    # id='rowid', POR SER AUTOINCREMENTAL.
                    user_name=self.user_name,
                    password=self.password,
                    salary=self.salary,
                )
                self.id = self.__getId(self.user_name, self.password)

        def update(self):
            if self.id == None:
                self.create()
            else:
                super().update(self.name_table,'id', self.id, 
                    user_name=self.user_name,
                    password=self.password,
                    salary=self.salary,
                )
        
        def find(self, pfilter=None):
            if pfilter:
                return super().find(self.name_table, pfilter)
            else:
                return super().find(self.name_table)
        
        def delete(self):
            if self.id == None:
                self.id = self.__getId(self.user_name, self.password)
            super().delete(self.name_table, id=self.id)
        
        def show(self):
            print(self.__dict__)

    def myFiltro(unaTupla):
        # print(unaTupla)
        _, name, _, _ = unaTupla
        if name == 'Pablo':
            return False
        else:
            return True
    
    user1 = DemoDAO('Pablo', '123456', 10000.55)
    user2 = DemoDAO('Yhael', '654321', 20000.00)
    user3 = DemoDAO('Nahuel', '321654', 1000.50)
    user1
    print()
    user1.checkTable('user')
    user1.show()

    print()
    user1.create()
    user2.create()
    user3.create()
    user1.show()

    print()
    
    print("Reultado del  Filtro: ", user1.find(myFiltro))

    print()
    
    user1.user_name = 'Lionel'
    user1.update()
    user1.show()
    print()

    print(user1.driver.selectAll(user1.name_table))
    user1.delete()
    print(user1.driver.selectAll(user1.name_table))