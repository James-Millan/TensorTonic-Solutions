import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    total = 0.0
    for i in range(len(x)):
        total += (x[i] - y[i]) ** 2

    return np.sqrt(total)