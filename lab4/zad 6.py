#Zaproponuj rekurencyjny algorytm szybkiego potęgowania.
# def potega(a,b):
#     if (b==1):
#         return a
#     elif b==0:
#         return 1
#     else:
#         return a*potega(a,b-1)
#
def pot_rek(a,b):
    if b==1:
        return a
    elif b%2==0:
        s = pot_rek(a,int(b/2))
        return s*s
    else:
        return a * pot_rek(a,b-1)
print(pot_rek(2,5))
