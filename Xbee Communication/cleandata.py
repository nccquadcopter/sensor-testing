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
	magframe = magframe[~magframe.magz.str.contains('mag')]#filters out tags into numerical data
	magframe.magz = magframe.magz.astype(float) #converts to float after removing strings
	print(str(len(df) - len(magframe)) + ' rows removed from dataset.') #tell us what we removed
	magframe = magframe.drop(['recieved_time', 'sensor_id'], axis=1)# get rid of our timestamp, rely on one from teensy
	magframe.to_csv('/users/aaron/desktop/mag_data.csv') #save mag data in its own csv file
	magframe = magframe.set_index('sensor_time') #set index to sensor_id
	return magframe


mag = clean_magData()