class User:
    def __init__(self, name, surname):
    
        self.first_name = name
        self.last_name = surname

    def sayName (self):
        print("Меня зовут ", self.first_name) 

    def saySurname (self):
        print("Моя фамилия ", self.last_name)

    def sayFullname(self):
        print("Мое имя ", self.first_name, "Моя фамилия " , self.last_name)


