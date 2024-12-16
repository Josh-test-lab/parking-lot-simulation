"""
Information:
    Title = 'Main program for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131216]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""

### import module
import random
import time
import numpy as np
from event import *

### main program
# initial value
t = 0
max_simulation_time = 10 * 365 * 24

# the parking spaces
remain_car_parking_space = 90
remain_motorcycle_parking_space = 627

# number of spaces which be parked
car_parked = 0
motorcycle_parked = 0
bicycle_parked = 0

# number of new vehicle 
new_car = 0
new_motorcycle = 0
new_bicycle = 0


