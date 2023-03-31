def rek_silnia(n):
    if n==0:
        return 1
    else:
        return n*rek_silnia(n-1)
print(rek_silnia(20))
