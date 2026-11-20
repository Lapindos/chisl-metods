import time

import numpy as np

print("hw-5.06")

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

def loop_center(mat):
    n, k = mat.shape
    means = [0.0] * k
    for j in range(k):
        s = 0.0
        for i in range(n):
            s += mat[i, j]
        means[j] = s / n
    result = []
    for i in range(n):
        row = []
        for j in range(k):
            row.append(mat[i, j] - means[j])
        result.append(row)
    return result

def numpy_center(mat):
    return mat - mat.mean(axis=0)

rng = np.random.default_rng(42)
m = rng.normal(size=(10**5, 10))
r_loop, t_loop = measure(loop_center, m)
r_numpy, t_numpy = measure(numpy_center, m)
print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
