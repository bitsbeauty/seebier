#!/usr/bin/env python

import sys
import os
from PyQt4 import QtGui, QtCore
import tempSensor01 as Temp 

#Temp Sensoren
maischeTemp = Temp.TempSensor("28-0000072fbb7d")


class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		# self.setGeometry(50, 50, 500, 300)
		# self.setWindowTitle("PyQT tuts!")
		# self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.palette = QtGui.QPalette()
		self.palette.setColor(QtGui.QPalette.Background, QtGui.QColor(21, 81, 133))
		self.setPalette(self.palette)

		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)

		

		# self.show()
		self.showFullScreen()

	def close_application(self):
		print("Exit the Programm")
		sys.exit()
	

def runGui():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())



if __name__ == '__main__':
	try:  
		runGui()

		while True:
			tempMaische = maischeTemp.read_temp()
			print "%f C" % (tempMaische)	
			time.sleep(1)

	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working
		import traceback
		print traceback.format_exc()
		#print "Other error or exception occurred!"  
	  
	finally:
		GUI.close_application()

