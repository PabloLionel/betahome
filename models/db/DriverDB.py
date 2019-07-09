#######################################################
# 
# DriverDB.py
# Python implementation of the Class DriverDB
# Created on:      23-jun.-2019 6:56:26
# Original author: Betacode
# reference: https://www.giacomodebidda.com/mvc-pattern-in-python-sqlite/
# 
#######################################################
from .Query import Query
import sys
import sqlite3 as sq3

class Adapter:
    def __init__(self, namedb="betahome.db"):
        self.__conn=sq3.connect(namedb)
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
    
    def __del__(self):
        self.conn.close()

# refactorizar: mover a un modulo utils.py:

# Pensando a futuro para el backend.
def scrub(name_func): # no esta probado.
    """Decorador para limpia los string de entrada
    (para evitar inyección de SQL).

    Parameters
    ----------
    all_parameters: *args

    Returns
    -------
    *args
    """
    def inner_func(*args):
        args = tuple(
            map(
                lambda a: ''.join(k for k in a if k.isalnum()) if isinstance(a, str) else a,
                args
            )
        )
        return name_func(*args)
    return inner_func

class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if not self.instance:
            self.instance = self.klass(*args, **kwds)
        return self.instance

@SingletonDecorator
class DriverDB:
    def __init__(self, db=Adapter()):
        self.__db = db
        # hacer un metodo que obtenga
        # todas las tablas y de cada tabla
        # liste sus columnas para chequear
        # las consultas.
    
    @property
    def db(self):
        return self.__db
    
    @db.setter
    def db(self, db):
        if isinstance(db, Adapter):
            self.__db = db
        else:
            raise 'Se espera un objeto adaptador de la base de datos.'

    def __parseColumns(self, columns):
        return ','.join(columns) if columns else '*'

    def selectOne(self, table_name, columns, column_compare, item):
        """Hace una consulta devolviendo un solo resultado.

        Parameters
        ----------
        table_name : str
            Nombre de la tabla.
        columns : str[]
            Lista de columnas, ej: ['id', 'name', 'password'].
            Para una lista vacia la consulta será ' select * ...'.
        column_compare : str
            Columna a comparar
        item : str
            Valor de comparación.

        Returns
        -------
        tuple
        """
        return self.runQuery(
            Query(f'''
                SELECT {self.__parseColumns(columns)}
                FROM {table_name}
                WHERE {column_compare}={item}''',
                save=False,
                get_all=False
            )
        )

    def selectAll(self, table_name, columns="*"):
        """Hace una consulta devolviendo un solo resultado.

        Parameters
        ----------
        table_name : str
            Nombre de la tabla.
        columns : str[]
            Lista de columnas, ej: ['id', 'name', 'password'].
            Para una lista vacia la consulta será ' select * ...'.

        Returns
        -------
        tuple
        """
        # a futuro, no solo limpiarlos, sino tambien
        # chequear datos de entrada:
        return self.runQuery(Query(f'SELECT {self.__parseColumns(columns)} FROM {table_name}', save=False))

    def runQuery(self, q):
        try:
            # a futuro, no solo limpiarlos, sino tambien
            # chequear datos de entrada:
            # clean_sql = self.scrub(q.sql)
            if q.many:
                c = self.db.cursor.executemany(q.sql, q.data)
            else:
                c = self.db.cursor.execute(q.sql, q.data)
            if q.save:
                self.save()
            return c.fetchall() if q.get_all else c.fetchone()
        except sq3.IntegrityError as e:
            raise '[ Error ] {}'.format(e)
        except sq3.OperationalError as e:
            raise '[ Error ] {}'.format(e)
        except sq3.ProgrammingError as e:
            raise '[ Error ] {}'.format(e)
        except: # catch *all* exceptions
            e = sys.exc_info()[0]
            raise e

    def save(self):
        self.db.conn.commit()

def main():
    pass

if __name__ == "__main__":
    main()