"""
Title: Events for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131219, 1131218, 1131217, 1131216
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
import random
import numpy as np

### function
## vehicle enter the parking lot events
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

    return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park

def vehicle_parked_event(new_vehicle, vehicle_parked, remain_vehicle_parking_space):
    if new_vehicle == 0:
        return vehicle_parked, remain_vehicle_parking_space, vehicle_cannot_park

    if new_vehicle <= remain_vehicle_parking_space:
        remain_vehicle_parking_space -= new_vehicle
        vehicle_parked += new_vehicle
        vehicle_cannot_park = 0
    else:
        vehicle_cannot_park = new_vehicle - remain_vehicle_parking_space
        vehicle_parked += remain_vehicle_parking_space
        remain_vehicle_parking_space = 0

    return vehicle_parked, remain_vehicle_parking_space, vehicle_cannot_park

## vehicle leave the parking lot events
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
        bicycle_parked -= (2 * space)
    else:
        bicycle_left_failed += (2 * (space + remain_motorcycle_parking_space - max_motorcycle_parking_space))
        remain_motorcycle_parking_space = max_motorcycle_parking_space
        bicycle_parked = 0

    if new_bicycle == 1:
        if bicycle_parked % 2 == 1:
            bicycle_parked -= 1
            remain_motorcycle_parking_space += 1
        elif remain_motorcycle_parking_space <= max_motorcycle_parking_space:
            bicycle_parked -= 1
        elif bicycle_parked % 2 == 0:
            bicycle_left_failed += 1
        
    return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed

def vehicle_left_event(new_vehicle, vehicle_parked, remain_vehicle_parking_space, max_vehicle_parking_space):
    vehicle_left_failed = 0
    if new_vehicle == 0:
        return vehicle_parked, remain_vehicle_parking_space, vehicle_left_failed
    
    if vehicle_parked < new_vehicle:
        vehicle_left_failed = new_vehicle - vehicle_parked
        new_vehicle = vehicle_parked

    if new_vehicle + remain_vehicle_parking_space <= max_vehicle_parking_space:
        remain_vehicle_parking_space += new_vehicle
        vehicle_parked -= new_vehicle
    else:
        vehicle_left_failed += (new_vehicle + remain_vehicle_parking_space - max_vehicle_parking_space)
        remain_vehicle_parking_space = max_vehicle_parking_space
        vehicle_parked = 0
        
    return vehicle_parked, remain_vehicle_parking_space, vehicle_left_failed

