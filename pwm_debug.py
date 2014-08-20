#!/usr/bin/python
# -*- coding: utf-8 -*-

# uncomment line 14-20 for using I2C and comment line 24-35, switch for using GPIO directly

import smbus
import time
import RPi.GPIO as GPIO

liste = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print liste #debugging ...
periodendauer = 0.001 # means 1000Hz

# # to send data to mcp23017
# b = smbus.SMBus(1) # 0 indicates /dev/i2c-0, muss auf 1 stehen (für rev2)
# while True:
	# for values in liste:
		# b.write_byte_data(0x20,0x14,values) #send data via smbus(I2C) to mcp23017
		# # print values #debugging only
		# time.sleep(periodendauer)

		
# to send data direct to gpio-pin
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
while True:
	for values in liste:
		if values > 0:
			values = True
		else:
			values = False
		GPIO.output(7,values)
		# print values #debugging only
		time.sleep(periodendauer)