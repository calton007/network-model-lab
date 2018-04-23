import networkx as nx
import matplotlib.pyplot as plt
import random
import math
NUM = 282
p = 7.35 / 281

# G = nx.random_graphs.erdos_renyi_graph(NUM, p)
# G(n,p)
G = nx.Graph()
for i in range(NUM):
    G.add_node(i)
for i in range(NUM):
    for j in range(NUM):
        if i != j and not G.has_edge(i, j):
            if random.random() < p:
                G.add_edge(i, j)
# nx.draw(G, pos=nx.circular_layout(G))
plt.show()
degree = nx.degree_histogram(G)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
s = 0
for i in range(len(y)):
    s += (y[i] * (i + 1))
print("Average Degree:", s)
print("Average Clustering:", nx.average_clustering(G))
try:
    print("Average Path Length:", nx.average_shortest_path_length(G))
except nx.exception.NetworkXError:
    print("Graph is not connected.")
plt.figure()
plt.scatter(x, y, marker='.')
# log
plt.figure()
plt.loglog(x, y, linewidth=0, marker='.')
plt.show()
