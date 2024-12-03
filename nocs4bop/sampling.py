import numpy

def __farthest_point_sampling(points, n_samples):
    n_points = points.shape[0]
    selected_pts = numpy.zeros((n_samples,), dtype=int)
    dist_to_set = numpy.full(n_points, numpy.inf)

    pt_idx = 0
    for i in range(n_samples):
        selected_pts[i] = pt_idx
        diff = points - points[pt_idx]
        dists = numpy.sqrt(numpy.sum(diff**2, axis=1))
        dist_to_set = numpy.minimum(dist_to_set, dists)
        pt_idx = numpy.argmax(dist_to_set)

    return selected_pts

def sample_points(points, n_points, sampling_type="random_sample"):
    if sampling_type == "random_sample":
        return points[numpy.random.choice(points.shape[0], n_points)]
    elif sampling_type == "farthest_point_sample":
        return points[__farthest_point_sampling(points, n_points)]
    else:
        return points
