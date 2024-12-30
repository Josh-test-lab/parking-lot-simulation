import numpy as np
from event import *
from function import *
import os

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

# save the results
data_per_hour, average_per_hour = save_result_to_csv(result, path_to_initial_value_json_file, file_name_data_per_hour, file_name_average_per_hour)


initial_value = load_initial_values(path_to_initial_value_json_file)
mean = initial_value["passenger_probability_per_hour"]['mean']['value']

num_passerger = data_per_hour['passenger_enter'] + data_per_hour['passenger_leave']

control_variate_estimate_list = []
for idx in ['car_parked', 'motorcycle_parked', 'bicycle_parked']:
    temp_mean_list = []
    temp_var_list = []
    temp_ub_list = []
    temp_lb_list = []
    for j in range(5, 24):
        indices = [j + 24*i for i in range(365)]
        cov = np.mean((data_per_hour[idx][indices] - average_per_hour[idx][j])*(num_passerger[indices] - mean[j]))
        c_optimal = -cov / mean[j]
        temp1 = average_per_hour[idx][j] + c_optimal*(np.mean(num_passerger[indices]) - mean[j])
        temp_mean_list.append(temp1)
        temp2 = np.var(data_per_hour[idx][indices] - c_optimal*(num_passerger[indices] - mean[j]), ddof=1)
        temp_var_list.append(temp2)
        temp3 = temp1 + 1.96*np.sqrt(temp2/len(indices))
        temp_ub_list.append(temp3)
        temp4 = temp1 - 1.96*np.sqrt(temp2/len(indices))
        temp_lb_list.append(temp4)
    control_variate_estimate_list.append(temp_mean_list)
    control_variate_estimate_list.append(temp_var_list)
    control_variate_estimate_list.append(temp_ub_list)
    control_variate_estimate_list.append(temp_lb_list)
control_variate_estimate_list = np.array(control_variate_estimate_list)

# Replace NaN with 0
control_variate_estimate_list = np.nan_to_num(control_variate_estimate_list, nan=0.0)



# car_parked
hours = list(range(5, 24))  # Assume 24 hours
sample_mean = control_variate_estimate_list[0]
sample_variance =control_variate_estimate_list[1]
upper_bound = control_variate_estimate_list[2]
lower_bound = control_variate_estimate_list[3]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(hours, upper_bound, label="Upper Bound", color="red", marker='o')
plt.plot(hours, lower_bound, label="Lower Bound", color="blue", marker='o')
plt.fill_between(hours, lower_bound, upper_bound, color="gray", alpha=0.3, label="Confidence Interval")
plt.xticks(hours)  # Show all hour indices
plt.xlabel("Hour")
plt.ylabel("Value of Confidence Interval")
plt.title("Confidence Interval by Hour")
plt.legend()
plt.grid()
plt.show()