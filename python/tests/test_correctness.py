import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import numpy as np # type: ignore
from matrixmul import matmul_naive, generate_random_matrix

def test_small_equals_numpy():
    n = 5
    A = generate_random_matrix(n, seed=42)
    B = generate_random_matrix(n, seed=7)
    C = matmul_naive(A, B)
    npA = np.array(A, dtype=float)
    npB = np.array(B, dtype=float)
    npC = npA @ npB
    assert np.allclose(np.array(C), npC, atol=1e-9)
