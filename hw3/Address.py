class Address:
    index = "000000"
    city = "город"
    street = "улица"
    building = "000"
    apart = "000"
    def __init__(self, index, city, street, building, apart):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apart = apart
    def __str__(self):
     return f"{self.city}{self.street}{self.building}"