import pandas as pd


def read_stresses(filename):
    nodes, stresses = [], []
    with open(filename) as f_stress:
        # when to start reading data
        while True:
            line = f_stress.readline()
            if line[0] == "-" and len(line) > 15:
                break

        # start reading data
        while True:
            line = f_stress.readline()
            values = line.split()
            if len(values) < 3:
                break
            nodes.append(int(values[1]))
            stresses.append(float(values[2]))
    return nodes, stresses


def read_coords_elem_nodes(filename):
    coords, elem_nodes = [], []
    with open(filename) as f_coord:
        # when to start reading data
        while True:
            line = f_coord.readline()
            if line[:2] == "*N":
                break

        # start reading data
        while True:
            line = f_coord.readline()
            values = line.split(", ")
            if len(values) < 4:
                break
            coords.append([float(coord) for coord in values[1:4]])

        while True:
            line = f_coord.readline()
            values = line.split(", ")
            if len(values) < 5:
                break
            elem_nodes.append([int(element) for element in values[1:5]])
    return coords, elem_nodes


def read_exterior(filename):
    exterior_nodes = pd.read_csv(filename)['nodeid'].values.tolist()
    return exterior_nodes
