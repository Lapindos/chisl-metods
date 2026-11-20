import time

import numpy as np

print("hw-5.09")


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


def loop_abs(arr):
    for i in range(arr.shape[0]):
        if arr[i] < 0:
            arr[i] = -arr[i]
    return arr


def numpy_abs(arr):
    arr[arr < 0] *= -1
    return arr


rng = np.random.default_rng(42)
base = rng.normal(size=10**6)
a_loop = base.copy()
a_numpy = base.copy()
r_loop, t_loop = measure(loop_abs, a_loop)
r_numpy, t_numpy = measure(numpy_abs, a_numpy)
print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
print(f"отрицательных не осталось: {np.all(r_numpy >= 0)}")
print("Вывод: замена по маске a[a < 0] *= -1 меняет массив на месте, без нового списка.")
print("Цикл делает то же самое через if, но дольше.")
print("Для честного сравнения каждому способу дана своя копия, чтобы они не портили одни и те же данные.")
