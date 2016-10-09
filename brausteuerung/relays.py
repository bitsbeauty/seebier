import RPi.GPIO as GPIO
import time

# GPIO Setup
GPIO.setmode(GPIO.BCM)




class Relay():
	"""docstring for Relay"""
	
	# HIGH = AUS
	# LOW = AN

	def __init__(self, _pins):
		#super(Relay, self).__init__()
		i=0
		self.pins = _pins

		for relayPin in self.pins:
			GPIO.setup(relayPin ,GPIO.OUT)
			GPIO.output(relayPin, GPIO.HIGH) #make on


	def test(self):
		for relayPin in self.pins:
			GPIO.output(relayPin, GPIO.LOW) #make on
			time.sleep(0.5)

		for relayPin in self.pins:
			GPIO.output(relayPin, GPIO.HIGH) #do off

	def actuate(self, relayNr):
		# HIGH = AUS
		# LOW = AN
		GPIO.output(self.pins[relayNr], GPIO.LOW) #make on







# ---------------------------------------------------------------
if __name__ == '__main__':
	try:  
		relayPins = [6, 13, 19, 26]
		brennerRelay = Relay(relayPins)

		brennerRelay.test()
		time.sleep(1)
		brennerRelay.actuate(0)
		time.sleep(1)
		brennerRelay.actuate(3)
		time.sleep(0.5)
		


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