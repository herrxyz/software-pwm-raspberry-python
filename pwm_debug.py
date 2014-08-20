#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import sys
import json

b = smbus.SMBus(1) # 0 indicates /dev/i2c-0, muss auf 1 stehen (für rev2)

liste = json.load(open('list.txt'))
print liste

while True:
	for werte in liste:
		b.write_byte_data(0x20,0x14,werte)
		# print werte
		# time.sleep(periodendauer)