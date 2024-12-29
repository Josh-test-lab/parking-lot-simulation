"""
Title: Save images to GIF for parking model for the parking lot in Zhixue station
Author: Hsu, Yao-Chih, Xie, Yi-Xuan, Sin, Wen-Lee
Version: 1131229
Reference: Class of Simulation Study by C. Wang at 2024 fall
"""

### import module
from images_to_gif.images_to_gif import images_to_gif
import tqdm
import time

### main program
start_time = time.time()
folders = [
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

for idx in range(1,4):
    for folder in tqdm.tqdm(folders):
        print(f'\nConverting "{folder}" in "scenario_{idx}"...')
        path_to_image_folder = f'scenario\\scenario_{idx}\\data_per_hour\\{folder}'
        path_to_output_gif = f'scenario\\scenario_{idx}\\data_per_hour\\{folder}.gif'
        images_to_gif(path_to_image_folder, path_to_output_gif, duration = 0.5, loop = 1)

end_time = time.time()
print(f'Done!')
print(f'Cost {end_time - start_time} seconds.')
input(f'Press any key to continue...')







