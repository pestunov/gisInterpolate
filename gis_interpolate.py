import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')   # try another styles: 'classic'

x = np.linspace(0, 10, 200)

fig = plt.figure()
plt.plot(x, np.sin(x), '-', label='sin')
plt.plot(x, np.cos(x), '--', label='cos')
plt.legend()


fig.show()
fig.savefig('/home/pi/pic.png')
