# Zadanie 1.
# Dana jest wzór rekurencyjny pewnego ciągu liczbowego :
 

# a)	Zdefiniuj funkcję rekurencyjna obliczająca n-ty wyraz ciągu
# b)	Wyświetl 5 pierwszych wyrazów tego ciągu
# c)	Podaj złożoność obliczeniową dla podanego algorytmu rekurencyjnego
# Zadanie na trzy
def fun_iter(n):
    list_of_elem = []
    if n != 0:
        for i in range(n):
            n = (i-i)+ 2 * i
            list_of_elem.append(n)
    else:
        n==0
        list_of_elem.append(n)
    return list_of_elem

print(fun_iter(5))

def alg_rek(n):
    list_of_elem = []
    n = (n-1) + 2 * n
    list_of_elem.append(n)
    alg_rek(n)
    return n, list_of_elem
# print(alg_rek(0))
def rekur(n):
    if n < 1:
        return 1
    else:
        result = 2 * n + rekur(n-1)
        print(f"rekur({n}) = {result}")
        return result

print(rekur(5))
# złożoność liniowa
