import math
import time

import numpy as np


def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


# 1. Сумма
def loop_sum(arr):
    total = 0.0
    for x in arr:
        total += x
    return total


def numpy_sum(arr):
    return arr.sum()


rng = np.random.default_rng(42)
a = rng.normal(size=10**5)

r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
s1 = t_loop / t_numpy

rng = np.random.default_rng(42)
a = rng.normal(size=10**6)

r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
s2 = t_loop / t_numpy

rng = np.random.default_rng(42)
a = rng.normal(size=10**7)

r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
s3 = t_loop / t_numpy

print(f"n → ускорение: {10**5} → {s1:.1f}×, {10**6} → {s2:.1f}×, {10**7} → {s3:.1f}×")


# 2.
rng = np.random.default_rng(42)
a = rng.normal(size=10**6)


def loop_mean_std(arr):
    s = 0.0
    s2 = 0.0
    for x in arr:
        s += x
        s2 += x * x
    n = arr.shape[0]
    mean = s / n
    var = s2 / n - mean * mean
    std = math.sqrt(var)
    return mean, std


def numpy_mean_std(arr):
    return arr.mean(), arr.std()


r_loop,  t_loop  = measure(loop_mean_std,  a)
r_numpy, t_numpy = measure(numpy_mean_std, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop[0]:.6f}, {r_loop[1]:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy[0]:.6f}, {r_numpy[1]:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
d_mean = abs(r_loop[0] - r_numpy[0])
d_std = abs(r_loop[1] - r_numpy[1])
print(f"|Δmean| = {d_mean:.3e}  до 1e-12: {d_mean <= 1e-12}  |Δstd| = {d_std:.3e}  до 1e-12: {d_std <= 1e-12}")


# 3.
rng = np.random.default_rng(42)
a = rng.normal(size=10**6)


def loop_y(arr):
    result = [0.0] * arr.shape[0]
    for i in range(arr.shape[0]):
        x = arr[i]
        result[i] = math.sin(x) + x * x
    return result


def numpy_y(arr):
    return np.sin(arr) + arr**2


r_loop,  t_loop  = measure(loop_y,  a)
r_numpy, t_numpy = measure(numpy_y, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")


# 4.
rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
changed = int(np.sum((a < 0) | (a > 1)))


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


r_loop,  t_loop  = measure(loop_clip,  a)
r_numpy, t_numpy = measure(numpy_clip, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
print(f"элементов изменено: {changed}")
