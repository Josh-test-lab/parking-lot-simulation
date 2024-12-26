"""
Title: Testing for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih
Version: 1131225, 1131224, 1131223
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

print(f'\033[33mWelcome to testing the enter and leave events for the parking lot. The config will be put at `scenario\initial_values_example.json`, please enter positive integers to simulate vehicles parking, and negative intergers for vehicles leaving. Separated by spaces when you enter numbers. \033[0m')
print(f'The current initial value is')
print(f'max parking space for car, motorcycle is {[max_car_parking_space, max_motorcycle_parking_space]}.')
print(f'max bicycle parked in a motorcycle space is {[max_bicycle_parked_in_a_motorcycle_space]}.')
print(f'parked by car, motorcycle, bicycle is {[car_parked, motorcycle_parked, bicycle_parked]}.')
count = 1
while True:
    while True:
        try:
            user_input = input(f'{count}. \033[33mEnter the number of new car, motorcycle, and bicycle (separated by spaces): \033[0m').split()
            if len(user_input) != 3:
                raise ValueError('You must enter exactly 3 values')
            [new_car, new_motorcycle, new_bicycle] = map(int, user_input)
            break
        except ValueError as e:
            print(f'\033[31mInvalid input: {e}. Please try again.\033[0m')
    if new_car > 0:
        car_parked, remain_car_parking_space, car_cannot_park = vehicle_parked_event(new_car, car_parked, remain_car_parking_space)
        print(f'{'car_parked': <{20}}, {'remain_car_parking_space': <{35}}, {'car_cannot_park': <{26}}= {[car_parked, remain_car_parking_space, car_cannot_park]}')
    else:
        new_car = -new_car
        car_parked, remain_car_parking_space, car_left_failed = vehicle_left_event(new_car, car_parked, remain_car_parking_space, max_car_parking_space)
        print(f'{'car_parked': <{20}}, {'remain_car_parking_space': <{35}}, {'car_left_failed': <{26}} = {[car_parked, remain_car_parking_space, car_left_failed]}')


    if new_motorcycle > 0:
        motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park = vehicle_parked_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space)
        print(f'{'motorcycle_parked': <{20}}, {'remain_motorcycle_parking_space': <{35}}, {'motorcycle_cannot_park': <{26}} = {[motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park]}')
    else:
        new_motorcycle = -new_motorcycle
        motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed = vehicle_left_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space)
        print(f'{'motorcycle_parked': <{20}}, {'remain_motorcycle_parking_space': <{35}}, {'motorcycle_left_failed': <{26}} = {[motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed]}')


    if new_bicycle > 0:
        bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park = bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
        print(f'{'bicycle_parked': <{20}}, {'remain_motorcycle_parking_space': <{35}}, {'bicycle_cannot_park': <{26}} = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park]}')
    else:
        new_bicycle = -new_bicycle
        bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
        print(f'{'bicycle_parked': <{20}}, {'remain_motorcycle_parking_space': <{35}}, {'bicycle_left_failed': <{26}} = {[bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed]}')

    count += 1
    print(f' ')



