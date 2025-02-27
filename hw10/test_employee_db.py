from datetime import datetime

from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")
api = EmployeeApi("http://5.101.50.27:8000")


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
    assert list(employee_from_api.values()) == list(created_employee)


def test_get_list_company_id():

    company_id = 3
    body = api.get_list_company_id(company_id)
    body_db = db.get_list_company_id(company_id)
    assert len(body) == len(body_db)


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

    assert result[1] == first_name
    assert result_api["last_name"] == result[2]


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

    assert edited["last_name"] == new_last_name
    assert edited["email"] == new_email
    assert employee_from_db[0] == employee_id
