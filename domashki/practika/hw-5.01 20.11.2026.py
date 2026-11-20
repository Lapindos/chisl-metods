import time

import numpy as np

print("hw-5.01 20.11.2026")


def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


def loop_sum(arr):
    total = 0.0
    for x in arr:
        total += x
    return total


def numpy_sum(arr):
    return arr.sum()


sizes = [10**5, 10**6, 10**7]
speeds = []

for n in sizes:
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)
    r_loop, t_loop = measure(loop_sum, a)
    r_numpy, t_numpy = measure(numpy_sum, a)
    speed = t_loop / t_numpy
    speeds.append(speed)
    print(f"n={n}")
    print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
    print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
    print(f"ускорение: {speed:.1f}×")
    print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")
    print()

print("n → ускорение:", end=" ")
for n, s in zip(sizes, speeds):
    print(f"{n} → {s:.1f}×", end="  ")
print()

first_big = None
for n, s in zip(sizes, speeds):
    if s > 10 and first_big is None:
        first_big = n

print("Вывод: NumPy короче — одна строка вместо цикла.")
if first_big is None:
    print("На этих размерах ускорение ещё не стало больше 10 раз.")
else:
    print(f"Разница становится заметной (больше 10 раз) уже при n = {first_big}.")
print(
    f"Дальше ускорение такое: {speeds[0]:.0f}×, {speeds[1]:.0f}×, {speeds[2]:.0f}×. "
    "Оно не обязано расти с каждым n, но остаётся большим."
)
print("Причина в том, что цикл делает каждый шаг в Python, а sum работает в скомпилированном коде.")
