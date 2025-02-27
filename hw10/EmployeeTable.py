import allure
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class EmployeeTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.session = sessionmaker(bind=self.db, expire_on_commit=False)

    @allure.step("db.Создать сотрудника")
    def create_employee(
            self,
            first_name : str,
            last_name : str,
            middle_name : str,
            company_id : int,
            email : str,
            phone : int,
            birthdate : int,
            is_active : bool,
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

    @allure.step("db.Получить инфрмацию по {id} сотрудника")
    def get_info(self, id):
        return self.session().execute(text(f"select max({id}) from employee")).fetchone()

    @allure.step("db.Удалить сотрудника")
    def delete(self, id):
        return self.session().execute(text(f"delete from employee where id = {id}"))
    
    @allure.step("db.Получить список сотрудников по {company_id} компании")
    def get_list_company_id(self, company_id):
        return self.session().execute(text(f"select * from employee where company_id = {company_id}")).fetchall()


