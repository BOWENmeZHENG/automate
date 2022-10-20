import numpy as np


def sort_nodes(nodes, stresses):
    sort_index = np.argsort(nodes)
    nodes_sorted_dup = [nodes[index] for index in sort_index]
    stresses_sorted_dup = [stresses[index] for index in sort_index]
    nodes_sorted, indices_unique, stresses_sorted = [], [], []
    for i, node in enumerate(nodes_sorted_dup):
        if node not in nodes_sorted:
            nodes_sorted.append(node)
            indices_unique.append(i)
    for index in indices_unique:
        stresses_sorted.append(stresses_sorted_dup[index])
    return nodes_sorted, stresses_sorted
