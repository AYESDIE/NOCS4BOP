import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nocs4bop import calculate_nocs

import open3d
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
            point_cloud = open3d.io.read_point_cloud(file_name)
            points = numpy.asarray(point_cloud.points)
        elif file_name.endswith(".obj"):
            point_cloud = open3d.io.read_triangle_mesh(file_name)
            points = numpy.asarray(point_cloud.vertices)
        else:
            print(f"Unknown file type: {file_name}")
            continue
        
        file_name_wo_ext = file_name.split(".")[0].split("/")[-1]
        points = numpy.asarray(point_cloud.points)
        nocs_points, shift, scale = calculate_nocs(points, False)
        numpy.savez(os.path.join(f"processed_{input_dir}", f"{file_name_wo_ext}_nocs_random_sample.npz"), nocs_points=nocs_points, shift=shift, scale=scale)
        
        nocs_points, shift, scale = calculate_nocs(points, True)
        numpy.savez(os.path.join(f"processed_{input_dir}", f"{file_name_wo_ext}_nocs_farthest_point_sample.npz"), nocs_points=nocs_points, shift=shift, scale=scale)
        