"""
Title: Testing for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih
Version: 1131224, 1131223
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
from event import *
import json
import math

### main program
with open(r'scenario\initial_values_example.json', 'r', encoding = 'utf-8') as file:
    initial_value = json.load(file)

## initial values
t = 0 
clock = 0 
max_simulation_time = initial_value['simulation_time']['max_simulation_time']['value']

# number of max parking spaces
max_car_parking_space = initial_value['parking_spaces']['max_car_parking_space']['value']
max_motorcycle_parking_space = initial_value['parking_spaces']['max_motorcycle_parking_space']['value']
if max_car_parking_space == -1:
    max_car_parking_space = math.inf
if max_motorcycle_parking_space == -1:
    max_motorcycle_parking_space = math.inf

# number of max bicycles which parked in one motorcycle space
max_bicycle_parked_in_a_motorcycle_space = initial_value['parking_spaces']['max_bicycle_parked_in_a_motorcycle_space']['value']

# number of spaces which be parked now
car_parked = initial_value['number_of_spaces_parked']['car_parked']['value']
motorcycle_parked = initial_value['number_of_spaces_parked']['motorcycle_parked']['value']
bicycle_parked = initial_value['number_of_spaces_parked']['bicycle_parked']['value']

# number of spaces which can be parked
remain_car_parking_space = max_car_parking_space - car_parked
remain_motorcycle_parking_space = max_motorcycle_parking_space - motorcycle_parked - int(bicycle_parked / max_bicycle_parked_in_a_motorcycle_space) - (1 if bicycle_parked % max_bicycle_parked_in_a_motorcycle_space != 0 else 0)

while True:
    while True:
        try:
            user_input = input("Enter the number of new car, motorcycle, and bicycle (separated by spaces): ").split()
            if len(user_input) != 3:
                raise ValueError("You must enter exactly 3 values.")
            [new_car, new_motorcycle, new_bicycle] = map(int, user_input)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
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
        bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park = bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
        print(f'bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park]}')
    else:
        new_bicycle = -new_bicycle
        bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
        print(f'bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed]}')




