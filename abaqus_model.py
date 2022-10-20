from abaqus import *
from abaqusConstants import *

mdb = openMdb('wheel.cae')
p = mdb.models['Model-1'].parts['wheel']
node_object = p.sets['Set-1'].nodes
node_labels = [node.label for node in node_object]

with open('exterior.csv', 'w') as f:
    f.write('nodeid\n') 
    for label in node_labels:
        f.write(str(label) + '\n')