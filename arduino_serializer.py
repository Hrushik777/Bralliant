import serial
import time

arduino = None

def arduino_initialize(port='COM3', baudrate=9600):
    global arduino
    arduino = serial.Serial(port, baudrate, timeout=1)
    time.sleep(2) 

def arduino_write(text):
    global arduino
    arduino.write((text + '\n').encode())

def arduino_close():
    global arduino
    if arduino is not None:
        arduino.close()
        arduino = None 

