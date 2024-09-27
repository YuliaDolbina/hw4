from Address import Address 
from Mailing import Mailing

from_address = Address ("456542, ", "Москва, ", "Театральная, ", "1, ", "77")
to_address = Address ("410001, ", "Саратов, ", "Зеленая, ", "17, ", "551")
cost = int("1000")
track = str("546899864")
mailing1 = Mailing(to_address, from_address, cost, track)
print(f"Отправление {track} из {from_address} в {to_address} стоимостью {cost} рублей")   

