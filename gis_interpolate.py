import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')   # try another styles: 'classic'

NDOTS = 100

lat = [1, 2, 3, 3.2, 3.4]
long = [1, 2, 3, 5, 4.5]
param = [2, 3, 2, 1, 3]

fig = plt.figure()
plt.scatter(lat, long, c=param, s=100, marker='s')
plt.colorbar()

fig.show()
fig.savefig('/home/pi/pic.png')
