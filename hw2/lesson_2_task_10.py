def bank(x,y):
    for each_year in range (y):
        x = (x * 1.1)

    return round(x, 2)

x = float(input ("Сумма вклада: ")) 
y = int(input ("Срок вклада: ")) 
print("ВЫ получите: " + str(bank(x,y)))     