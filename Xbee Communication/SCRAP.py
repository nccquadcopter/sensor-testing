import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/users/aaron/desktop/mag_data.csv')
df = df[['magx','magy','magz']]

#convert to integers
df = df * 1000
df = df.astype(int)


#set array dimensions
# width = int(df.magx.max() - df.magx.min())
# height = int(df.magy.max() - df.magy.min())


# raw x, y, z list values
x = list(df.magx.values)
y = list(df.magy.values)
z = list(df.magz.values)

#map values to index for later use
# xmap = df.magx.to_dict()
# ymap = df.magy.to_dict()
# zmap = df.magz.to_dict()

# #create an index series
# df['i'] = df.index
# df['xi'] = df.i * df.magx
# xi = list(df['xi'].values)

# index = df.index.to_list()

# # z_array = np.nan * np.empty((4587,4587))
# z_array[Y, X] = Z



def make_grid(x, y, z):
    '''
    Takes x, y, z values as lists and returns a 2D numpy array
    '''
    dx = abs(np.sort(list(set(x)))[-1] - np.sort(list(set(x)))[0])
    dy = abs(np.sort(list(set(y)))[-1] - np.sort(list(set(y)))[0])
    i = ((x - min(x)) / dx).astype(int) # Longitudes
    j = ((y - max(y)) / dy).astype(int) # Latitudes
    grid = np.nan * np.empty((len(set(j)),len(set(i))))
    grid[-j, i] = z # if using latitude and longitude (for WGS/West)
    return grid

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
# zi, yi, xi = np.histogram2d(Y, X, bins=(1000,1000), weights=Z, normed=False)
# counts, _, _ = np.histogram2d(Y, X, bins=(1000,1000))

# zi = zi / counts
# zi = np.ma.masked_invalid(zi)

# fig, ax = plt.subplots()
# ax.pcolormesh(xi, yi, zi, edgecolor='black', cmap='jet')
# scat = ax.scatter(X, Y, c=Z, s=50, cmap='jet', edgecolors='black')
# fig.colorbar(scat/10000)
# ax.margins(0.05)

# plt.show()

# # width 

# z_array = np.nan * np.empty((width,height))
# z_array[Y, X] = Z