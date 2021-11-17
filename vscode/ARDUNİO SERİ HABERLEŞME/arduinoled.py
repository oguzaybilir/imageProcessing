import serial as s
import time

Serial = s.Serial("COM3",9600)
time.sleep(2)
print(Serial.readline())

while True:
    var = input(n)