import serial # these
import time # are 
import csv # package "dependencies." Think of them as "libraries" for certain functions (like the libraries that contain certain functions for our sensors)

# lines 6-12 assigns a "read serial port" function to the variable ser, along with some parameters
ser = serial.Serial(
	port='/dev/tty.usbserial-DN066RZ4', #this line is important, it's the name of the serial port that the xbee is connected to
	baudrate=9600,
	parity=serial.PARITY_NONE, #don't know what this does but it works
	stopbits=serial.STOPBITS_ONE, #don't know what this does but it works
	bytesize=serial.EIGHTBITS) #don't know what this does but it works
ser.timeout=5

path = '/users/aaron/desktop/test_data.csv' # set the file path and name it path. This will be different on every computer and needs to be configured

print() 
print("NORMANDALE QUADCOPTER TEAM")
print()
print("connected to: " + ser.portstr) #print the port name in the terminal
print("write path set to: " + path) #pring the filepath in the terminal
print("listening...")
print() #print a blank line

buffer = "" #a placd to hold our incoming data. set to "" to erase any lingering data.
temp = "" # temp is a placeholder for what comes before and after the comma that seperates the sensor tag identifyer from the sensor data (this will allow us to save time, id, and data in seperate lines on the csv file)
while True: #for as long as there is no exception, do the following:
	try:
		oneByte = ser.read(1) #try reading one byte, what does it say?
		if oneByte == b"\r": #if that byte indicates the end of the line...
			print (buffer) # print it out so we can see what it said before the last character in the line
			with open(path,"a") as f: #lines 26 through 29 is a block to write the line to a csv file at our "path". open a file at the path and call it variable, f
				writer = csv.writer(f,delimiter=",") # assign the csv writing function to the variable, writer
				writer.writerow([time.time(),temp,buffer]) # use the writer function
				f.close() #close the file, f 
			buffer = "" #let's reset the buffer again, because we just saved the whole line.
			temp = ""
			continue #and continue with our "while loop"
		elif oneByte == b',': #once we hit the comma..
			temp = buffer #reassign the buffer we've been building to "temp"
			print(buffer) #print it
			buffer = "" #reset buffer and capture the 2nd half of the string
		else:
			buffer += oneByte.decode() #if line 24 indicated that it wasn't the end of the line, add the byte to the buffer and continue our while loop.
	except:
		ser.flushInput() #if there is an exception/error, flush the serial port and end the loop




