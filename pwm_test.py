#!/usr/bin/python
# -*- coding: utf-8 -*-

#software pwm with I2C using mcp23017
# started with 3 channels / will be upgraded later to 8
# GPIO comment for debugging purpose, wanted to know if flickering every 4-5sec is a problem of smbus or not

import smbus
import time
import sys
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BOARD)
# GPIO.cleanup()
# GPIO.setup(7, GPIO.OUT)

b = smbus.SMBus(1) # 0 indicates /dev/i2c-0, muss auf 1 stehen (für rev2)

# def channels(channel):
	# for i < channel
		# dutycycle_i = 0
		
# def set_dutycycle(channel,duty)
	# for i < channel
		# dutycycle_i = duty

def periode(frequenz_hz):
	period = 1.0/frequenz_hz
	return period
		
def pwm_on(frequenz,dutycycle_0,dutycycle_1,dutycycle_2):
	global duty_0, duty_1, duty_2
	x,y,z = 0,0,0 #initialice x,y,z for if-loops
	p0,p1,p2 = 0,0,0 #initialice p0,p1,p2 for on or off
	liste = []
	for i in range(0,100):
		if duty_0 == 0:
			p0 = 0x00
		else:
			if x <= i:
				# set light on channel_1
				p0 = 0x01	#hexcode for pin1 on at mcp 
				x = x + duty_0
				# print x
			else:
				# set light off channel_0
				p0 = 0x00
		if duty_1 == 0:
			p1 = 0x00
		else:
			if y <= i:
				# set light on channel_1
				y = y + duty_1
				p1 = 0x02	#hexcode for pin2 on at mcp 
				# print y
			else:
				# set light off channel_1
				p1 = 0x00
		if duty_2 == 0:
			p2 = 0x00
		else:
			if z <= i:
				# set light on channel_2
				z = z + duty_2
				p2 = 0x04	#hexcode for pin3 on at mcp 
				# print z
			else:
				# set light off channel_2
				p2 = 0x00
		liste.append(pwm(p0,p1,p2))
				
		if i == frequenz_hz-1:
			i = 0
			x = 0
			y = 0
			z = 0
	# print liste
	return liste

def pwm(p0,p1,p2):
	p_all = p0 + p1 + p2 #sum up different pins to use a single command to write it (
	return p_all
	
	
#set frequency in HZ, dutycycle from 0 to 1.0 for (atm 3) channels, will get data from outside later
frequenz_hz = 500.0
periodendauer = periode(frequenz_hz)
dutycycle_0 = 0.0
dutycycle_1 = 0.0
dutycycle_2 = 0.1
# channel = 0
if dutycycle_0 == 0:
	duty_0 = 0
else:
	duty_0 = 1/dutycycle_0
if dutycycle_1 == 0:
	duty_1 = 0
else:
	duty_1 = 1/dutycycle_1
if dutycycle_2 == 0:
	duty_2 = 0
else:
	duty_2 = 1/dutycycle_2

liste = pwm_on(frequenz_hz,dutycycle_0,dutycycle_1,dutycycle_2)	#bring it into a list, looping over list is way faster than calculating this 500times per second
print liste	#debugging purpose only

# for i in range(0,100):
	# if liste[i] != 0:
		# liste[i] = True
	# else:
		# liste[i] = False
# print liste

# while True:
	# for werte in liste:
		# GPIO.output(7,werte)
		
		# time.sleep(periodendauer)

while True:
	for werte in liste:
		b.write_byte_data(0x20,0x14,werte)
		# print werte
		time.sleep(periodendauer)
 
# address = 0x20 # I2C Adresse
# PinDict= {"7": 0x80, "6":0x40, "5":0x20, "4":0x10,"3":0x08, "2":0x04, "1":0x02, "0":0x01, "allon":0xff, "alloff":0x00}