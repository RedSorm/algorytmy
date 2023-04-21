a=[0,0,0,0,0,0,0,0,1,1]
def divandconq(a):
    liczba_zer=0
    p= 0
    k= len(a)-1
    while p <= k:
        sr = (p+k)//2
        if a[sr] == 1:
            k =sr -1
        else:
            liczba_zer = liczba_zer+(sr-p)+1
            p = sr+1
    return liczba_zer
print(divandconq(a))
