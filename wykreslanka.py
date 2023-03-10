n= int(input('ilosc liczb: '))
dane = list(map(int,input('liczby po spacji: ').split()))
print(dane)
liczba = 1
wykres = 0
for i in dane:
    if i ==  liczba:
        liczba+=1
    else:
        wykres+=1
print(wykres)
