import time
import tracemalloc

import numpy as np

print("hw-5.08")

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

def loop_filter(arr):
    result = []
    for x in arr:
        if x > 0:
            result.append(x)
    return result

def numpy_filter(arr):
    return arr[arr > 0]

rng = np.random.default_rng(42)
a = rng.normal(size=10**6)
r_loop, t_loop = measure(loop_filter, a)
r_numpy, t_numpy = measure(numpy_filter, a)

tracemalloc.start()
loop_filter(a)
_, peak_loop = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
numpy_filter(a)
_, peak_numpy = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"цикл:   {t_loop*1000:10.2f} мс   сколько осталось: {len(r_loop)}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   сколько осталось: {r_numpy.size}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
print(f"пик памяти цикла:  {peak_loop / 1024 / 1024:.2f} МБ")
print(f"пик памяти NumPy:  {peak_numpy / 1024 / 1024:.2f} МБ")
