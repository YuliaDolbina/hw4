from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 15", "+79864358765")
phone2 = Smartphone("Apple", "iPhone 13", "+79873249876")
phone3 = Smartphone("Asus", "Zen", "+79806883298")
phone4 = Smartphone("Honor", "10", "+79083249898")
phone5 = Smartphone("Apple", "iPhone 14", "+79279874356")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)
                    
for list in catalog:
    print (f"{list.brand} - {list.model}.{list.phoneNumber}")