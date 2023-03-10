n= int(input())
dane = input().split()
print(dane)
ilep= 0
skok = 0
for i in dane:
    if i == "1":
        ilep+=1
        if skok<ilep:
            skok=ilep
    else:
        ilep=0
    print(ilep,skok)
print(skok)