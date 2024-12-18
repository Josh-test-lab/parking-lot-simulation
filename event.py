"""
Information:
    Title = 'Events for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131217, 1131216]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""

### import module
import random
import numpy as np

### function
# vehicle enter the parking lot events
def bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space):
    bicycle_cannot_park = 0
    if new_bicycle == 0:
        return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park
    
    space = int(new_bicycle / 2)
    new_bicycle = new_bicycle % 2

    if space <= remain_motorcycle_parking_space:
        remain_motorcycle_parking_space -= space
        bicycle_parked += (2 * space)
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
    #new_bicycle = 0
    return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park

def motorcycle_parked_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space):
    if new_motorcycle == 0:
        return motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park

    if new_motorcycle <= remain_motorcycle_parking_space:
        remain_motorcycle_parking_space -= new_motorcycle
        motorcycle_parked += new_motorcycle
        motorcycle_cannot_park = 0
    else:
        motorcycle_cannot_park = new_motorcycle - remain_motorcycle_parking_space
        motorcycle_parked += remain_motorcycle_parking_space
        remain_motorcycle_parking_space = 0
    #new_motorcycle = 0
    return motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park

def car_parked_event(new_car, car_parked, remain_car_parking_space):
    if new_car == 0:
        return car_parked, remain_car_parking_space, car_cannot_park

    if new_car <= remain_car_parking_space:
        remain_car_parking_space -= new_car
        car_parked += new_car
        car_cannot_park = 0
    else:
        car_cannot_park = new_car - remain_car_parking_space
        car_parked += remain_car_parking_space
        remain_car_parking_space = 0
    #new_car = 0
    return car_parked, remain_car_parking_space, car_cannot_park

# vehicle leave the parking lot events
def bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space):
    bicycle_left_failed = 0
    if new_bicycle == 0:
        return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed
    
    if bicycle_parked < new_bicycle:
        bicycle_left_failed = new_bicycle - bicycle_parked
        new_bicycle = bicycle_parked

    space = int(new_bicycle / 2)
    new_bicycle = new_bicycle % 2

    if space + remain_motorcycle_parking_space <= max_motorcycle_parking_space:
        remain_motorcycle_parking_space += space
        bicycle_parked -= space
    else:
        bicycle_left_failed += (space + remain_motorcycle_parking_space - max_motorcycle_parking_space)
        remain_motorcycle_parking_space = max_motorcycle_parking_space
        bicycle_parked = 0

    if new_bicycle == 1:
        if bicycle_parked % 2 == 1:
            bicycle_parked -= 1
        elif remain_motorcycle_parking_space <= max_motorcycle_parking_space:
            bicycle_parked -= 1
        elif bicycle_parked % 2 == 0:
            bicycle_left_failed += 1
        
    #new_bicycle = 0
    return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed

def motorcycle_left_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space):
    motorcycle_left_failed = 0
    if new_motorcycle == 0:
        return motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed
    
    if motorcycle_parked < new_motorcycle:
        motorcycle_left_failed = new_motorcycle - motorcycle_parked
        new_motorcycle = motorcycle_parked

    if new_motorcycle + remain_motorcycle_parking_space <= max_motorcycle_parking_space:
        remain_motorcycle_parking_space += new_motorcycle
        motorcycle_parked -= new_motorcycle
    else:
        motorcycle_left_failed += (new_motorcycle + remain_motorcycle_parking_space - max_motorcycle_parking_space)
        remain_motorcycle_parking_space = max_motorcycle_parking_space
        motorcycle_parked = 0
        
    #new_motorcycle = 0
    return motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed

def car_left_event(new_car, car_parked, remain_car_parking_space, max_car_parking_space):
    car_left_failed = 0
    if new_car == 0:
        return car_parked, remain_car_parking_space, car_left_failed
    
    if car_parked < new_car:
        car_left_failed = new_car - car_parked
        new_car = car_parked

    if new_car + remain_car_parking_space <= max_car_parking_space:
        remain_car_parking_space += new_car
        car_parked -= new_car
    else:
        car_left_failed += (new_car + remain_car_parking_space - max_car_parking_space)
        remain_car_parking_space = max_car_parking_space
        car_parked = 0
        
    #new_car = 0
    return car_parked, remain_car_parking_space, car_left_failed

