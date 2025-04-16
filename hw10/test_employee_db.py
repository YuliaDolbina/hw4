from datetime import datetime
import allure
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")
api = EmployeeApi("http://5.101.50.27:8000")

@allure.title("Получение информации о сотруднике {first_name}  {last_name}")
@allure.description("Получение информации о сотруднике")
@allure.feature("READ")
@allure.severity("Trivial")
def test_to_get_info():
    first_name = "Snow"
    last_name = "White"
    middle_name = ""
    company_id = 3
    email = "snowwhite@test.com"
    phone = "87767867"
    birthdate = "2000-10-10"
    is_active = True

    created_employee = db.create_employee(
        first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active
    )
    employee_from_api = api.get_info(created_employee[0])
    db.delete(created_employee[0])

    employee_from_api["birthdate"] = datetime.strptime(employee_from_api["birthdate"], "%Y-%m-%d").date()
    with allure.step("Сравнить списки"):
        assert list(employee_from_api.values()) == list(created_employee)

@allure.title("Получение списка сотрудников по {company_id} компании")
@allure.description("Получение списка сотрудников по id компании")
@allure.feature("READ")
@allure.severity("Trivial")
def test_get_list_company_id():

    company_id = 3
    body = api.get_list_company_id(company_id)
    body_db = db.get_list_company_id(company_id)
    with allure.step("Сравнить длину списков"):
        assert len(body) == len(body_db)

@allure.title("Создание нового сотрудника")
@allure.description("Добавление сотрудника и информации о нем")
@allure.feature("CREATE")
@allure.severity("Major")
def test_create_employee():
    first_name = "TOM"
    last_name = "Green"
    middle_name = ""
    company_id = 4
    email = "tom@test.com"
    phone = "76786757543354"
    birthdate = "2000-12-12"
    is_active = True

   
    result = db.create_employee(first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active)
    new_id = result[0]
    result_api = api.get_info(new_id)

    db.delete(new_id)
    with allure.step("Имя и фамилия по апи и из бд совпадают"):
        assert result[1] == first_name
        assert result_api["last_name"] == result[2]

@allure.title("Редактирование информации о сотруднике {first_name}  {last_name}")
@allure.description("Внесение изменений в информацию о сотруднике")
@allure.feature("UPDATE")
@allure.severity("Trivial")
def test_edit_employee():
    first_name = "TOM"
    last_name = "Green"
    middle_name = ""
    company_id = 4
    email = "tom@test.com"
    phone = "76786757543354"
    birthdate = "2000-12-12"
    is_active = True

    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active)
    employee_id = result["id"]
    new_last_name = "Cinderella"
    new_email = "cindi@test.com"

    edited = api.edit_employee(employee_id, new_last_name, new_email, phone)

    employee_from_db = db.get_info(employee_id)
    db.delete(employee_id)
    with allure.step("Сравнить информацию из бд и по апи"):
        assert edited["last_name"] == new_last_name
        assert edited["email"] == new_email
        assert employee_from_db[0] == employee_id

###comments