"""
Title: Main program for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131225, 1131224, 1131223, 1131222, 1131220, 1131219, 1131218, 1131217, 1131216
Reference: Class of Simulation Study by C. Wang at 2024 fall

Note: This is the main code of simulation. For simulation of different scenarios, we will use the function `parking_simulate()` in `function.py`.
"""

### import module
from event import *
from function import *
import os

### main program

## scenario 1
# file path
path_to_initial_value_json_file = r'scenario\scenario_1\initial_values_for_scenario_1.json'
if not os.path.exists('scenario\\scenario_1\\data_per_hour'):
    os.makedirs('scenario\\scenario_1\\data_per_hour')
file_name_data_per_hour = r'scenario\scenario_1\data_per_hour\result_fordata_per_hour_for_scenario_1.csv'
if not os.path.exists('scenario\\scenario_1\\average_per_hour'):
    os.makedirs('scenario\\scenario_1\\average_per_hour')
file_name_average_per_hour = r'scenario\scenario_1\average_per_hour\result_for_average_per_hour_for_scenario_1.csv'

# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

# save the results
data_per_hour, average_per_hour = save_result_to_csv(result, path_to_initial_value_json_file, file_name_data_per_hour, file_name_average_per_hour)

# store results to pictures
#save_result_to_picture_per_day(data_per_hour, 'scenario\\scenario_1\\data_per_hour')
save_result_to_picture_per_day(average_per_hour, 'scenario\\scenario_1\\average_per_hour')





## scenario 2
# file path
path_to_initial_value_json_file = r'scenario\scenario_2\initial_values_for_scenario_2.json'
if not os.path.exists('scenario\\scenario_2\\data_per_hour'):
    os.makedirs('scenario\\scenario_2\\data_per_hour')
file_name_data_per_hour = r'scenario\scenario_2\data_per_hour\result_fordata_per_hour_for_scenario_2.csv'
if not os.path.exists('scenario\\scenario_2\\average_per_hour'):
    os.makedirs('scenario\\scenario_2\\average_per_hour')
file_name_average_per_hour = r'scenario\scenario_2\average_per_hour\result_for_average_per_hour_for_scenario_2.csv'

# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

# save the results
data_per_hour, average_per_hour = save_result_to_csv(result, path_to_initial_value_json_file, file_name_data_per_hour, file_name_average_per_hour)

# store results to pictures
#save_result_to_picture_per_day(data_per_hour, 'scenario\\scenario_2\\data_per_hour')
save_result_to_picture_per_day(average_per_hour, 'scenario\\scenario_2\\average_per_hour')





## scenario 3
# file path
path_to_initial_value_json_file = r'scenario\scenario_3\initial_values_for_scenario_3.json'
if not os.path.exists('scenario\\scenario_3\\data_per_hour'):
    os.makedirs('scenario\\scenario_3\\data_per_hour')
file_name_data_per_hour = r'scenario\scenario_3\data_per_hour\result_fordata_per_hour_for_scenario_3.csv'
if not os.path.exists('scenario\\scenario_3\\average_per_hour'):
    os.makedirs('scenario\\scenario_3\\average_per_hour')
file_name_average_per_hour = r'scenario\scenario_3\average_per_hour\result_for_average_per_hour_for_scenario_3.csv'

# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

# save the results
data_per_hour, average_per_hour = save_result_to_csv(result, path_to_initial_value_json_file, file_name_data_per_hour, file_name_average_per_hour)

# store results to pictures
#save_result_to_picture_per_day(data_per_hour, 'scenario\\scenario_3\\data_per_hour')
save_result_to_picture_per_day(average_per_hour, 'scenario\\scenario_3\\average_per_hour')





