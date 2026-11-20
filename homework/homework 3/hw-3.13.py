import numpy as np

print("hw-3.13")

rng = np.random.default_rng(0)
a = rng.normal(size=20)
pos = a[a > 0]
band = a[(a > -1) & (a < 1)]
picked = a[[0, 5, 10, 15]]
outliers = a[np.abs(a) > 2]
print("a > 0, сколько:", pos.size)
print("-1 < a < 1, сколько:", band.size)
print("элементы 0, 5, 10, 15:", picked)
print("выбросы |a| > 2:", outliers)

try:
    bad = a[a > 0] & (a < 1)
    print(bad)
except (ValueError, TypeError) as e:
    print("a[a > 0] & (a < 1) ошибка:", type(e).__name__)

a[a < 0] = 0
print("после зануления отрицательных:", a)
