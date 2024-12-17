"""
Information:
    Title = 'Main program for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131217, 1131216]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""

### import module
import random
import time
import numpy as np
from event import *

### main program
# initial value
t = 0 # simulation clock
clock = 0 # clock in a day
max_simulation_time = 10 * 365 * 24 # total time

# the parking spaces
max_car_parking_space = 90
max_motorcycle_parking_space = 627
remain_car_parking_space = max_car_parking_space
remain_motorcycle_parking_space = max_motorcycle_parking_space

# number of spaces which be parked
car_parked = 0
motorcycle_parked = 0
bicycle_parked = 0

# number of new vehicle 
new_car = 0
new_motorcycle = 0
new_bicycle = 0

motorcycle_parked, remain_motorcycle_parking_space, motorcycle_leave_failed = motorcycle_leave_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space)

[motorcycle_parked, remain_motorcycle_parking_space, motorcycle_leave_failed]