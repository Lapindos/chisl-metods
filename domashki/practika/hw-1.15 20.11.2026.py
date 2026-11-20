import math

import mpmath as mp
import numpy as np

print("hw-1.15 20.11.2026")

print("Цель: проверить, где формула sqrt(x+1) - sqrt(x) становится неустойчивой.")
print("Постановка: плохой способ — прямая разность корней. Хороший — 1 / (sqrt(x+1) + sqrt(x)).")
print("Эталон: mpmath с 50 знаками, независимо от float.")

mp.mp.dps = 50
xs = np.logspace(2, 16, 8)


def bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)


def good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))


def exact(x):
    x = mp.mpf(x)
    return mp.sqrt(x + 1) - mp.sqrt(x)


print("x    плохой    хороший    эталон    ошибка плохого    ошибка хорошего")
for x in xs:
    x = float(x)
    ref = exact(x)
    bad_value = bad(x)
    good_value = good(x)
    err_bad = abs(mp.mpf(bad_value) - ref) / abs(ref)
    err_good = abs(mp.mpf(good_value) - ref) / abs(ref)
    print(
        f"{x:.3e}  {bad_value:.6e}  {good_value:.6e}  {float(ref):.6e}  "
        f"{float(err_bad):.3e}  {float(err_good):.3e}"
    )

print("Вывод: плохой алгоритм неустойчив из-за вычитания двух близких корней.")
print("Пока x около сотен и тысяч, ошибка ещё маленькая, и плохой способ ещё пригоден для грубого ответа.")
print("Дальше ошибка растёт, а около 1e16 разность в float уже почти бесполезна.")
print("Хороший алгоритм на всём диапазоне держит обычную точность float, примерно 1e-16.")
print("Достижимая точность здесь — это точность float64 у устойчивой формулы, а не у прямой разности.")
