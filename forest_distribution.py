import numpy as np
import igraph as ig
from collections import Counter
from scipy.optimize import curve_fit


def to_graph(A : np.array):
    h = len(A)
    w = len(A[0])
    edges = []
    node_counter = 0
    for i in range(h):
        for j in range(w):
            if j != w-1:
                if A[i,j] == A[i,j+1] == 1: 
                    edges.append([node_counter , node_counter + 1])
            if i != h-1:
                if A[i,j] == A[i+1,j] == 1:
                    edges.append([node_counter , node_counter + h])
            if j != w-1 and i != h-1:
                if A[i,j] == A[i+1,j+1] == 1:
                    edges.append([node_counter , node_counter + h+1])
            if j != 0 and i != h-1:
                if A[i,j] == A[i+1,j-1] == 1:
                    edges.append([node_counter , node_counter + h-1])
            
            
            node_counter += 1
    return ig.Graph(n = node_counter , edges = edges)

def hole_distribution(g, bins =10):
    components = g.components()
    sizes = np.array(components.sizes())
    sizes = sizes[sizes>1] # not counting cluster made of one elementent
    return sizes

def powerlaw(x, m, c):
    return x**m * c

def fit(distribution, func):
    c = Counter(distribution)
    y = list(c.keys())
    X = list(c.values())    
    opt, _ = curve_fit(func, X, y)
    return opt
    
    
