n = int(input("podaj przypadki"))
while n>0:
    x = int(input("Podaj prędkość: "))
    y = input("Czy masz urodziny? Wpisz tak lub nie:  ")
    if y == "tak":
        if x <= 65:
            print("bez mandatu")
        elif 66<=  x <= 85:
                print("niski mandat")
        else:
                print("Wysoki mandat")
    else:
        if x <= 60:
            print("bez mandatu")
        elif 61<=  x <= 80:
                print("niski mandat")
        else:
                print("Wysoki mandat")
    n -=1ź