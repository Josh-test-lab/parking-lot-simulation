"""
Information:
    Title = 'Functions for parking model for the parking lot in Zhixue station'
    Author = 'Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee'
    Version = [1131218]
    Reference = ['Class of Simulation Study by C. Wang at 2024 fall']
"""

### import module
import json

### function
def load_initial_value():
    # load 'initial_values.json' file
    with open('initial_values.json', 'r', encoding = 'utf-8') as file:
        initial_value = json.load(file)

    # Simulation time
    max_simulation_time = initial_value['simulation_time']['max_simulation_time']['value']  # total time

    # Parking spaces
    max_car_parking_space = initial_value['parking_spaces']['max_car_parking_space']['value']  # max car spaces
    max_motorcycle_parking_space = initial_value['parking_spaces']['max_motorcycle_parking_space']['value']  # max motorcycle spaces

    # Number of spaces parked
    car_parked = initial_value['number_of_spaces_parked']['car_parked']['value']  # cars parked
    motorcycle_parked = initial_value['number_of_spaces_parked']['motorcycle_parked']['value']  # motorcycles parked
    bicycle_parked = initial_value['number_of_spaces_parked']['bicycle_parked']['value']  # bicycles parked

    return max_simulation_time, max_car_parking_space, max_motorcycle_parking_space, car_parked, motorcycle_parked, bicycle_parked






