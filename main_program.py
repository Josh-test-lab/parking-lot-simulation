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
from event import *
from function import *

### main program
## initial value
t = 0 # simulation clock
clock = 0 # clock in a day
max_simulation_time = 10 * 365 * 24 # total time

# the parking spaces
max_car_parking_space = 90
max_motorcycle_parking_space = 627
remain_car_parking_space = max_car_parking_space
remain_motorcycle_parking_space = max_motorcycle_parking_space

# number of spaces which be parked now
car_parked = 0
motorcycle_parked = 0
bicycle_parked = 0

# number of new vehicle enter/leave the parking lot
new_car = 0
new_motorcycle = 0
new_bicycle = 0

while t <= max_simulation_time:
    
    # update time variable
    if clock == 23:
        clock == 0
    else:
        clock += 1

    t += 1