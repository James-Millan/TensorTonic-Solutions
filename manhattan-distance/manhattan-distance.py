import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    total = 0.0
    for i in range(len(x)):
        total += np.abs(x[i] - y[i])

    return total