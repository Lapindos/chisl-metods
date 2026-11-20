import time

import numpy as np

print("hw-5.04")

def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

def loop_clip(arr):
    result = [0.0] * arr.shape[0]
    for i in range(arr.shape[0]):
        x = arr[i]
        if x < 0:
            result[i] = 0.0
        elif x > 1:
            result[i] = 1.0
        else:
            result[i] = x
    return result

def numpy_clip(arr):
    return np.clip(arr, 0, 1)

rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
changed = int(np.sum((a < 0) | (a > 1)))
r_loop, t_loop = measure(loop_clip, a)
r_numpy, t_numpy = measure(numpy_clip, a)
print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
print(f"элементов изменено: {changed}")
