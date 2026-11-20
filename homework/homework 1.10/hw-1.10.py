import math

import numpy as np
import mpmath as mp

print("hw-1.10")

mp.mp.dps = 50


def exact(x):
    x = mp.mpf(x)
    return (1 - mp.cos(x)) / (x * x)


def rel_from_exact(approx, x):
    ref = exact(x)
    return float(abs(mp.mpf(approx) - ref) / abs(ref))


def bad64(x):
    return (1 - math.cos(x)) / (x * x)


def good64(x):
    s = math.sin(x / 2)
    return 2 * s * s / (x * x)


def bad32(x):
    x = np.float32(x)
    one = np.float32(1)
    value = (one - np.cos(x)) / (x * x)
    return float(value)


print("Опыт (а). Плохой алгоритм, меняем x.")
err_a = []
xs = [1e-2, 1e-4, 1e-6, 1e-8]
for x in xs:
    err = rel_from_exact(bad64(x), x)
    err_a.append(err)
    print(f"  x={x:.0e}  ошибка={err:.6e}")
orders_a = math.log10(err_a[-1] / err_a[0])
print(f"  от первого x к последнему ошибка изменилась на {orders_a:.1f} порядков")

print("Опыт (б). x = 1e-4, меняем float32 и float64.")
x = 1e-4
err32 = rel_from_exact(bad32(x), x)
err64 = rel_from_exact(bad64(x), x)
print(f"  float32 ошибка={err32:.6e}")
print(f"  float64 ошибка={err64:.6e}")
if err64 == 0:
    print("  ошибка float64 здесь равна нулю в пределах печати")
else:
    print(f"  float32 хуже float64 в {err32 / err64:.3g} раз, это {math.log10(err32 / err64):.1f} порядков")

print("Опыт (в). x = 1e-8, меняем алгоритм.")
x = 1e-8
err_bad = rel_from_exact(bad64(x), x)
err_good = rel_from_exact(good64(x), x)
print(f"  плохой ошибка={err_bad:.6e}")
print(f"  хороший ошибка={err_good:.6e}")
print(f"  смена алгоритма меняет ошибку на {math.log10(err_bad / err_good):.1f} порядков")

print("Вывод: в опыте (а) доминирует сокращение 1 - cos(x), ошибка растёт, когда x уменьшается.")
print("В опыте (б) доминирует машинная точность: float32 хранит меньше цифр, чем float64.")
print("В опыте (в) доминирует устойчивость алгоритма: та же точка, но хорошая формула почти не ошибается.")
