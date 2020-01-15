#! /usr/bin/env python
import serial
import sys
import time
import rospy
from sensor_msgs.msg import Joy
def callback(joy):
       change = joy.axes[1]*10
       if joy.buttons[0]:
	  loc1+change
       if joy.buttons[1]:
	  loc2+change
       if joy.buttons[2]:
          loc4+change
       if joy.buttons[3]:
	  loc5+change
       if joy.buttons[4]:
	  loc6+change
       if joy.buttons[5]:
	  loc7+change


	
def main():
 rospy.init_node('surucu', anonymous=True)
 rospy.Subscriber("joy",Joy, callback)
 '''ssc32 = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0);
 print(ssc32.name)
 print("start")
 if d==1:
	 ssc32.write("#1 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#2 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#3 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#4 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#5 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#6 P1100 T1000 \r")
	 time.sleep(2)
	 ssc32.write("#7 P1100 T1000 \r")
	 print("end")
	 ssc32.close()
'''
 rospy.spin()
if __name__ == '__main__':
   	 main()
