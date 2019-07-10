try:
    from models.dao import DataAccessObject
    from models.db.DriverDB import DriverDB
    from models.db.Query import Query
    from models.UserModel import UserModel
except:
    from dao import DataAccessObject
    from db.DriverDB import DriverDB
    from db.Query import Query
    from UserModel import UserModel
    from CategoryModel import CategoryModel
    
class Model:
    driver = DriverDB()
    def __init__(self):
        self.user = self.getUser()
        self.categories = self.getCategories()
    
    def getCategories(self):
        categories = list()
        if self.existingTable(CategoryModel.name_table()):
            allCategories = self.driver.selectAll(CategoryModel.name_table())
            for c in allCategories:
                categories.append(CategoryModel(*c))
        else:
            firstCategory = CategoryModel(id=1, name="Servicios", total=0)
            categories + [
                firstCategory,
                CategoryModel(id=2, name="Salud", total=0),
                CategoryModel(id=3, name="Inmuebles", total=0),
                CategoryModel(id=4, name="Alimentos", total=0),
                CategoryModel(id=5, name="Otros", total=0),
            ]
            for c in categories:
                c.create()
        return categories
    
    def getUser(self):
        if not self.existingTable(UserModel.name_table()):
            return None
        else:
            allUser = self.driver.selectAll(
                UserModel.name_table(),
                ['user_name', 'password', 'salary']
            )
            return UserModel(*allUser[-1])
            
    def existingTable(self, name_table):
        resultQuery = self.driver.runQuery(Query(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name_table}';",
            get_all=False,
            save=False
        ))
        return bool(resultQuery)
        

def main():
    print(UserModel.name_table())
    m = Model()

if __name__ == "__main__":
    main()