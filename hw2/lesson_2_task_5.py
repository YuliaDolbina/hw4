def month_to_season (a):
    if a == 1 or a == 2 or a == 12:
        return ("winter")
    elif a == 3 or a == 4 or a == 5:
        return ("spring")
    elif a == 6 or a == 7 or a == 8:
        return ("summer")
    elif a == 9 or a == 10 or a == 11:
        return ("autumn")
    else:
        return ("please, enter the correct number")
    
print(month_to_season(int(input("Enter the number of the month: "))))




