import math
import time

import numpy as np

print("hw-5.02")


def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


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


rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
r_loop, t_loop = measure(loop_mean_std, a)
r_numpy, t_numpy = measure(numpy_mean_std, a)
print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop[0]:.6f}, {r_loop[1]:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy[0]:.6f}, {r_numpy[1]:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
d_mean = abs(r_loop[0] - r_numpy[0])
d_std = abs(r_loop[1] - r_numpy[1])
print(f"|Δmean| = {d_mean:.3e}  до 1e-12: {d_mean <= 1e-12}")
print(f"|Δstd| = {d_std:.3e}  до 1e-12: {d_std <= 1e-12}")
print("Вывод: среднее и std в одну строку через NumPy читаются проще, чем цикл с двумя суммами.")
print("На миллионе чисел NumPy заметно быстрее. Совпадение до 1e-12 смотрим по напечатанной разнице.")
print("Маленькая разница в последних знаках нормальна: порядок сложения в цикле и в NumPy разный.")
