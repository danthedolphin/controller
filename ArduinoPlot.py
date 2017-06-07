# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 22:41:12 2017

@author: Daniel
"""

import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3',115200)
print 'Serial is opened'

gyro = []
position = []
shoot = []
time = []
plt.ion

plt.subplot(3,1,1)
gyrohandle = plt.plot(time, gyro,'c')
plt.ylim(-500,500)
plt.xlabel("Time")
plt.ylabel("Gyro")

plt.subplot(3,1,2)
poshandle = plt.plot(time, position,'g')
plt.ylim(5,725)
plt.xlabel("Time")
plt.ylabel("Position")

plt.subplot(3,1,3)
shoothandle = plt.plot(time, shoot,'r')
plt.ylim(0,1)
plt.xlabel("Time")
plt.ylabel("Shoot")


count = 0

while 1:
    try:
        value = ser.readline().split('\t')
        position.append(int(value[1]))
        time.append(int(value[0]))
        gyro.append(float(value[2]))
        shoot.append(int(value[4]))

        if ((len(position))>400):
            del position[0]
            del time[0]
            del gyro[0]
            del shoot[0]
            
        if (count%10 == 0):
            plt.subplot(3,1,1)
            gyrohandle[0].set_ydata(gyro)
            gyrohandle[0].set_xdata(time)
            plt.xlim(time[0],time[-1])
            plt.pause(0.01)
            
            plt.subplot(3,1,2)
            poshandle[0].set_ydata(position)
            poshandle[0].set_xdata(time)
            plt.xlim(time[0],time[-1])
            plt.pause(0.01)
            
            plt.subplot(3,1,3)
            shoothandle[0].set_ydata(shoot)
            shoothandle[0].set_xdata(time)
            plt.xlim(time[0],time[-1])
            plt.pause(0.01)
            
        
        
    except KeyboardInterrupt:
        ser.close()
    
    count = count + 1
