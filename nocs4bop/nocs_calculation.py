import numpy
from .sampling import sample_points

def calculate_nocs(points, furthest_point_sampling=False):
    points = sample_points(points, 1024, "random_sample" if not furthest_point_sampling else "farthest_point_sample")
    centroid = points.mean(axis=0)
    centered_points = points - centroid
    shift = -centroid

    size = 2 * numpy.amax(numpy.abs(centered_points), axis=0)
    scale = 1.0 / numpy.max(size)

    scaled_points = centered_points * scale * numpy.array([[1.0, 1.0, -1.0]])

    return scaled_points, shift, scale
