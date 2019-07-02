from IDao import IDataAccessObject
from db import DriverDB

class DataAccessObject(IDataAccessObject):

    def __init__(self):
        self.name = "Pablo"
        print(type(self).__name__)
        # pass

    # @staticmethod
    def statusDB(self, parameter_list):
        return True
    
    def create(self):
        pass
    
    def update(self):
        pass
    
    def find(self, filter):
        pass
    
    def delete(self):
        pass

if __name__ == "__main__":
    class ExampleDAO(DataAccessObject):

        def __init__(self):
            DataAccessObject.__init__(self)
            print(type(self).__name__)
    dao = ExampleDAO()
    print("Hola ", dao.name)