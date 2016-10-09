import RPi.GPIO as GPIO
import time

# GPIO Setup





class Fuellstand():
	"""docstring for Fuellstand"""
	
	# HIGH = AUS
	# LOW = AN

	def __init__(self, _pin):
		#super(Relay, self).__init__()
		self.pin = _pin
		self.status = 0

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin ,GPIO.IN)

	def read(self):
		# HIGH = AUS
		# LOW = AN
		self.status = GPIO.input(self.pin) #make on
		return self.status







# ---------------------------------------------------------------
if __name__ == '__main__':
	try:  
		fPin = 17
		fuellstandsSensor = Fuellstand(fPin)

		while True:
			print fuellstandsSensor.read();
			time.sleep(0.05)


	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working
		import traceback
		print traceback.format_exc()
		#print "Other error or exception occurred!"  
	  
	finally:
		print "FinallY"
		GPIO.cleanup() # this ensures a clean exit

# ---------------------------------------------------------------		