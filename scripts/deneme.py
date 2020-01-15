
import serial
import sys
import time

ssc32 = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0);
print(ssc32.name)
print("start")
ssc32.write("#1 P1000 T1000 \r")
print("end")
ssc32.close()

