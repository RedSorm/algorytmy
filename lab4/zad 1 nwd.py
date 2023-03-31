# Dana jest iteracyjna wersja funkcji znajdowania NWD.

def nwd(a,b):
    while b:
        a,b =b, a%b
    return a

def nwd_r(a,b):
    if b!=0:
        return nwd_r(b,a%b)
    else:
        return a
def nwd_i(a,b):
    while b!=a:
        if a>b:


    return a




print(nwd(24,36))
print(nwd_r(24,36))
