# Napisz program, który znajduje pozycję najmniejszego elementy listy(tablicy). Program wyświetla pozycję i wartość najmniejszego elementu listy.
import random
lista=[]
for i in range(20):
    lista.append(random.randrange(1,100))
print(lista)
def findminelement(lista):
    min_= lista[0]
    for i in lista:
        if i<min_:
            min_=i
    return min_
def findminpositon(lista):
    minpoz=0
    for i in range(1,len(lista)):
        if lista[i]<lista[minpoz]:
            minpoz=i
    return minpoz
print(f'Najmniejszy element listy to: {findminelement(lista)}')
print(f'Pozycja najmniejszego elementu listy to: {findminpositon(lista)+1}')


