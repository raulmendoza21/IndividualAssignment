# production code: pure O(n^3) matmul and helpers
from __future__ import annotations
from typing import List, Sequence
import random

Matrix = List[List[float]]

def generate_random_matrix(n: int, seed: int | None = None) -> Matrix:
    if seed is not None:
        random.seed(seed)
    return [[random.random() for _ in range(n)] for _ in range(n)]

def zeros(n: int) -> Matrix:
    return [[0.0 for _ in range(n)] for _ in range(n)]

def matmul_naive(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    C = zeros(n)
    # i-j-k loop (cache-friendly on C when B is transposed; here keep it simple)
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            a_ik = Ai[k]
            Bk = B[k]
            for j in range(n):
                Ci[j] += a_ik * Bk[j]
    return C
