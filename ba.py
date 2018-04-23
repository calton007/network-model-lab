import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
NUM = 50
m = 5


def f_1(x, A, B):
    return A*x + B


G = nx.random_graphs.barabasi_albert_graph(NUM, m)
nx.draw(G)
plt.show()
# plt.figure()
# degree = nx.degree_histogram(G)
# x = [1.0 * i for i in range(len(degree))]
# y = [z / float(sum(degree)) for z in degree]
# s = 0
# for i in range(len(y)):
#     s += (y[i] * (i + 1))
# print("Average Degree:", s)
# print("Average Clustering:", nx.average_clustering(G))
# try:
#     print("Average Path Length:", nx.average_shortest_path_length(G))
# except nx.exception.NetworkXError:
#     print("Graph is not connected.")
# plt.scatter(x, y, marker='.')
# # log
# plt.figure()
# # plt.loglog(x, y, linewidth=0, marker='.')
# Xi = []
# Yi = []
# for i in range(len(x)):
#     if x[i] > 0.0 and y[i] > 0.0:
#         Xi.append(np.log10(x[i]))
#         Yi.append(np.log10(y[i]))
# k, b = optimize.curve_fit(f_1, Xi, Yi)[0]
# print(k, b)
# x = [Xi[0], Xi[-1]]
# y = [k * Xi[0] + b, k * Xi[-1] + b]
# plt.plot(x, y)
# plt.scatter(Xi, Yi, color='red')
# plt.show()