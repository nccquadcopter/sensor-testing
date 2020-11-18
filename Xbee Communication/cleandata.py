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
	magframe.magz = magframe.magz.astype(float) #converts magz to float after removing strings
	print(str(len(df) - len(magframe)) + ' rows removed from dataset.\n') #tell us what we removed
	magframe = magframe.drop(['recieved_time', 'sensor_id'], axis=1)# get rid of our timestamp and id, rely on one from teensy and the fact that we know this all comes from the magnetometer
	magframe.to_csv('/users/aaron/desktop/mag_data.csv') #save mag data in its own csv file
	magframe = magframe.set_index('sensor_time') #set index to sensor_id
	return magframe

mag = clean_magData()
mag.plot()



# the snippet below  is the first attempt at maping in 3d. it works for the x,y,z magData
# this will be more useful when we pair the values with position
#  ..right now, it lacks anything about orientation
#  incredible, really. after "cleaning", it takes just a few lines of code to plot it in 3 dimensions

from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

dfz = mag.reset_index()
dfz = dfz[['magx','magy','magz']]

surf = ax.plot_trisurf(dfz.magx, dfz.magy, dfz.magz, 
	cmap=plt.get_cmap('gist_earth'), linewidth=0.2)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()