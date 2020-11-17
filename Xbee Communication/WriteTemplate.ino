  //REMEMBER to activate "Serial1" instead of "Serial" in order to communicate with the Xbee.
  //Below is an example of how to format every print line. 
  Serial1.print("ENTER SENSOR ID HERE"); //this is important for knowing what data we're receiving
  Serial1.print(","); //This seperates our "Sensor Id" from the data - very important
  Serial1.print(PUT DATA VAR HERE); //this is where you put the data to be sent. Seperate with commas.
  Serial1.print("\r"); //This is our "end line" character - very important
