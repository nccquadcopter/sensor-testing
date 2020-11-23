import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/users/aaron/desktop/mag_data.csv')
df = df[['magx','magy','magz']]

# raw x, y, z list values
x = list(df.magx.values)
y = list(df.magy.values)
z = list(df.magz.values)
'''
Takes x, y, z values as lists and returns a 2D numpy array
'''
dx = abs(np.sort(list(set(x)))[-1] - np.sort(list(set(x)))[0])
dy = abs(np.sort(list(set(y)))[-1] - np.sort(list(set(y)))[0])
# i = ((x - min(x)) / dx).astype(int) # Longitudes
# j = ((y - max(y)) / dy).astype(int) # Latitudes
i = ((x - min(x)) / dx) # Longitudes
j = ((y - max(y)) / dy) # Latitudes
grid = np.nan * np.empty((len(j),len(i)))
# i = ((x - min(x)) / dx).astype('|S10') # Longitudes
# j = ((y - max(y)) / dy).astype('|S10') # Latitudes
# grid[-j, i] = z # if using latitude and longitude (for WGS/West)


# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(1977)
# x, y, z = np.random.random((3, 50))

# Bin the data onto a 10x10 grid
# Have to reverse x & y due to row-first indexing
zi, yi, xi = np.histogram2d(j, i, bins=(1910,1910), weights=z, normed=False)
counts, _, _ = np.histogram2d(j, i, bins=(1910,1910))

zi = zi / counts
# zi = np.ma.masked_invalid(zi)

# fig, ax = plt.subplots()
# ax.pcolormesh(xi, yi, zi, edgecolor='black', cmap='jet')
# scat = ax.scatter(i, j, c=z, s=50, cmap='jet', edgecolors='black')
# fig.colorbar(scat)
# ax.margins(0.05)

# plt.show()


import numpy as np
import matplotlib.pyplot as plt

X, Y = np.meshgrid(x, y)

#Z = 4*X**2 + Y**2

# zr = []
for i in range(0, len(df.magy)):
    y = df.magy.min() + ((df.magy.max() - df.magy.min()) * len(df.magy)*float(i))
    for k in range(0, len(df.magx)):
        x = df.magx.min() + ((df.magx.max() - df.magx.min()) * len(df.magx)*float(k))

#         v = 4.0*x*x + y*y

#         zr.append(v)

# Z = np.reshape(zr, X.shape)
Z = np.reshape(z, X.shape)

print(X.shape)
print(Y.shape)
print(Z.shape)

plt.contour(X, Y, Z)
plt.show()

xout = pd.DataFrame(X)
yout = pd.DataFrame(Y)
zout = pd.DataFrame(Z)

xout = xout.to_csv('/users/aaron/desktop/x2d.csv')
yout = yout.to_csv('/users/aaron/desktop/y2d.csv')
zout = zout.to_csv('/users/aaron/desktop/z2d.csv')


X = pd.read_csv('/users/aaron/desktop/x2d.csv', header=None)
X = X.drop(0, axis=1)
X = X[1:]

Y = pd.read_csv('/users/aaron/desktop/y2d.csv', header=None)
Y = Y.drop(0, axis=1)
Y = Y[1:]

Z = pd.read_csv('/users/aaron/desktop/z2d.csv', header=None)
Z = Z.drop(0, axis=1)
Z = Z[1:]

# # width 

# z_array = np.nan * np.empty((width,height))
# z_array[Y, X] = Z
# 
# 
# 


# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # # Grab some test data.
# # X, Y, Z = axes3d.get_test_data(0.05)

# # Plot a basic wireframe.
# ax.plot_wireframe(x, y, zi, rstride=1, cstride=1)

# plt.show()




'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np


# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Make data.
# X = np.arange(-5, 5, 0.05)
# Y = np.arange(-5, 5, 0.05)
# X, Y = np.meshgrid(i, j)
# R = np.sqrt(X**2 + Y**2)
# Z = np.cos(R)
# Z = zi

# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()
# 
# 
# 

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-8, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-8, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=8, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-8, 48)
ax.set_ylabel('Y')
ax.set_ylim(-8, 8)
ax.set_zlabel('Z')
ax.set_zlim(-8, 8)

# plt.show()

