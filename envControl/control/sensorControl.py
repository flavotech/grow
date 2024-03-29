import envControl.control.serialBase as serialBase
from databases import dataBase
import time
import datetime


# saveValue: formats sensor reading and sends it to dataBase function
# 	to save it to the database
# inputs: sensor - type of sensor input; value - value of sensor reading
def saveValue(sensor, value):
	now = datetime.datetime.now()
	#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	dataBase.insertReading(sensor,  value, now)

# function to read analog input pH and convert to pH
def readpH():
	m = dataBase.getCalibrationParameter("pHslope")
	serialBase.sendChar('P')
	time.sleep(.5)
	pH_voltage = float(serialBase.readLine()[:4]) # get rid of the new line carriage '\r\n' and convert to float
	pH = round(7 - (3.26 - pH_voltage)*m, 2)
	print("pH: ")
	print(pH)
	return pH

# function to read the raw pH voltage
def readpHVolts():
	serialBase.sendChar('P')
	time.sleep(.5)
	pH_voltage = float(serialBase.readLine()[:4])
	print(pH_voltage)
	return pH_voltage

# function to display the pH voltage over and over
def adjustpHOffset():
	while True:
		serialBase.sendChar('P')
		time.sleep(.5)
		pH_voltage = float(serialBase.readLine()[:4])
		print(pH_voltage)

# function to return the water temperature of the tank
def readWaterTemp():
	serialBase.sendChar('W')
	time.sleep(.5)
	waterTemp = serialBase.readLine()
	print("Water temperature: ")
	print(waterTemp)
	return waterTemp

# function to read air temperature of the cabinet
def readTemp():
	serialBase.sendChar('T')
	time.sleep(.5)
	temp = serialBase.readLine()[:3] # extract temp voltage
	temp = temp.decode()
	temp = float(temp)
	temp = .1205*temp
	print("Air temp: ")
	print(temp)
	return temp

# function to read electrical conductivity of the water
def readEC():
	serialBase.sendChar('E')
	time.sleep(.5)
	EC = float(serialBase.readLine()[:3])
	print("EC: ")
	print(EC)
	print("ms/cm")
	return EC

# function to read TDS
def readTDS():
	serialBase.sendChar('D')
	time.sleep(.5)
	TDS = float(serialBase.readLine()[:5])
	print("TDS: ")
	print(TDS)
	print("ppm")
	return TDS

