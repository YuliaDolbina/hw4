from EmployeeApi import EmployeeApi

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

    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active)
    
    new_id = result["id"]
    body = api.get_info(new_id)

    assert body["id"] == new_id


def test_create_employee():
    first_name = "TOM"
    last_name = "Green"
    middle_name = ""
    company_id = 4
    email = "tom@test.com"
    phone = "76786757543354"
    birthdate = "2000-12-12"
    is_active = True

    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active)

    assert result["first_name"] == first_name



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

    assert edited["last_name"] == new_last_name
    assert edited["email"] == new_email

def test_get_list_company_id():
    company_id = ["company_id"]
    body = api.get_list_company_id(company_id)
    assert len(body) > 0 

    




