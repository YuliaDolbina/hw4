empty_dict = {}


football_stats = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": ["Австралия", "Англия", "Аргентина", "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {
        "Золотой мая": "Лионель Месси",
        "Серебряный мая": "Килиан Мбаппе",
        "Золотая бутса": "Килиан Мбаппе",
        "Серебряная бутса": "Килиан Мбаппе",
        "Золотой мая": "Лионель Месси",
        "Больше всего голов": {
            "Игрок": "Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        }
    }
}


#def test_read_value():
   # count = football_stats.get("Число стран")
    #assert count == 48

def test_empty_dict():
    assert len(empty_dict) == 0

def test_write_value():
    football_stats["Число стран"] = 50
    count = football_stats.get("Число стран")
    assert count == 50

def test_write_new_value():
    football_stats["Победитель"] = "Аргентина"
    winner = football_stats["Победитель"]
    assert winner == "Аргентина"



    