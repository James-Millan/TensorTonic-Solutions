import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    n = len(A)
    m = len(A[0])
    A_t = [[0] * n for _ in range(m)] 
    for i in range(n):
        for j in range(m):
            A_t[j][i] = A[i][j]

    return np.asarray(A_t)