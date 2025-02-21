import requests



class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_info(self, id):
        resp = requests.get(self.url + "/employee/info/" + str(id))

        return resp.json()

    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active):
        employee = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        resp = requests.post(self.url + "/employee/create", json=employee)

        return resp.json()

    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    def edit_employee(self, employee_id, new_last_name, new_email, new_phone):
        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"

        employee = {
            "last_name": new_last_name,
            "email": new_email,
            "phone": new_phone,
            "is_active": True,
        }
        resp = requests.patch(url_with_token, json=employee)

        return resp.json()
    

    def get_list_company_id(self, company_id):
        resp = requests.get(self.url+"/employee/list/"+ str(company_id))
        return resp.json()
    

