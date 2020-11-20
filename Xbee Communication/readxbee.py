import serial # these
import time # are package "dependencies." Think of them as "libraries" for certain functions (like the libraries that contain certain functions for our sensors)

# lines 6-12 assigns a "read serial port" function to the variable ser, along with some parameters
ser = serial.Serial(
	port='/dev/tty.usbserial-DN066RZ4', #this line is important, it's the name of the serial port 
	# that the xbee is connected to
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

while True: #for as long as there is no exception, do the following:
	try:
		oneByte = ser.read(1) #try reading one byte, what does it say?
		if oneByte == b"\r": #if that byte indicates the end of the line...
			print (buffer) # print it out so we can see what it said 
			with open(path,"a") as f: #lines 30 and 32 write to the file
				f.write(str(time.time()) + "," + str(buffer) + "\n")
			buffer = "" #let's reset the buffer, because we just saved the whole line.
			continue #and continue with our "while loop"
		else:
			buffer += oneByte.decode() #if line 28 indicated that it wasn't the end of the line, add the byte to the buffer and continue our while loop.
	except:
		ser.flushInput() #if there is an exception/error, flush the serial port and end the loop
		quit()




