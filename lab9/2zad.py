def BFS_for_list(lista, s):
    Q = []
    colors = [0] * len(lista)  # 0 - kolor biały , 1 szary ,2 czarny
    colors[s] = 1
    Q.append(s)
    while len(Q) != 0:
        u = Q[0]
        sasiedzi = lista[u]
        for v in sasiedzi:
            if colors[v] == 0:
                colors[v] = 1
                Q.append(v)
                print(u, "-->", v)
        print("Q = ", Q)
        Q.pop(0)
        colors[u] = 2

L=[ [1,2,3],
    [4],
    [1],
    [5],
    [],
    [2,4],
]
BFS_for_list(L,0)
