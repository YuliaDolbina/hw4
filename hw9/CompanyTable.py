from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


class CompanyTable:

    scripts = {
        "select": "select * from company",
        "select_active": "select * from company where \"is_active\" = true",
        "delete": "delete from company where id = :id_to_delete",
        "insert": "insert into company (\"name\") values (:new_name)",
        "select max id": "select max(id) from company"
    }


    def __init__(self, connection_string):
        self.db = create_engine(connection_string)


    def get_companies(self):
        return self.db.execute(self.scripts["select"]).fetchall()


    def get_active_companies(self):
        return self.db.execute(self.scripts["select_active"]).fetchall()
    
    def delete(self, id):
        sql = text(self.scripts["delete"])
        return self.db.execute(sql, id_to_delete=id)
    
    def create(self, name):
        self.db.execute(self.scripts["insert"], new_name=name).fetchall()

    def get_max_id(self):
        return self.db.execute(self.scripts["select max id"]).fetchall()


        



