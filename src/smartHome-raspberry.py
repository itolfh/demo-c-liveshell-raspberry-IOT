#!/usr/bin/python

import json
import sys
import RPi.GPIO as GPIO
from time import sleep

realData = ''
realData = realData + sys.argv[1]

#控制灯的gpio口（BCM模型下的gpio编号）
ledGpio=23
#控制门的gpio口（BCM模型下的gpio编号）
doorGpio=18
#门开的电机角度值
doorOpenValue = 10
#门关的电机角度值
doorCloseValue = 5

#灯和门的状态
ledStatus=0
doorStatus=0

#change a json string to dict
data_str = json.loads(realData)

#change the value of 'led' node to int
ledStatus = int(data_str['led'])

#change the value of 'door' node to int
doorStatus = int(data_str['door'])

#disable warnings
GPIO.setwarnings(False)

#set raspberry's gpio into bcm's mode
GPIO.setmode(GPIO.BCM)

#set led and door gpio to output
GPIO.setup(ledGpio, GPIO.OUT)
GPIO.setup(doorGpio, GPIO.OUT)

#set door gpio to pwm, and start
motor = GPIO.PWM(doorGpio, 50)
motor.start(0)

#if led status is 1, means turn it on, else turn off
if(ledStatus == 1):
	GPIO.output(ledGpio, GPIO.LOW)
else:
	GPIO.output(ledGpio, GPIO.HIGH)

#If door status is 1, turn door on, else turn off.
#
if(doorStatus == 1):
	motor.ChangeDutyCycle(doorOpenValue)
	sleep(2)
else:
	motor.ChangeDutyCycle(doorCloseValue)
	sleep(2)
	
