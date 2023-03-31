def pisz(tekst,n):
    for i in range(n):
        print(tekst)

def pisz_rek(tekst,n):
    if n>0:
        print(tekst)
        pisz_rek(tekst,n-1)
#pisz_rek("Algorytmy",10)
def silnia_iter(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

print(silnia_iter(3))