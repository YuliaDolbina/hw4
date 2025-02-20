import requests
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)


def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "python"
    descr = "tests"

    result = api.create_company(name, descr)
    new_id = result["id"]   

    body = api.get_company_list()
    len_after = len(body)
    db.delete(new_id)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id


def test_get_one_company():
    name = "skypro"
    db.create(name)
    max_id = db.get_max_id()
        
    new_company = api.get_company(max_id)
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
   










## pytest hw9/test_x_clients_db.py   