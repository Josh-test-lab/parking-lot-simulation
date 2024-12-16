"""
Information:
    Title = 'Events for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131216]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""

### import module
import random
import numpy as np

### function
def bicycle_parked_in_motorcycle_space(new_bicycle, bicycle_parked, remain_motorcycle_parking_space):
    if new_bicycle == 0:
        return new_bicycle, bicycle_parked, remain_motorcycle_parking_space
    elif new_bicycle % 2 == 0:
        space = new_bicycle / 2
        new_bicycle = 0
    else:
        space = int(new_bicycle / 2)
        new_bicycle = 1

    if space <= remain_motorcycle_parking_space:
        remain_motorcycle_parking_space -= space
        bicycle_parked += (2 * space)
        bicycle_cannot_park = 0
    else:
        bicycle_cannot_park = 2 * (space - remain_motorcycle_parking_space)
        bicycle_parked += (2 * remain_motorcycle_parking_space)
        remain_motorcycle_parking_space = 0

    if new_bicycle == 1:
        if bicycle_parked % 2 == 1:
            bicycle_parked += 1
        elif remain_motorcycle_parking_space > 0:
            bicycle_parked += 1
            remain_motorcycle_parking_space -= 1
        elif remain_motorcycle_parking_space <= 0:
            bicycle_cannot_park += 1
    new_bicycle = 0
    return new_bicycle, bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park

def motorcycle_parked():
    return

def car_parked():
    return






