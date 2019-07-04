from abc import ABC, abstractmethod

class IQuery(ABC):
    @property
    @abstractmethod
    def sql(self): return NotImplementedError

    @sql.setter
    @abstractmethod
    def sql(self, val): return NotImplementedError
    
    @property
    @abstractmethod
    def data(self): return NotImplementedError

    @data.setter
    @abstractmethod
    def data(self, val): return NotImplementedError
    
    @property
    @abstractmethod
    def many(self): return NotImplementedError

    @many.setter
    @abstractmethod
    def many(self, val): return NotImplementedError
    
    @property
    @abstractmethod
    def save(self): return NotImplementedError

    @save.setter
    @abstractmethod
    def save(self, val): return NotImplementedError
    
    @property
    @abstractmethod
    def get_all(self): return NotImplementedError

    @get_all.setter
    @abstractmethod
    def get_all(self, val): return NotImplementedError

class Query():
    """
    Defauts
    -------
        Query(data=tuple(), many=False, save=True, get_all=True)
    Parameters
    ----------
    data:
    many:
    save:
    get_all:
    
    """
    def __init__(self, sql, *args, **kwargs):
        # chequear a futuro todos los datos de entrada.
        if not isinstance(sql, str):
            raise TypeError('A "str" was expected with the query')
        self.sql=sql
        kw = list(kwargs.keys())
        self.data=kwargs.get('data') if 'data' in kw else tuple()
        self.many=kwargs.get('many') if 'many' in kw else False
        self.save=kwargs.get('save') if 'save' in kw else True
        self.get_all=kwargs.get('get_all') if 'get_all' in kw else True
