"""
Title: Functions for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131227, 1131226, 1131225, 1131224, 1131223, 1131222, 1131220, 1131218
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
import random
from event import *
import json
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os
import tqdm

### function
def load_initial_values(path_to_initial_value_json_file):
    """
    load 'initial_values.json' file
    """
    with open(path_to_initial_value_json_file, 'r', encoding = 'utf-8') as file:
        initial_value = json.load(file)

    return initial_value

def generate_new_passengers_per_hour(passenger_probability_per_hour, clock, normal_dist = False):
    """
    generate passengers per hour for enter and leave the station
    generate by normal distribution, first array is mean, second arrray is standard deviation
    """
    mean = passenger_probability_per_hour['mean']['value'][clock]
    std = passenger_probability_per_hour['std']['value'][clock]
    passenger_enter_rate = passenger_probability_per_hour['passenger_enter_rate']['value'][clock]
    if normal_dist:
        population = int(round(abs(np.random.normal(loc = mean, scale = std)), 0))
    else:
        population = np.random.poisson(lam = mean)
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
    
    car = [int(round(passengers[0] * car_park_probability, 0)), int(round(passengers[1] * car_leave_probability, 0))]
    motorcycle = [int(round(passengers[0] * motorcycle_park_probability, 0)), int(round(passengers[1] * motorcycle_leave_probability, 0))]
    bicycle = [int(round(passengers[0] * bicycle_park_probability, 0)), int(round(passengers[1] * bicycle_leave_probability, 0))]

    return car, motorcycle, bicycle

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
    number_of_vehicle_occupied_long_term = initial_value['number_of_vehicle_occupied_long_term']

    # store counters
    parked = []
    parked_failed = []
    left_failed = []
    passengers_list = []
    clocks = []
    reamin_space = []
    
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

        while new_motorcycle > 0 and new_bicycle > 0:
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
        clocks.append([t, clock])
        reamin_space.append([remain_car_parking_space, remain_motorcycle_parking_space])
        # passenger_list: [passenger_enter, passenger_leave, car_in, car_out, motorcycle_in, motorcycle_out, bicycle_in, bicycle_out, walker]
        passengers_list.append([passengers[0], passengers[1], new_vehicles[0][0], new_vehicles[0][1], new_vehicles[1][0], new_vehicles[1][1], new_vehicles[2][0], new_vehicles[2][1], int(round(np.sum(passengers) - np.sum(new_vehicles), 0))])

        # update time variables
        if clock == 23:
            clock = 0
        else:
            clock += 1
        t += 1

    end_time = time.time()
    CPU_time = end_time - start_time

    return clocks, passengers_list, parked, parked_failed, left_failed, reamin_space, CPU_time

def save_result_to_csv(result, path_to_initial_value_json_file, file_name_data_per_hour, file_name_average_per_hour):
    initial_value = load_initial_values(path_to_initial_value_json_file)
    max_simulation_time = initial_value['simulation_time']['max_simulation_time']['value']
    column_mappings = [
        {'name': 'clock', 'result_idx': 0, 'sub_idx': 1},
        {'name': 'passenger_enter', 'result_idx': 1, 'sub_idx': 0},
        {'name': 'passenger_leave', 'result_idx': 1, 'sub_idx': 1},
        {'name': 'car_enter', 'result_idx': 1, 'sub_idx': 2},
        {'name': 'car_leave', 'result_idx': 1, 'sub_idx': 3},
        {'name': 'motorcycle_enter', 'result_idx': 1, 'sub_idx': 4},
        {'name': 'motorcycle_leave', 'result_idx': 1, 'sub_idx': 5},
        {'name': 'bicycle_enter', 'result_idx': 1, 'sub_idx': 6},
        {'name': 'bicycle_leave', 'result_idx': 1, 'sub_idx': 7},
        {'name': 'walker', 'result_idx': 1, 'sub_idx': 8},
        {'name': 'car_parked', 'result_idx': 2, 'sub_idx': 0},
        {'name': 'motorcycle_parked', 'result_idx': 2, 'sub_idx': 1},
        {'name': 'bicycle_parked', 'result_idx': 2, 'sub_idx': 2},
        {'name': 'car_cannot_park', 'result_idx': 3, 'sub_idx': 0},
        {'name': 'motorcycle_cannot_park', 'result_idx': 3, 'sub_idx': 1},
        {'name': 'bicycle_cannot_park', 'result_idx': 3, 'sub_idx': 2},
        {'name': 'car_left_failed', 'result_idx': 4, 'sub_idx': 0},
        {'name': 'motorcycle_left_failed', 'result_idx': 4, 'sub_idx': 1},
        {'name': 'bicycle_left_failed', 'result_idx': 4, 'sub_idx': 2},
        {'name': 'remain_car_parking_space', 'result_idx': 5, 'sub_idx': 0},
        {'name': 'remain_motorcycle_parking_space', 'result_idx': 5, 'sub_idx': 1}
    ]

    data_per_hour = pd.DataFrame(index = range(max_simulation_time), columns = [col['name'] for col in column_mappings])

    for col in tqdm.tqdm(column_mappings):
        data_per_hour[col['name']] = [result[col['result_idx']][hour][col['sub_idx']] for hour in range(max_simulation_time)]
    data_per_hour['CPU_time(in second)'] = [result[6]] + [None] * (len(data_per_hour) - 1)
    data_per_hour.to_csv(file_name_data_per_hour, index = False)
    print(f'Date frame `data_per_hour` has been saved to "{file_name_data_per_hour}".')

    average_per_hour = data_per_hour.groupby('clock').mean().reset_index()
    average_per_hour['CPU_time(in second)'] = [result[6]] + [None] * (len(average_per_hour) - 1)
    average_per_hour.to_csv(file_name_average_per_hour, index = False)
    print(f'Date frame `average_per_hour` has been saved to "{file_name_average_per_hour}".')

    return data_per_hour, average_per_hour

def save_result_to_picture_per_day(dataset, path_to_initial_value_json_file, path_to_save_picture):
    initial_value = load_initial_values(path_to_initial_value_json_file)
    max_car_parking_space = initial_value['parking_spaces']['max_car_parking_space']['value']
    max_motorcycle_parking_space = initial_value['parking_spaces']['max_motorcycle_parking_space']['value']
    max_bicycle_parked_in_a_motorcycle_space = initial_value['parking_spaces']['max_bicycle_parked_in_a_motorcycle_space']['value']
    # define the groups of data to plot
    groups_to_plot = [
        ('passenger_enter', 'passenger_leave', 'passenger'),
        ('car_parked', 'car_enter', 'car_leave', 'car_cannot_park', 'car_left_failed'),
        ('motorcycle_parked', 'motorcycle_enter', 'motorcycle_leave', 'motorcycle_cannot_park', 'motorcycle_left_failed'),
        ('bicycle_parked', 'bicycle_enter', 'bicycle_leave', 'bicycle_cannot_park', 'bicycle_left_failed'),
        ('walker',),
        ('car_parked', 'motorcycle_parked', 'bicycle_parked'),
        ('car_enter', 'motorcycle_enter', 'bicycle_enter'),
        ('car_leave', 'motorcycle_leave', 'bicycle_leave'),
        ('car_cannot_park', 'motorcycle_cannot_park', 'bicycle_cannot_park'),
        ('car_left_failed', 'motorcycle_left_failed', 'bicycle_left_failed'),
        ('motorcycle_and_bicycle', 'motorcycle_parked', 'motorcycle_enter', 'motorcycle_leave', 'bicycle_parked', 'bicycle_enter', 'bicycle_leave')
    ]

    titles = [
        'passenger',
        'car',
        'motorcycle',
        'bicycle',
        'walker',
        'total parked',
        'total enter',
        'total leave',
        'total cannot park',
        'total left failed',
        'motorcycle and bicycle'
    ]

    hour = len(dataset)
    if hour < 24:
        raise ValueError('Not enough data to plot. At least 24 hours.')
    is_average = hour == 24

    for title in titles:
        os.makedirs(os.path.join(path_to_save_picture, title), exist_ok = True)

    y_values_map = {
        'passenger': lambda data: data['passenger_enter'] + data['passenger_leave'],
        'motorcycle_and_bicycle': lambda data: max_bicycle_parked_in_a_motorcycle_space * data['motorcycle_parked'] + data['bicycle_parked']
    }

    max_space_map = {
        'car': max_car_parking_space,
        'bicycle': max_bicycle_parked_in_a_motorcycle_space * max_motorcycle_parking_space,
        'motorcycle': max_motorcycle_parking_space,
        'motorcycle and bicycle': max_bicycle_parked_in_a_motorcycle_space * max_motorcycle_parking_space
    }

    threshold_map = {
        'car': lambda data: data['parking_space_threshold']['car']['value'],
        'bicycle': lambda data: data['parking_space_threshold']['motorcycle']['value'],
        'motorcycle': lambda data: data['parking_space_threshold']['motorcycle']['value'],
        'motorcycle and bicycle': lambda data: data['parking_space_threshold']['motorcycle']['value']
    }

    def configure_legend(ax, ax_right = None, bbox_to_anchor = (1.10, 1)):
        handles_left, labels_left = ax.get_legend_handles_labels()
        handles_right, labels_right = ax_right.get_legend_handles_labels() if ax_right else ([], [])
        combined_handles = handles_left + handles_right
        combined_labels = labels_left + labels_right
        plt.legend(combined_handles, combined_labels, loc = 'upper left', bbox_to_anchor = bbox_to_anchor)

    def save_plot(title, day, is_average, path_to_save_picture):
        filename = f'{path_to_save_picture}\\{title}\\{title}_for_day_{'average' if is_average else day + 1}.png'
        plt.tight_layout()
        plt.savefig(filename, dpi = 300)
        plt.close()

    for day in tqdm.tqdm(range(hour // 24)):
        daily_data = dataset.iloc[day * 24:(day + 1) * 24]

        # plot the data
        for group, title in zip(groups_to_plot, titles):
            plt.figure(figsize = (10, 6))
            for col in group:
                y_values = y_values_map.get(col, lambda data: data[col])(daily_data)
                plt.plot(daily_data['clock'], y_values, label = col)
                
            plt.xlabel('Hour')
            plt.xticks(np.arange(0, 24, 1))
            plt.ylabel(f'Values ({max_bicycle_parked_in_a_motorcycle_space} * motorcycle & 1 * bicycle)' if title == 'motorcycle and bicycle' else 'Values')
            plt.title(f'Hourly data for {title} in day {'average' if is_average else day + 1}')
            ax = plt.gca()
            ax_right = None
            if title in max_space_map and max_car_parking_space != -1 and max_motorcycle_parking_space != -1:
                threshold = threshold_map.get(title, lambda data: data[title])(initial_value)
                max_space = max_space_map[title]
                ax_right = ax.twinx()
                ax_right.set_ylim(ax.get_ylim())
                ax_right.yaxis.set_major_formatter(mtick.PercentFormatter(xmax = max_space))
                ax_right.set_ylabel('Percentage')
                ax_right.axhline(y = threshold * max_space, color = 'gray', linestyle = '--', linewidth = 1, label = f'{int(threshold * 100)}% threshold')
                ax_right.axhline(y = max_space, color = 'red', linestyle = '--', linewidth = 1, label = f'Maximum parking space')

            configure_legend(ax, ax_right)
            save_plot(title, day, is_average, path_to_save_picture)

    print(f'All pictures have been saved to "{path_to_save_picture}".')





    