'''
Building a graph of characters from the novel War and Peace
'''

import re
from itertools import combinations
from collections import Counter

import matplotlib.pyplot as plt
import networkx as nx


namepattern = re.compile(r'''
        (?<![\.\?!]\s)   # Not the end of a sentence
        [A-Z]           # single uppercase letter
        [a-z]{3,}       # at least 3 lowercase letters
''', flags=re.VERBOSE)

wordpattern = re.compile(r"[\s']")

sentpattern = re.compile(r"[\.\?!']")

def getpairs(sentence, nameset):
    '''
    Return all the pairs of words in a sentence
    '''
    words = set(wordpattern.split(sentence))
    # All the names that appear in the sentence
    found = words.intersection(nameset)
    return combinations(found, 2)

def heavynodes(G, n=10):
    '''
    Return a subgraph of the n nodes with the largest weights
    '''
    wt = lambda x: x[1]['weight']
    w = sorted(G.node.items(), key = wt, reverse=True)
    return G.subgraph((x[0] for x in w[:n]))


if __name__ == '__main__':

    with open('/Users/clark/data/warandpeace.txt') as f:
        text = f.read()

    allnames = set(namepattern.findall(text))

    G1 = nx.Graph()

    for name in allnames:
        G1.add_node(name, weight=text.count(name))

    G = heavynodes(G1, n=30)
    G.remove_nodes_from('That There They This Well What When \
            Princes'.split(' '))
    bignames = set(G.node.keys())

    # First add all the edges with 0 weight
    sentences = sentpattern.split(text)
    for s in sentences:
        nodewt = ((a, b, 0) for a, b in getpairs(s, bignames))
        G.add_weighted_edges_from(nodewt)

    # Then add all the weights
    for s in sentences:
        for a, b in getpairs(s, bignames):
            G[a][b]['weight'] += 1

    # Drawing
    nodesizes = [2 * x['weight'] for x in G.node.values()]
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=nodesizes, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Add lines for 30, 10
    # Would have been cool to do a more continuous version here
    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 30]
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 10]

    nx.draw_networkx_edges(G, pos, edge_color='g', alpha=0.05)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, edge_color='g',
            alpha=0.3)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, edge_color='b', 
            alpha=0.6, width=2)

    plt.axis('off')
    plt.savefig('wpgraph.pdf')
