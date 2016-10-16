#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
import tempSensor as Temp 
import ADC_ADS1x15 as ADC

#Temp Sensoren
maischeTemp = Temp.TempSensor("28-0000072fbb7d")
nachgussTemp = Temp.TempSensor("28-0000072e5bab")
pkTemp = ADC.NTCsensor(3)


class Window(QtGui.QWidget):

	def __init__(self):
		super(Window, self).__init__()
		# self.setGeometry(50, 50, 500, 300)
		# self.setWindowTitle("PyQT tuts!")
		# self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.palette = QtGui.QPalette()
		self.palette.setColor(QtGui.QPalette.Background, QtGui.QColor(21, 81, 133))
		self.setPalette(self.palette)

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.on_timer)
		self.timer.start(500)

		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)

		# define style of Textfield (Labels)
		self.labelPalette = QtGui.QPalette()
		self.labelPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)

		#Layout


		# --------MAISCHE TEMP
		self.l_maischeTempText = QtGui.QLabel("Maische Temperatur",self)
		self.l_maischeTempText.move(100, 270)
		self.l_maischeTempText.setPalette(self.labelPalette)
		self.l_maischeTempText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
		#Temperature 
		self.l_maischeTemp = QtGui.QLabel(self)
		self.l_maischeTemp.move(100, 200)
		self.l_maischeTemp.setPalette(self.labelPalette)
		font = QtGui.QFont()
		# font.setFamily(_fromUtf8("FreeMono"))
		font.setPixelSize(70)
		self.l_maischeTemp.setFont(font)
		self.l_maischeTemp.setText("00,00"+u"\u00b0")

		# -------NACHGUSS TEMP
		self.l_nachgussTempText = QtGui.QLabel("Nachguss Temperatur",self)
		self.l_nachgussTempText.move(400, 270)
		self.l_nachgussTempText.setPalette(self.labelPalette)
		self.l_nachgussTempText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
		# Temperature 
		self.l_nachgussTemp = QtGui.QLabel(self)
		self.l_nachgussTemp.move(400, 200)
		self.l_nachgussTemp.setPalette(self.labelPalette)
		font = QtGui.QFont()
		# font.setFamily(_fromUtf8("FreeMono"))
		font.setPixelSize(70)
		self.l_nachgussTemp.setFont(font)
		self.l_nachgussTemp.setText("00,00"+u"\u00b0")

		# -------PLATTENKÜHLER TEMP
		self.l_pkTempText = QtGui.QLabel("Plattenkühler",self)
		self.l_pkTempText.move(650, 270)
		self.l_pkTempText.setPalette(self.labelPalette)
		self.l_pkTempText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
		# Temperature 
		self.l_pkTemp = QtGui.QLabel(self)
		self.l_pkTemp.move(650, 235)
		self.l_pkTemp.setPalette(self.labelPalette)
		font = QtGui.QFont()
		# font.setFamily(_fromUtf8("FreeMono"))
		font.setPixelSize(30)
		self.l_pkTemp.setFont(font)
		self.l_pkTemp.setText("00,00"+u"\u00b0")


		# self.show()
		self.showFullScreen()

	def on_timer(self):
		self.l_maischeTemp.setText(maischeTemp.temp_str())
		self.l_nachgussTemp.setText(nachgussTemp.temp_str())
		self.l_pkTemp.setText(pkTemp.temp_str())
		#print ("maische:{} nachguss:{}".format(maischeTemp.temp_str()))
		print maischeTemp.temp_str()

	def close_application(self):
		print("Exit the Programm")
		sys.exit()
	

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())



if __name__ == '__main__':
	try:  
		
		run()

	except:  
		# this catches ALL other exceptions including errors.  
		# You won't get any error messages for debugging  
		# so only use it once your code is working
		import traceback
		print traceback.format_exc()
		#print "Other error or exception occurred!"  
	  
	finally:
		GUI.close_application()

