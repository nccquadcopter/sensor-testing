#every onece in a few hundred data points, two lines get sent over together as one line.
#This is just a simple pandas script to find those and eliminate them.

import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('QT4Agg')
import pandas as pd

path = '/users/aaron/desktop/test_data.csv' #change this to location of file

def clean_magData():
	df = pd.read_csv(path, header=None, names=['recieved_time', 'sensor_id', 
		'sensor_time', 'magx', 'magy', 'magz'])

	magframe = df[df.sensor_id == "magData"] #creates magnetometer df. filters out incomplete tags
	try:
		magframe = magframe[~magframe.magz.str.contains('mag')]#filters out tags in numerical data
	except:
		pass
	print('\n'+str(len(df) - len(magframe))+' rows removed from dataset.\n') #tell us what we removed
	magframe = magframe.drop(['recieved_time', 'sensor_id'], axis=1)# get rid of our timestamp and id, rely on one from teensy and the fact that we know this all comes from the magnetometer
	magframe = magframe.astype(float) #make sure all values are floats
	magframe.to_csv('/users/aaron/desktop/mag_data.csv') #save mag data in its own csv file
	return magframe

mag = clean_magData()
# mag.plot()
# 
mag = pd.read_csv('/users/aaron/desktop/mag_data.csv')

# the snippet below  is the first attempt at maping in 3d. it works for the x,y,z magData
# this will be more useful when we pair the values with position
#  ..right now, it lacks anything about orientation
#  incredible, really. after "cleaning", it takes just a few lines of code to plot it in 3 dimensions
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

dfz = mag.reset_index()
dfz = dfz[['magx','magy','magz']]

surf = ax.plot_trisurf(dfz.magx, dfz.magy, dfz.magz,  
	cmap='twilight', edgecolor="black", linewidth=0.2)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# ax.scatter(dfz.magx, dfz.magy, dfz.magz, c=dfz.magz, cmap='twilight', linewidth=0.5)
# ax.plot(dfz.magx, dfz.magy, dfz.magz, color='black', linewidth=0.2)

ax.set_xlabel('X')
# ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
# ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
# ax.set_zlim(-100, 100)

plt.show()


