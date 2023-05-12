def DFS(graph, s):
    stos = []
    colors = [0] * len(graph)  # 0 - kolor biały , 1 szary ,2 czarny
    colors[s] = 1
    stos.append(s)
    while len(stos) != 0:
        u = stos[-1]
        sasiedzi = graph[u]
        stos.pop()
        for v in range(len(sasiedzi)):
            if colors[v] == 0 and sasiedzi[v] == 1:
                colors[v] = 1
                stos.append(v)
                print(u, "-->", v)
        print("Stos = ", stos)
        stos.pop(0)
        colors[u] = 2
G = [ [0, 1, 1, 1, 0, 0], # gfraf jest w prezentacji, jedynki są tam gdzie mozemy przejsc z konkretnego node'a, kazda tablica przedstawia node od 0 do 5
      [0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0]
    ]

DFS(G, 0)