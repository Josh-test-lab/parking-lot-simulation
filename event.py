"""
Title: Events for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131223, 1131219, 1131218, 1131217, 1131216
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
import numpy as np

### function
## vehicle enter the parking lot events
# def bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space):
#     bicycle_cannot_park = 0
#     if new_bicycle == 0:
#         return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park
    
#     space = int(new_bicycle / 2)
#     new_bicycle = new_bicycle % 2

#     if space <= remain_motorcycle_parking_space:
#         remain_motorcycle_parking_space -= space
#         bicycle_parked += (2 * space)
#     else:
#         bicycle_cannot_park = 2 * (space - remain_motorcycle_parking_space)
#         bicycle_parked += (2 * remain_motorcycle_parking_space)
#         remain_motorcycle_parking_space = 0

#     if new_bicycle == 1:
#         if bicycle_parked % 2 == 1:
#             bicycle_parked += 1
#         elif remain_motorcycle_parking_space > 0:
#             bicycle_parked += 1
#             remain_motorcycle_parking_space -= 1
#         elif remain_motorcycle_parking_space <= 0:
#             bicycle_cannot_park += 1

#     return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park

def bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space = 2):
    bicycle_cannot_park = 0
    if new_bicycle == 0:
        return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park
    if max_bicycle_parked_in_a_motorcycle_space == 1:
        return vehicle_parked_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space)
    
    space = int(new_bicycle / max_bicycle_parked_in_a_motorcycle_space)
    new_bicycle = new_bicycle % max_bicycle_parked_in_a_motorcycle_space

    if space <= remain_motorcycle_parking_space:
        remain_motorcycle_parking_space -= space
        bicycle_parked += (max_bicycle_parked_in_a_motorcycle_space * space)
    else:
        bicycle_cannot_park = max_bicycle_parked_in_a_motorcycle_space * (space - remain_motorcycle_parking_space)
        bicycle_parked += (max_bicycle_parked_in_a_motorcycle_space * remain_motorcycle_parking_space)
        remain_motorcycle_parking_space = 0
        while bicycle_parked % max_bicycle_parked_in_a_motorcycle_space != 0 and bicycle_cannot_park > 0:
            bicycle_parked += 1
            bicycle_cannot_park -= 1

    while new_bicycle > 0:
        if bicycle_parked % max_bicycle_parked_in_a_motorcycle_space != 0:
            bicycle_parked += 1
        elif remain_motorcycle_parking_space > 0:
            bicycle_parked += 1
            remain_motorcycle_parking_space -= 1
        elif remain_motorcycle_parking_space <= 0:
            bicycle_cannot_park += 1
        new_bicycle -= 1

    return bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park

def vehicle_parked_event(new_vehicle, vehicle_parked, remain_vehicle_parking_space):
    vehicle_cannot_park = 0
    if new_vehicle == 0:
        return vehicle_parked, remain_vehicle_parking_space, vehicle_cannot_park

    if new_vehicle <= remain_vehicle_parking_space:
        remain_vehicle_parking_space -= new_vehicle
        vehicle_parked += new_vehicle
    else:
        vehicle_cannot_park = new_vehicle - remain_vehicle_parking_space
        vehicle_parked += remain_vehicle_parking_space
        remain_vehicle_parking_space = 0

    return vehicle_parked, remain_vehicle_parking_space, vehicle_cannot_park

## vehicle leave the parking lot events
# def bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space):
#     bicycle_left_failed = 0
#     if new_bicycle == 0:
#         return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed
    
#     if bicycle_parked < new_bicycle:
#         bicycle_left_failed = new_bicycle - bicycle_parked
#         new_bicycle = bicycle_parked

#     space = int(new_bicycle / 2)
#     new_bicycle = new_bicycle % 2

#     if space + remain_motorcycle_parking_space <= max_motorcycle_parking_space:
#         remain_motorcycle_parking_space += space
#         bicycle_parked -= (2 * space)
#     else:
#         bicycle_left_failed += (2 * (space + remain_motorcycle_parking_space - max_motorcycle_parking_space))
#         remain_motorcycle_parking_space = max_motorcycle_parking_space
#         bicycle_parked = 0

#     if new_bicycle == 1:
#         if bicycle_parked % 2 == 1:
#             bicycle_parked -= 1
#             remain_motorcycle_parking_space += 1
#         elif remain_motorcycle_parking_space <= max_motorcycle_parking_space:
#             bicycle_parked -= 1
#         elif bicycle_parked % 2 == 0:
#             bicycle_left_failed += 1
        
#     return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed

def bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space = 2):
    bicycle_left_failed = 0
    if new_bicycle == 0:
        return bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed
    if max_bicycle_parked_in_a_motorcycle_space == 1:
        return vehicle_left_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space)
    
    if bicycle_parked < new_bicycle:
        bicycle_left_failed = new_bicycle - bicycle_parked
        new_bicycle = bicycle_parked

    space = int(new_bicycle / max_bicycle_parked_in_a_motorcycle_space)
    new_bicycle = new_bicycle % max_bicycle_parked_in_a_motorcycle_space

    if space + remain_motorcycle_parking_space <= max_motorcycle_parking_space:
        remain_motorcycle_parking_space += space
        bicycle_parked -= (max_bicycle_parked_in_a_motorcycle_space * space)
    else:
        bicycle_left_failed += (max_bicycle_parked_in_a_motorcycle_space * (space + remain_motorcycle_parking_space - max_motorcycle_parking_space))
        remain_motorcycle_parking_space = max_motorcycle_parking_space
        bicycle_parked = 0

    while new_bicycle > 0:
        if bicycle_parked >= new_bicycle:
            if bicycle_parked % max_bicycle_parked_in_a_motorcycle_space == 1:
                bicycle_parked -= 1
                remain_motorcycle_parking_space += 1
            else:
                bicycle_parked -= 1
        else:
            bicycle_left_failed += new_bicycle
            break
        new_bicycle -= 1
        
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

def vehicle_occupied_long_term_event(car_parked, motorcycle_parked, bicycle_parked, number_of_vehicle_occupied_long_term, poisson_dist = False):
    car_occupied_long_term, motorcycle_occupied_long_term, bicycle_occupied_long_term = number_of_vehicle_occupied_long_term['car']['value'], number_of_vehicle_occupied_long_term['motorcycle']['value'], number_of_vehicle_occupied_long_term['bicycle']['value']
    
    if poisson_dist:
        car_occupied_long_term, motorcycle_occupied_long_term, bicycle_occupied_long_term = np.random.poisson(lam = car_occupied_long_term), np.random.poisson(lam = motorcycle_occupied_long_term), np.random.poisson(lam = bicycle_occupied_long_term)
    
    car_occupied_long_term, motorcycle_occupied_long_term, bicycle_occupied_long_term = min(car_occupied_long_term, car_parked), min(motorcycle_occupied_long_term, motorcycle_parked), min(bicycle_occupied_long_term, bicycle_parked)

    return car_occupied_long_term, motorcycle_occupied_long_term, bicycle_occupied_long_term




