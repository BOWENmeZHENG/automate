import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("nodes.csv")
x, y, z = data.x[data.nodetype == 1], data.y[data.nodetype == 1], data.z[data.nodetype == 1]
xi, yi, zi = data.x[data.nodetype == 0], data.y[data.nodetype == 0], data.z[data.nodetype == 0]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, label="type 1, exterior nodes")
ax.scatter(xi, yi, zi, label="type 2, interior nodes")
plt.legend()
plt.show()
