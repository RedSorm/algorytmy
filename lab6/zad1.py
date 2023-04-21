# Dany jest uporządkowany ciąg liczb (od najmniejszej do największej) umieszczony w liście. Stosując metodę "dziel i zwyciężaj"
# ułóż algorytm wyszukiwania pozycji danej liczby w tym ciągu.
# muszą być posortowane
# WERSJA ITERACYJNA
a = [ 3 , 7 , 21 , 31 , 35 , 45 , 51 , 60 ]
def binary_search(a,elem):
    p = 0
    k = len(a)-1
    while(p <= k):
        sr =(p+k)//2
        if a[sr]==elem:
            return sr
        elif a[sr]<elem:
            p = sr+1
        else:
            k=sr-1
    return False
print(binary_search(a,3))
 # WERSJA REKURENCYJNA
def rek_binary_search(a,elem,p,k):
    sr = (p + k) // 2
    if p > k:
        return False
    if a[sr] == elem:
        return sr
    if a[sr] > elem:
        return rek_binary_search(a,elem,0,sr-1)
    else:
        return rek_binary_search(a,elem,sr+1,k)
print(rek_binary_search(a,51,0,len(a)-1))
