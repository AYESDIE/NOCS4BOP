import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nocs4bop import calculate_nocs

import bop_toolkit_lib.inout
import numpy

for input_dir in os.listdir("."):
    if "models" not in input_dir:
        continue
    
    if not os.path.isdir(input_dir):
        continue
    
    os.makedirs(f"processed_{input_dir}", exist_ok=True)
    for file_name in os.listdir(input_dir):
        file_name = os.path.join(input_dir, file_name)
        if file_name.endswith(".ply"):
            point_cloud = bop_toolkit_lib.inout.load_ply(file_name)
            points = point_cloud['pts']
        else:
            print(f"Unknown file type: {file_name}")
            continue
        
        file_name_wo_ext = file_name.split(".")[0].split("/")[-1]
        point_cloud['pts'] = calculate_nocs(points)
        bop_toolkit_lib.inout.save_ply(os.path.join(f"processed_{input_dir}", f"{file_name_wo_ext}_nocs.ply"), point_cloud)        