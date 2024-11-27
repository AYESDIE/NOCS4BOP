import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nocs4bop import calculate_nocs

import open3d
import numpy

for input_dir in ["models", "models_eval"]:
    if not os.path.exists(input_dir):
        continue
    os.makedirs(f"processed_{input_dir}", exist_ok=True)
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        file_name = file_name.split(".")[0]
        point_cloud = open3d.io.read_point_cloud(file_path)
        points = numpy.asarray(point_cloud.points)
        nocs_points, shift, scale = calculate_nocs(points)
        numpy.savez(os.path.join(f"processed_{input_dir}", f"{file_name}_nocs.npz"), nocs_points=nocs_points, shift=shift, scale=scale)