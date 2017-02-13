import RPi.GPIO as gpio
import time
import sys

gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT) #step
gpio.setup(15, gpio.OUT) #dir
gpio.setup(23, gpio.OUT) #ms1
gpio.setup(24, gpio.OUT) #ms2

def set_stepper_on():
        gpio.output(14, 0)
        time.sleep(0.05)
        gpio.output(14, 1)
        time.sleep(0.05)

def set_cw():
        gpio.output(15, 0)

def set_anticw():
        gpio.output(15, 1)

def ms_steps():
        gpio.output(23, 0)
        gpio.output(24, 0)

ms_steps()
set_cw()

infinite_loop = True
steps=0
while (infinite_loop == True):
        set_stepper_on()
        steps+=1
        print steps