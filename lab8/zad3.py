`import networkx as nx
import matplotlib.pyplot as plt
x=["Maciek","Marysia","Marta",   "Magda","Marek"]
y=["0",         "1",     "2",     "3",     "4"  ]
G = nx.DiGraph()
## G = nx.MultiDiGraph()
## G = nx. Graph()
nodes=["0", "1", "2", "3"]
G.add_nodes_from(nodes)
G.add_edge("0","1")
G.add_edge("0","2")
G.add_edge("0","3")
G.add_edge("4","1")
G.add_edge("4","3")
G.add_edge("1","2")
G.add_edge("2","1")
print(G.nodes())
print(G.edges())
nx.draw(G, with_labels = True)
plt.savefig("simple_path.png") # zapis do pliku png
plt.show() # wyświetlenie