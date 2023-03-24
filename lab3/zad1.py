# Napisz program, który losuje 100 liczb całkowitych z przedziału -20, 50 i zapisuje je do tablicy dwuwymiarowej 10x10, następnie program znajdują maksymalną wartość w tej tablicy.
import random
def createtwodimarray(m,n):
   lista =[]
   for i in range(m):
      pom=[]
      for j in range(n):
         pom.append(random.randint(-20,50))
      lista.append(pom)
   return lista
def printtwodimarray(lista):
   for i in range(len(lista)):
      for j in range(len(lista[i])):
         print(lista[i][j], end="\t")
      print()

def createtwodimarray2(m,n):
   lista=[[random.randint(-20,50) for i in range(n)] for j in range(m)]
   return lista


macierz=createtwodimarray(10,10)
printtwodimarray(macierz)
def maxing(lista):
   myMax = lista[0][0]
   for i in range(len(lista)):
      for j in range(len(lista[i])):
         if lista[i][j]>myMax:
            myMax = lista[i][j]
   return myMax
print(maxing(macierz))


def findpositionmaxelem(lista):
   myMax = lista[0][0]
   wiersz = 0
   kolumna = 0
   for i in range(len(lista)):
      for j in range(len(lista[i])):
         if lista[i][j]>myMax:
            myMax=lista[i][j]
            wiersz=i
            kolumna=j
   return myMax,wiersz,kolumna
wynik=findpositionmaxelem(macierz)
print(f'Maksymalny elemeny w liscie to {wynik[0]}  jest w wierszu {wynik[1]+1} i kolumnie {wynik[2]+1} ')




