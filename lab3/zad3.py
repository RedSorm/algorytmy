# Napisz program, który mnoży dwie tablice n -wymiarowe przez siebie.
# Jakie muszą być spełnione założenia przy mnożeniu dwóch tablic dwuwymiarowych?
# Jaka jest złożoność obliczeniowa takiego programu?
import random
def createtwodimarray2(m,n):
   lista=[[random.randint(-20,50) for i in range(n)] for j in range(m)]
   return lista
a = createtwodimarray2(5,4)
b = createtwodimarray2(4,5)
def mulmatrix(m1,m2):
   wm1 = len(m1)
   km1 = len(m1[0])
   wm2 = len(m2)
   km2 = len(m2[0])
   if wm1==km2 and km1==wm2:
      m3 =[]
      for i in range(wm1):
         pom =[]
         for j in range(len(wm1)):
            for c in range(km2):
               w+=m1[j][i][k][c]*[m2][c][j]
            pom.append(w)
         m3.append(pom)

   return m3