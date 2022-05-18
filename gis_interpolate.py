# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:39:00 2022

@author: Phil
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')   # try another styles: 'classic'

srcData = "D:/1_Data1/SeaAllMethane/methaneSea.dat"
destData = "D:/1_Data1/SeaAllMethane/methaneSeaRes.dat"
# srcData = "~/methaneSea.dat"

df = pd.read_csv(srcData,
                 header=1,
                 #skip_blank_lines=True,
                 skipinitialspace=True,
                 na_values='--',
                 skiprows=[2],
                 sep='\t',
                 decimal=',',
                 #nrows=100000,
                 usecols=[1,2,3],
                 )


longStep = 0.01
latStep = 0.01

df['long'] = (df['longitude']/longStep).round()*longStep
df['lat'] = (df['latitude']/latStep).round()*latStep

res = df.groupby(['long', 'lat'], as_index=False).agg({'ch4_water_calc': ['mean', 'count']})

res.to_csv(destData,
           sep='\t',
           )

valMax = res['ch4_water_calc'].max


fig = plt.figure()

# wether this or those
plt.scatter(res['long'], res['lat'], c='r', s=10, marker='s')


fig.show()
fig.savefig('gis.png')

print(df)
print(res)
