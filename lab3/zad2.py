#Napisz program, który mnoży tablicę dwuwymiarową przez dowolna liczbę podaną z klawiatury.
import random
def createtwodimarray2(m,n):
   lista=[[random.randint(-20,50) for i in range(n)] for j in range(m)]
   return lista



macierz=createtwodimarray2(10,10)

def multlistbynumber(lista,liczba):
    for a in range(len(lista)):
        for j in range(len(lista[a])):
            lista[a][j]=[lista[a][j]*liczba for i in lista[a]]
    return lista
print(multlistbynumber(macierz,3))
