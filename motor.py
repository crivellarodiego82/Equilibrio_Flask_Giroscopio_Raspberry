# Crivellaro Diego Sistema di equilibrio
import time
import RPi.GPIO as GPIO
# Inizializzazione pin gpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mhz = 100

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

m1 = GPIO.PWM(4, mhz)
m2 = GPIO.PWM(17, mhz)
m3 = GPIO.PWM(18, mhz)
m4 = GPIO.PWM(21, mhz)

def backward(speed):
    if(speed > 100):
        speed = 100
    m1.start(speed) 
    GPIO.output(4, False)
    m3.start(speed)
    GPIO.output(18, False)
    
def forward(speed):
    if(speed > 100):
        speed = 100
    m2.start(speed) 
    GPIO.output(17, False)
    m4.start(speed)
    GPIO.output(21, False)

def stop():
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()
    
def finish():
	print('Finishing up!')
	GPIO.output(4, False)
	GPIO.output(17, False)
	GPIO.output(18, False)
	GPIO.output(21, False)
	quit()
