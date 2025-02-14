import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url


    def get_info(self, id):
        resp = requests.get(self.url+"/employee/info/"+str(id))
        return resp.json()["id"]    
    

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
        resp = requests.post(self.url+"/employee/create", json=employee)
        return resp.json()
    

    def get_token(self, user = 'harrypotter', password = 'expelliarmus'):
        creds = {
            'username': user, 
            'password': password
            }
        resp = requests.post(self.url +'/auth/login', json=creds)
        return resp.json()["user_token"]
    

    def edit_employee(self,new_id, new_first_name, new_email):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"

        employee = {
            "first_name": new_first_name,
            "email": new_email
            }
        resp = requests.patch(url_with_token, json=employee)
        return resp.json()    


