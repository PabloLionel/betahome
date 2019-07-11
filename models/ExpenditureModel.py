#######################################################
# 
# ExpenditureModel.py
# Python implementation of the Class ExpenditureModel
# Created on:      10-jul.-2019 20:00:39
# Original author: Betacode
# 
#######################################################
from datetime import datetime
try:
    from .dao import DataAccessObject
    from .db.Query import Query
except:
    from dao import DataAccessObject 
    from db.Query import Query

class ExpenditureModel(DataAccessObject):
    
    def __init__(self, name, expenditure, estate="a pagar", idexpenditure = None, idcategory=5, *args, **kwargs):
        DataAccessObject.__init__(self)
        self.init()
        self.idcategory = idcategory
        self.idexpenditure = idexpenditure
        self.name = name
        self.estate = estate # pagado / a pagar
        self.expenditure = expenditure
        self.date = self.now()

    def name_table():
        return 'expenditure'

    def init(self):
        self.driver.runQuery(
            Query(
                f"""
                CREATE TABLE IF NOT EXISTS {ExpenditureModel.name_table()} (
                    id	                            INTEGER DEFAULT 5,
                    idexpenditure	                INTEGER,
                    name	                        TEXT NOT NULL,
                    expenditure	                    FLOAT NOT NULL,
                    estate	                        TEXT,
                    date	                        TEXT,
                    PRIMARY KEY(id,idexpenditure),
                    FOREIGN KEY(id)                 REFERENCES category(id) ON UPDATE SET DEFAULT
                );
                """
            )
        )

    def create(self):
        res = super().create(
            ExpenditureModel.name_table(),
            idcategory=self.id,
            # idexpenditure=...,    # POR SER AUTOINCREMENTAL.
            name=self.name,
            estate=self.estate,
            expenditure=self.expenditure,
            date=self.date
        )
        _, self.idexpenditure, *e = super().lastRegister(ExpenditureModel.name_table())
        print(self.idexpenditure)
        return res

    def update(self):
        if self.idexpenditure != None:
            return super().updateWithCompositeKey(
                ExpenditureModel.name_table(),
                {'id': self.idcategory, 'idexpenditure': self.idexpenditure},
                name=self.name,
                estate=self.estate,
                expenditure=self.expenditure,
                date=self.date
            )

    def find(self, pfilter=None):
        if pfilter:
            return super().find(ExpenditureModel.name_table(), pfilter)
        else:
            return super().find(ExpenditureModel.name_table())

    def delete(self):
        if self.id != None and self.idexpenditure != None:
            return super().deleteWithCompositeKey(
                ExpenditureModel.name_table(),
                {'id':self.id, 'idexpenditure': self.idexpenditure}
            )
    
    def getAllRegisters(self):
        return self.driver.selectAll(ExpenditureModel.name_table())

    def now(self):
        """
        Este metodo obtiene la fecha actual (YYYY-MM-DD).

        see
        ---
        https://stackoverflow.com/questions/29900785/inserting-datetime-into-a-sqlite-database
        http://www.numericalexpert.com/blog/sqlite_blob_time/sqlite_time_etc.html
        """
        return datetime.now().strftime("%B %d, %Y %I:%M%p")