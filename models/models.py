try:
    from models.dao import DataAccessObject
    from models.db.DriverDB import DriverDB
    from models.db.Query import Query
    from models.UserModel import UserModel
    from models.CategoryModel import CategoryModel
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
        # nos aseguramos de crar la tabla
        firstCategory = CategoryModel(name="Servicios", total=0)
        # instanciamos las demas categorias:
        categories += [
            firstCategory,
            CategoryModel(name="Salud", total=0),
            CategoryModel(name="Inmuebles", total=0),
            CategoryModel(name="Alimentos", total=0),
            CategoryModel(name="Otros", total=0),
        ]
        # consultamos en la base de datos si estan guardadas
        allCategories = self.driver.selectAll(CategoryModel.name_table())
        if not allCategories:
            # las cargamos a la base de datos:
            for c in categories:
                print(f"cargando categoria: {c.name}")
                c.create()
        
        allCategories = self.driver.selectAll(CategoryModel.name_table())

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