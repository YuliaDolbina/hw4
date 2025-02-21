from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


class EmployeeTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        Base = declarative_base()
        session = sessionmaker(bind=self.db, expire_on_commit=False)


    def create_employee(self):
        return self.db.session().execute(text("insert into employee (fist_name, last_name, middle_name, company_id, email, phone, birthdate, is_active) values (:first_name, :last_name, :middle_name, :company_id, :email, :phone, :birthdate, :is_active)")).fetchall()
    

    def get_info(self, id):
        return self.db.session().execute(text(f"select max{id} from employee")).fetchall()
    

    def delete(self, id):
        return self.db.session().execute(text(f"delete from employee where id = {id}"))


## pytest -v hw9/test_employee_db.py
