import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/users/aaron/desktop/mag_data.csv')
df = df[['magx','magy','magz']]



# dfints = df * 10000

width = int(dfints.magx.max() - dfints.magx.min())
height = int(dfints.magy.max() - dfints.magy.min())

X = list(dfints.magx.values.astype(int))
Y = list(dfints.magy.values.astype(int))
Z = list(dfints.magz.values.astype(int))

X
Y
Z


# zi, yi, xi = np.histogram2d(Y, X, bins=(width, height), weights=Z, normed=False)
# zi = np.ma.masked_equal(zi,0)

# fig, ax = plt.subplots()
# ax.pcolormesh(xi, yi, zi, edgecolors='black')
# scat = ax.scatter(X,Y,c=Z, s=200)
# fig.colorbar(scat)
# ax.margins(0.05)

# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(1977)
# x, y, z = np.random.random((3, 50))

# Bin the data onto a 10x10 grid
# Have to reverse x & y due to row-first indexing
zi, yi, xi = np.histogram2d(Y, X, bins=(1000,1000), weights=Z, normed=False)
counts, _, _ = np.histogram2d(Y, X, bins=(1000,1000))

zi = zi / counts
zi = np.ma.masked_invalid(zi)

fig, ax = plt.subplots()
ax.pcolormesh(xi, yi, zi, edgecolor='black', cmap='jet')
scat = ax.scatter(X, Y, c=Z, s=50, cmap='jet', edgecolors='black')
fig.colorbar(scat/10000)
ax.margins(0.05)

plt.show()

# # width 

# z_array = np.nan * np.empty((width,height))
# z_array[Y, X] = Z