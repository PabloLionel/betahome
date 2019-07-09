try:
    from models.dao import DataAccessObject
    from models.UserModel import UserModel
    from models.db.DriverDB import DriverDB
    from models.db.Query import Query
except:
    from dao import DataAccessObject
    from UserModel import UserModel
    from db.DriverDB import DriverDB
    from db.Query import Query
    
class Model:
    driver = DriverDB()
    def __init__(self):
        self.user = self.getUser()
    
    def getUser(self):
        if not self.existingTable(UserModel.name_table()):
            print('tu tabla no existe')
            return None
        else:
            allUser = self.driver.selectAll(
                UserModel.name_table(),
                ['name_user', 'password', 'salary']
            )
            return UserModel(*allUser[-1])
            
    def existingTable(self, tname_table):
        self.driver.runQuery(Query(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tname_table}';",
            get_all=False,
            save=False
        ))

def main():
    print(UserModel.name_table())
    m = Model()

if __name__ == "__main__":
    main()