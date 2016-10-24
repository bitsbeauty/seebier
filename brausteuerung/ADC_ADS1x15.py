# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

import math



# Create an ADS1115 ADC (16-bit) instance.
#
# Or create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1




class NTCsensor():
	"""docstring for NTCsensor"""
	
	def __init__(self, _pin):
		# super(NTCsensor, self).__init__()
		self.pin = _pin
		self.B = 3914.76611887
		self.T0 = 25    #// Nenntemperatur des NTC-Widerstands in C
		self.R0 = 2251 #// Nennwiderstand des NTC-Sensors in Ohm
		self.T1 = 100   #// erhoehte Temperatur des NTC-Widerstands in C
		self.R1 = 153  #// Widerstand des NTC-Sensors bei erhoehter Temperatur in Ohm
		self.RV = 1000 #// Vorwiderstand in Ohm
		print "INIT NTC"
		

	#NTC temperature calculation by "jurs" for German Arduino forum
	ABSZERO = 273.15
	MAXANALOGREAD = 1651.0  #maximal analog read value

	def temperature_NTCB(self, VA_VB):
		# // Ermittlung der Temperatur mittels NTC-Widerstand
		# // Version der Funktion bei gegebener Materialkonstante B
		# // Erklarrung der Parameter:
		# // T0           : Nenntemperatur des NTC-Widerstands in C
		# // R0           : Nennwiderstand des NTC-Sensors in Ohm
		# // B            : Materialkonstante B
		# // Vorwiderstand: Vorwiderstand in Ohm  
		# // VA_VB        : Spannungsverhaeltnis "Spannung am NTC zu Betriebsspannung"
		# // Rueckgabewert : Temperatur

		T0 = self.T0 + self.ABSZERO  #umwandeln Celsius in absolute Temperatur
		self.RN = self.RV * VA_VB / (1.0-VA_VB) #aktueller Widerstand des NTC
		
		self.temp = T0 * self.B / (self.B + T0 * math.log(self.RN / self.R0))-self.ABSZERO

		return self.temp

	def readTemp(self):
		aValue = adc.read_adc(self.pin, gain=GAIN)
		 
		#// Berechnen bei bekannter Materialkonstante 3914.76611887
		self.temp = self.temperature_NTCB(aValue/self.MAXANALOGREAD)
		# print("NTCB in C: "),temp

	def temp_str(self):
		self.readTemp()
		# print self.temp # -74.706370654
		if round(self.temp,3) == -74.706:
			#print "not pluged"
			return "-"
		else:
			#print "plugged"
			return str(round(self.temp,1))+u"\u00b0"



# def temperature_NTCB(T0, R0, B,  RV, VA_VB):
# 	# // Ermittlung der Temperatur mittels NTC-Widerstand
# 	# // Version der Funktion bei gegebener Materialkonstante B
# 	# // Erklarrung der Parameter:
# 	# // T0           : Nenntemperatur des NTC-Widerstands in C
# 	# // R0           : Nennwiderstand des NTC-Sensors in Ohm
# 	# // B            : Materialkonstante B
# 	# // Vorwiderstand: Vorwiderstand in Ohm  
# 	# // VA_VB        : Spannungsverhaeltnis "Spannung am NTC zu Betriebsspannung"
# 	# // Rueckgabewert : Temperatur

# 	T0+=ABSZERO  #umwandeln Celsius in absolute Temperatur
# 	RN=RV*VA_VB / (1-VA_VB) #aktueller Widerstand des NTC

# 	return T0 * B / (B + T0 * math.log(RN / R0))-ABSZERO
	

# B = 3914.76611887
# T0 = 25    #// Nenntemperatur des NTC-Widerstands in C
# R0 = 2251 #// Nennwiderstand des NTC-Sensors in Ohm
# T1 = 100   #// erhoehte Temperatur des NTC-Widerstands in C
# R1 = 153  #// Widerstand des NTC-Sensors bei erhoehter Temperatur in Ohm
# Vorwiderstand = 1000 #// Vorwiderstand in Ohm  







if __name__ == '__main__':
	try:  
		
		# print "Berechnung"
		# T1 = 298.15
		# R1 = 2251

		# T2 = 373.15
		# R2 = 153

		# B = (T1 * T2)/ (T2-T1) * math.log(R1/R2)
		# print "B=",B
		# #B= 3914.76611887

		tempNtc = NTCsensor(0)

		while True:
			tempNtc.readTemp()
			print("NTCB in C: "),tempNtc.temp_str()
			time.sleep(0.5)

	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working
		import traceback
		print traceback.format_exc()
		#print "Other error or exception occurred!"  
	  
	finally:
		pass
