import math
import time

import numpy as np

print("hw-5.03")


def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


def loop_y(arr):
    result = [0.0] * arr.shape[0]
    for i in range(arr.shape[0]):
        x = arr[i]
        result[i] = math.sin(x) + x * x
    return result


def numpy_y(arr):
    return np.sin(arr) + arr**2


rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
r_loop, t_loop = measure(loop_y, a)
r_numpy, t_numpy = measure(numpy_y, a)
print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
print("Вывод: формула y = sin(x) + x^2 в NumPy пишется почти как в математике.")
print("Цикл делает то же самое, но на каждом элементе вызывает math.sin из Python, поэтому он медленнее.")
print("Результаты совпадают: оба способа считают одну и ту же формулу.")
