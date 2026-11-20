import time

import numpy as np

print("hw-5.10")


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


def loop_band(arr):
    result = []
    for x in arr:
        if -1 < x < 1:
            result.append(x)
    return result


def numpy_band(arr):
    return arr[(arr > -1) & (arr < 1)]


rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
r_loop, t_loop = measure(loop_band, a)
r_numpy, t_numpy = measure(numpy_band, a)
print(f"цикл:   {t_loop*1000:10.2f} мс   сколько осталось: {len(r_loop)}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   сколько осталось: {r_numpy.size}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

try:
    print(a > -1 and a < 1)
except ValueError:
    print("a > -1 and a < 1 не работает: and не умеет сравнивать целый массив")

print("Вывод: в Python можно написать -1 < x < 1, это читается как в математике.")
print("В NumPy так нельзя: нужно (a > -1) & (a < 1), и скобки обязательны.")
print("Без скобок условие либо падает, либо считается не так. Оба рабочих способа отбирают один и тот же кусок.")
