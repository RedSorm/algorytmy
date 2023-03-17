n = int(input())
temp = input().split()
x = int(input())
k = 0
k_lista = []
z = 0
for i in temp:
    if int(i) == x:
        k += 1
        k_lista.append(z + 1)
    z += 1
print(k, k_lista)