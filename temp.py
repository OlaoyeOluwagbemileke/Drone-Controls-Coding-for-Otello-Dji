# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()



tello.land()