import requests
from CompanyApi import CompanyApi

api = CompanyApi("http://5.101.50.27:8000")

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={"active": "true"})

    assert len(full_list) > len(filtered_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "python"
    descr = "tests"

    result = api.create_company(name, descr)
    new_id = result["id"]   

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id


def test_get_one_company():
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"] 
    
    new_company = api.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr


def test_edit():
    name = "company to edit"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"] 

    new_name = "edited company"
    new_descr = "__upd__"
    edited = api.edit_company(new_id, new_name, new_descr)

    assert edited["name"] == new_name
    assert edited["description"] == new_descr


def test_delete():
    name = "company to delete"
    result = api.create_company(name)
    new_id = result["id"] 

    api.delete(new_id)

    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'
       







