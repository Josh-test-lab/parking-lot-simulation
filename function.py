"""
Title: Functions for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131225, 1131224, 1131223, 1131222, 1131220, 1131218
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
import random
from event import *
import json
import time
import math
import numpy as np

### function
def load_initial_values(path_to_initial_value_json_file):
    """
    load 'initial_values.json' file
    """
    with open(path_to_initial_value_json_file, 'r', encoding = 'utf-8') as file:
        initial_value = json.load(file)

    return initial_value

def generate_new_passengers_per_hour(passenger_probability_per_hour, clock):
    """
    generate passengers per hour for enter and leave the station
    generate by normal distribution, first array is mean, second arrray is standard deviation
    """
    mean = passenger_probability_per_hour['mean']['value'][clock]
    std = passenger_probability_per_hour['std']['value'][clock]
    passenger_enter_rate = passenger_probability_per_hour['passenger_enter_rate']['value'][clock]
    population = int(round(abs(np.random.normal(loc = mean, scale = std)), 0))
    # [passenger_enter, passenger_leave]
    passengers = [int(population * passenger_enter_rate), int(population * (1 - passenger_enter_rate))]

    return passengers

def generate_new_vehicles_per_hour(vehicle_probability_per_hour, clock, passengers):
    """
    generate new vehicles per hour for enter and leave the parking lot
    """
    car_park_probability = vehicle_probability_per_hour['car']['park'][clock]
    car_leave_probability = vehicle_probability_per_hour['car']['leave'][clock]
    motorcycle_park_probability = vehicle_probability_per_hour['motorcycle']['park'][clock]
    motorcycle_leave_probability = vehicle_probability_per_hour['motorcycle']['leave'][clock]
    bicycle_park_probability = vehicle_probability_per_hour['bicycle']['park'][clock]
    bicycle_leave_probability = vehicle_probability_per_hour['bicycle']['leave'][clock]
    
    car = [int(round(passengers[0] * car_park_probability), 0), int(round(passengers[1] * car_leave_probability), 0)]
    motorcycle = [int(round(passengers[0] * motorcycle_park_probability), 0), int(round(passengers[1] * motorcycle_leave_probability), 0)]
    bicycle = [int(round(passengers[0] * bicycle_park_probability), 0), int(round(passengers[1] * bicycle_leave_probability), 0)]

    return [car, motorcycle, bicycle]

def parking_simulate(path_to_initial_value_json_file):
    ## load 'initial_values.json' file
    initial_value = load_initial_values(path_to_initial_value_json_file)

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
    
    # passenger and vehicle probability per hour
    passenger_probability_per_hour = initial_value['passenger_probability_per_hour']
    vehicle_probability_per_hour = initial_value['vehicle_probability_per_hour']

    # store counters
    parked = []
    parked_failed = []
    left_failed = []
    passengers_list = []
    clocks = []
    
    ## simulation 
    start_time = time.time()
    while t < max_simulation_time:
        # generate passengers and vehicles
        passengers = generate_new_passengers_per_hour(passenger_probability_per_hour, clock)
        new_vehicles = generate_new_vehicles_per_hour(vehicle_probability_per_hour, clock, passengers)
    
        # parking events for passengers who will aboard the train
        """
        index of 'new_vehicles' means
        first index is 0: car, 1: motorcycle, 2: bicycle
        third index is 0: enter, 1: leave
        """
        new_car, new_motorcycle, new_bicycle = new_vehicles[0][0], new_vehicles[1][0], new_vehicles[2][0]
        car_parked, remain_car_parking_space, car_cannot_park = vehicle_parked_event(new_car, car_parked, remain_car_parking_space)
        motorcycle_cannot_park, bicycle_cannot_park = 0, 0

        # debug
        # print(f't = {t}, clock = {clock}, new_car: {new_car}, new_motorcycle: {new_motorcycle}, new_bicycle: {new_bicycle}, walker: {int(round(np.sum(passengers) - np.sum(new_vehicles), 0))}')

        while new_motorcycle >= 0 and new_bicycle >= 0:
            if random.random() < 0.5:
                motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park_counter = vehicle_parked_event(1, motorcycle_parked, remain_motorcycle_parking_space)
                motorcycle_cannot_park += motorcycle_cannot_park_counter
                new_motorcycle -= 1
            else:
                bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park_counter = bicycle_parked_in_motorcycle_space_event(1, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
                bicycle_cannot_park += bicycle_cannot_park_counter
                new_bicycle -= 1
        if new_motorcycle != 0:
            motorcycle_parked, remain_motorcycle_parking_space, motorcycle_cannot_park_counter = vehicle_parked_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space)
            motorcycle_cannot_park += motorcycle_cannot_park_counter
        else:
            bicycle_parked, remain_motorcycle_parking_space, bicycle_cannot_park_counter = bicycle_parked_in_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)
            bicycle_cannot_park += bicycle_cannot_park_counter

        # leaving events for passengers who will leave the station
        """
        index of 'new_vehicles' means
        first index is 0: car, 1: motorcycle, 2: bicycle
        third index is 0: enter, 1: leave
        """
        new_car, new_motorcycle, new_bicycle = new_vehicles[0][1], new_vehicles[1][1], new_vehicles[2][1]
        car_parked, remain_car_parking_space, car_left_failed = vehicle_left_event(new_car, car_parked, remain_car_parking_space, max_car_parking_space)
        motorcycle_parked, remain_motorcycle_parking_space, motorcycle_left_failed = vehicle_left_event(new_motorcycle, motorcycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space)
        bicycle_parked, remain_motorcycle_parking_space, bicycle_left_failed = bicycle_left_motorcycle_space_event(new_bicycle, bicycle_parked, remain_motorcycle_parking_space, max_motorcycle_parking_space, max_bicycle_parked_in_a_motorcycle_space)

        # store counters
        parked.append([car_parked, motorcycle_parked, bicycle_parked])
        parked_failed.append([car_cannot_park, motorcycle_cannot_park, bicycle_cannot_park])
        left_failed.append([car_left_failed, motorcycle_left_failed, bicycle_left_failed])
        # passenger_list: [passenger_enter, passenger_leave, car_in, car_out, motorcycle_in, motorcycle_out, bicycle_in, bicycle_out, walk]
        passengers_list.append([passengers[0], passengers[1], new_vehicles[0][0], new_vehicles[0][1], new_vehicles[1][0], new_vehicles[1][1], new_vehicles[2][0], new_vehicles[2][1], int(round(np.sum(passengers) - np.sum(new_vehicles), 0))])
        clocks.append([t, clock])

        # update time variables
        if clock == 23:
            clock = 0
        else:
            clock += 1
        t += 1

    end_time = time.time()
    CPU_time = end_time - start_time

    return clocks, passengers_list, parked, parked_failed, left_failed, CPU_time


