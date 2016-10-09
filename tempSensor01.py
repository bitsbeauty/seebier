#!/usr/bin/env python

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

### Sensoren
#1 = 28-0000072fbb7d

class TempSensor():

	def __init__(self, serialnr):
		self.base_dir = '/sys/bus/w1/devices/'

		if os.path.isdir(self.base_dir + serialnr):
			self.device_folder = self.base_dir + serialnr
			# print "FOLDER:",self.device_folder
			self.device_file = self.device_folder + '/w1_slave'
			self.connected = True
		else:
			self.connected = False

	def read_temp_raw(self):
		f = open(self.device_file, 'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		# TODO: Show when sensor is not connected
		try:
			lines = self.read_temp_raw()

			while lines[0].strip()[-3:] != 'YES':
				time.sleep(0.2)
				lines = read_temp_raw()

			equals_pos = lines[1].find('t=')
			if equals_pos != -1:
				temp_string = lines[1][equals_pos+2:]
				self.temp_c = float(temp_string) / 1000.0
				self.temp_f = self.temp_c * 9.0 / 5.0 + 32.0
				return self.temp_c
		except:
			return None

	def temp_str(self):
		temp = self.read_temp()
		if temp is None:
			return "-"
		else:
			return str(round(temp,1))+u"\u00b0"
		



if __name__ == '__main__':
	try:
		maischeTemp = TempSensor("28-0000072fbb7d")

		while True:
			print "%f C" % (maischeTemp.read_temp())	
			time.sleep(1)
	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working
		import traceback
		print traceback.format_exc()
		#print "Other error or exception occurred!"  
	  
	finally:
		pass
