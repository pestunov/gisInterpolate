import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')   # try another styles: 'classic'

NDOTS = 100

#lat = [1, 2, 3, 3.2, 3.4, 1.2, 2.1, 4.1]
#long = [1, 2, 3, 5, 4.5, 2.2, 3.1, 0.1]
#param = [2, 3, 2, 1, 3, 2.3, 2.6, 1.2]
x = np.linspace(1, 10, 100)
y = np.linspace(1, 10, 100)
X, Y = np.meshgrid(x, y)
Z = 1/X + np.sin(X)/Y 

fig = plt.figure()

# wether this or those
# plt.scatter(lat, long, c=param, s=100, marker='s')
# plt.colorbar()

plt.contourf(X, Y, Z, 20, cmap='RdGy')


fig.show()
fig.savefig('/home/pi/pic.png')
