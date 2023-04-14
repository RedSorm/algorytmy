# Zaproponuj rekurencyjny algorytm przeliczania liczby w dowolnym systemie od 2 do 9 na liczbę binarną.
def bin_to_dec_horner(tekst,x):
    n = len(tekst)
    wynik = ord(tekst[0])-48 #odejmuje 48 z zamiany z kodu ascii
    for i in range(1,n):
        wynik = wynik * x+ ord(tekst[i])-48
    return wynik
print(bin_to_dec_horner('101',2))

def bin_to_hex_horner(tekst,x):
    lista= '0123456789ABCDEF'
    wynik =lista.find(tekst[0])
    n = len(tekst)
    for i in range(1,n):
        wynik = wynik * x+ lista.find((tekst[i]))
    return wynik
print(bin_to_hex_horner("C2",16))

def bin_to_dec_horner_rek(tekst,x):
    if len(tekst)==1:
        return ord(tekst[0])-48
    else:
        return x * bin_to_dec_horner_rek(tekst[0:len(tekst)-1],x)+ord(tekst[len(tekst)-1])-48
print(bin_to_dec_horner_rek("101",2))

def horner_rek_16(tekst,x):
    lista= '0123456789ABCDEF'
    if(len(tekst)==1):
        return lista.find(tekst[0])
    else:
        return x*horner_rek_16(tekst[0:len(tekst)-1],x) + lista.find(tekst[len(tekst)-1])
print(horner_rek_16("C2",16))