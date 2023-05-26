# Zadanie 2.1.
# Poniżej wpisano jeden z poznanych na zajęciach algorytmów sortowania listy.
# a)	Uzupełnij poniższą funkcje dotyczące sortowania listy tak, aby działała prawidłowo,
# b)	pokaż, w jaki sposób można uruchomić tę funkcję dla elementów [13, 15, 2, 71, 8, 4, 6],
# c)	pokaż kolejne zamiany wykonywane podczas sortowania elementów,
# d)	podaj złożoność obliczeniową dla podanej funkcji sortowania.
#
#
def sortowanie(T):
    n=len(T)       # n to liczba elementów
    for i in range(n-1):
        k=i
        for j in range(i+1, n):
            if T[j] < T[k]:
                k=j
    return T
print(sortowanie())


