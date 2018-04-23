import networkx as nx
import matplotlib.pyplot as plt
NUM = 282
p = 0.055
c = 14

G = nx.random_graphs.watts_strogatz_graph(NUM, c, p)
nx.draw(G, pos=nx.circular_layout(G))
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
