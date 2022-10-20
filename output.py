import os


def write_csv(nodes, stresses, coords, elem_nodes, exterior_nodes):
    os.makedirs("training_data", exist_ok=True)
    with open("training_data/nodes.csv", "w") as f:
        f.write("nodeid,nodetype,x,y,z,stress\n")
        for i in range(len(nodes)):
            if nodes[i] in exterior_nodes:
                nodetype = 1
            else:
                nodetype = 0
            f.write(f"{nodes[i]},{nodetype},{coords[i][0]:.5},{coords[i][1]:.5},{coords[i][2]:.5},{stresses[i]:.5}\n")
    with open("training_data/elements.csv", "w") as f:
        f.write("elemid,node1,node2,node3,node4\n")
        for i in range(len(elem_nodes)):
            f.write(f"{i},{elem_nodes[i][0]},{elem_nodes[i][1]},{elem_nodes[i][2]},{elem_nodes[i][3]}\n")
