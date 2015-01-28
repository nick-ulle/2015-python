'''
We'd like to do some network analysis of a body of text.

Let's build a graph where the nodes are names and the 
weight of the edge is the number of times that the two names
appear in the same sentence together.
'''

from pprint import pprint
import itertools

import matplotlib.pyplot as plt
import networkx as nx

names = {'Clark', 'Yeji', 'Dongmin', 'Kevin Bacon'}

pairs = set(itertools.combinations(names, 2))


def together(namepair, string):
    '''
    Return True if all elements of names are in string
    '''
    return all(n in string for n in namepair)


paragraph = '''
Clark and Yeji are married. Yeji's cousin is Dongmin.
Everybody likes Kevin Bacon. Dongmin and Clark play ping pong.
'''

# Look through the paragraph and add names that appear in the
# same sentence, and add an edge to the graph

G = nx.Graph()
G.add_nodes_from(names)

sentences = paragraph.split('.')

for s in sentences:
    for namepair in pairs:
        if together(namepair, s):
            G.add_edge(*namepair)

nx.draw_networkx(G, node_size=1500, alpha=0.2)
plt.show()

# We can now pull out an adjacency matrix
adj = nx.adjacency_matrix(G)
adj = adj.todense()

print(list(nx.connected_components(G)))
print(nx.algorithms.triangles(G))
