import networkx as nx
import matplotlib.pyplot as plt
import random
import math
NUM = 500
p = 0.2


# G(n,m)
G = nx.Graph()
m = math.floor(NUM * (NUM - 1)/2 * p) * 2
for i in range(NUM):
    G.add_node(i)
count = 0
while count < m:
    i = math.floor(random.random() * (NUM - 0) + 0)
    j = math.floor(random.random() * (NUM - 0) + 0)
    if i != j and not G.has_edge(i, j):
        G.add_edge(i, j)
        count += 1
# nx.draw(G, pos=nx.circular_layout(G))
plt.show()
degree = nx.degree_histogram(G)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
s = 0
for i in range(len(y)):
    s += (y[i] * (i + 1))
# print("Average Degree:", s)
# print("Average Clustering:", nx.average_clustering(G))
# try:
#     print("Average Path Length:", nx.average_shortest_path_length(G))
# except nx.exception.NetworkXError:
#     print("Graph is not connected.")
plt.figure()
plt.scatter(x, y, marker='.')
# log
plt.figure()
plt.loglog(x, y, linewidth=0, marker='.')
plt.show()
