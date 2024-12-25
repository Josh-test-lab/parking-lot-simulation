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
import matplotlib.pyplot as plt

### main program

## scenario 1
# initial value file path
path_to_initial_value_json_file = r'scenario\scenario_1\initial_values_for_scenario_1 copy.json'
# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

i = 3
for hour in range(87600):
    print(f'car_parked: {result[i][hour][0]}, motorcycle_parked: {result[i][hour][1]}, bicycle_parked: {result[i][hour][2]}')

a = []
for hour in range(24,48):
    a.append(result[1][hour][2] + result[1][hour][3])
x = range(24)
plt.figure(figsize=(10, 5))
plt.plot(x, a, marker='o', label='Data Points')
plt.title('Plot of Data Points')
plt.xlabel('Hour (0 to 23)')
plt.ylabel('Values')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(x)  # Ensure x-axis ticks match the data
plt.legend()
plt.tight_layout()
plt.show()




## scenario 2
# initial value file path
path_to_initial_value_json_file = r'scenario\scenario_2\initial_values_for_scenario_2.json'
# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

i = 3
for hour in range(87600):
    print(f'car_parked: {result[2][hour][0]}, motorcycle_parked: {result[i][hour][1]}, bicycle_parked: {result[i][hour][2]}')

a = []
for hour in range(24,48):
    a.append(result[1][hour][2] + result[1][hour][3])
x = range(24)
plt.figure(figsize=(10, 5))
plt.plot(x, a, marker='o', label='Data Points')
plt.title('Plot of Data Points')
plt.xlabel('Hour (0 to 23)')
plt.ylabel('Values')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(x)  # Ensure x-axis ticks match the data
plt.legend()
plt.tight_layout()
plt.show()




## scenario 3
# initial value file path
path_to_initial_value_json_file = r'scenario\scenario_3\initial_values_for_scenario_3.json'
# simulate the parking lot
result = parking_simulate(path_to_initial_value_json_file)
print(f'CPU time is {result[5]} seconds.')

i = 3
for hour in range(87600):
    print(f'car_parked: {result[2][hour][0]}, motorcycle_parked: {result[i][hour][1]}, bicycle_parked: {result[i][hour][2]}')

a = []
for hour in range(24,48):
    a.append(result[1][hour][2] + result[1][hour][3])
x = range(24)
plt.figure(figsize=(10, 5))
plt.plot(x, a, marker='o', label='Data Points')
plt.title('Plot of Data Points')
plt.xlabel('Hour (0 to 23)')
plt.ylabel('Values')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(x)  # Ensure x-axis ticks match the data
plt.legend()
plt.tight_layout()
plt.show()


b = [[] for _ in range(24)]
for hour in range(87600):
    clock_ = result[0][hour][1]
    b[clock_].append(result[1][hour][0] + result[1][hour][1])
b = np.mean(b, axis=1)
b

