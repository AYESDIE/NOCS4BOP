import numpy

def sample_points(points, n_points, sampling_type="random_sample"):
    if sampling_type == "random_sample":
        return points[numpy.random.choice(points.shape[0], n_points)]
    else:
        return points
