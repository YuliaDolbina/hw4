import requests

base_url = "http://5.101.50.27:8000"

def get_company_list(params_to_add = None):
    resp = requests.get(base_url + '/company/list', params=params_to_add)
    return resp.json()

def test_get_companies():
    body = get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    full_list = get_company_list()
    filtered_list = get_company_list(params_to_add={"active": "true"})

    assert len(full_list) > len(filtered_list)

def test_add_new():
    body = get_company_list()
    len_before = len(body)

    company = {
        "name": "python",
        "description": "requests"
    }

    resp = requests.post(base_url+"/company/create", json=company)

    assert resp.status_code == 201

    body = get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1


