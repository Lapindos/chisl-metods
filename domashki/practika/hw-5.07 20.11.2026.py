import time

import numpy as np

print("hw-5.07 20.11.2026")


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


def loop_max(arr):
    max_val = arr[0]
    max_idx = 0
    for i in range(arr.shape[0]):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_val, max_idx


def numpy_max(arr):
    return arr.max(), arr.argmax()


rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
r_loop, t_loop = measure(loop_max, a)
r_numpy, t_numpy = measure(numpy_max, a)
print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
same_val = np.isclose(r_loop[0], r_numpy[0])
same_idx = r_loop[1] == r_numpy[1]
print(f"максимум совпадает: {same_val}")
print(f"индекс совпадает: {same_idx}")
print("Вывод: a.max() и a.argmax() короче цикла, который запоминает значение и индекс.")
print("Индекс должен совпасть точно: здесь нет сложения, только сравнения.")
print("NumPy быстрее, потому что проходит массив не в Python-цикле.")
