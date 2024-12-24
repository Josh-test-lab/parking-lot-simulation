"""
Title: Main program for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131222, 1131220, 1131219, 1131218, 1131217, 1131216
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
from event import *

### main program
# number of max parking spaces
max_car_parking_space = 90
max_motorcycle_parking_space = 5

# number of spaces which be parked now
car_parked = 0
motorcycle_parked = 0
bicycle_parked = 0

# number of spaces which can be parked
remain_car_parking_space = max_car_parking_space - car_parked
remain_motorcycle_parking_space = max_motorcycle_parking_space - motorcycle_parked - int(bicycle_parked / 2) - (bicycle_parked % 2)

# number of new vehicle enter/leave the parking lot
new_car = 0
new_motorcycle = 0
new_bicycle = 0

while True:
    [new_car, new_motorcycle, new_bicycle] = input("Enter the number of new car, motorcycle, and bicycle: ").split()
    [new_car, new_motorcycle, new_bicycle] = [int(new_car), int(new_motorcycle), int(new_bicycle)]
    if new_car > 0:
        car_parked, remain_car_parking_space, car_cannot_park = vehicle_parked_event(new_car, car_parked, remain_car_parking_space)
        print(f'car_parked, remain_car_parking_space, car_cannot_park = {[car_parked, remain_car_parking_space, car_cannot_park]}')
    else:
        new_car = -new_car
        car_parked, remain_car_parking_space, car_left_failed = vehicle_left_event(new_car, car_parked, remain_car_parking_space, max_car_parking_space)
        print(f'car_parked, remain_car_parking_space, car_left_failed = {[car_parked, remain_car_parking_space, car_left_failed]}')


    if new_motorcycle > 0:
        motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park = vehicle_parked_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space)
        print(f'motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park = {[motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park]}')
    else:
        new_motorcycle = -new_motorcycle
        motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed = vehicle_left_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space)
        print(f'motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed = {[motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed]}')


    if new_bicycle > 0:
        bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park = bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space = 2)
        print(f'bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park]}')
    else:
        new_bicycle = -new_bicycle
        bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space = 2)
        print(f'bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed]}')




