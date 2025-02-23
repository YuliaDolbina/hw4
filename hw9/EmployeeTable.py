from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class EmployeeTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.session = sessionmaker(bind=self.db, expire_on_commit=False)

    def create_employee(
            self,
            first_name,
            last_name,
            middle_name,
            company_id,
            email,
            phone,
            birthdate,
            is_active,
    ):
        with self.session() as session:
            created_employee = session.execute(
                text(
                    f"""
                    insert into employee (first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active)
                    values ('{first_name}', '{last_name}', '{middle_name}',
                    {company_id}, '{email}', '{phone}', '{birthdate}', {is_active})
                    returning id, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active
                    """
                ),
            ).fetchone()
            session.commit()

            return created_employee

    def get_info(self, id):
        return self.session().execute(text(f"select max({id}) from employee")).fetchone()

    def delete(self, id):
        return self.session().execute(text(f"delete from employee where id = {id}"))
    
    def get_list_company_id(self, company_id):
        return self.session().execute(text(f"select * from employee where company_id = {company_id}")).fetchone()

## pytest -v hw9/test_employee_db.py
