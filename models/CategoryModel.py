#######################################################
# 
# CategoryModel.py
# Python implementation of the Class CategoryModel
# Created on:      10-jul.-2019 23:00:39
# Original author: Betacode
# 
#######################################################
try:
    from .dao import DataAccessObject
    from .db.Query import Query
except:
    from dao import DataAccessObject 
    from db.Query import Query

class CategoryModel(DataAccessObject):
    def __init__(self, id, name, total, *args, **kwargs):
        DataAccessObject.__init__(self)
        self.init()
        self.id = id
        self.name = name
        self.total = total

    def name_table():
        return 'category'

    def init(self):
        self.driver.runQuery(
            Query(
                f"""
                CREATE TABLE IF NOT EXISTS {CategoryModel.name_table()} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(30) UNIQUE,
                    total float
                )
                """
            )
        )

    def create(self):
        if self.id == None:
            res = super().create(
                CategoryModel.name_table(),
                # id=...,                 # POR SER AUTOINCREMENTAL.
                name=self.name,
                total=self.total,
            )
            print(res)
        return res

    def update(self):
        res = super().update(
            CategoryModel.name_table(),     # nombre de la tabla
            'id',                       # columna a comparar
            self.id,                    # item a comparar
            name=self.name,
            total=self.total,
        )
        print(res)
        return res

    def find(self, pfilter=None):
        if pfilter:
            return super().find(CategoryModel.name_table(), pfilter)
        else:
            return super().find(CategoryModel.name_table())

    def delete(self ):
        if self.id != None:
            return super().delete(CategoryModel.name_table(), id=self.id)

if __name__ == "__main__":
    category = CategoryModel(name="servicios", total=0)
