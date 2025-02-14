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

    body = api.get_info()
    new_id = result["id"]
    
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
    id = 126
    api.get_info(id)

    new_first_name = "Cinderella"
    new_email = "cindi@test.com"

    edited = api.edit_employee(id, new_first_name, new_email)

    assert edited["first_name"] == new_first_name
    assert edited["email"] == new_email


