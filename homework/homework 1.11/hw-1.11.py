import math

import numpy as np
import mpmath as mp

print("hw-1.11")

mp.mp.dps = 50
x = 1e-16
exact = mp.log(1 + mp.mpf(x))
by_math = math.log(1 + x)
by_numpy = float(np.log(1 + np.float64(x)))

print(f"x = {x}")
print(f"math.log(1 + x) = {by_math}")
print(f"numpy.log(1 + x) = {by_numpy}")
print(f"они равны через == : {by_math == by_numpy}")
print(f"эталон mpmath = {exact}")
print(f"math совпал с эталоном: {mp.almosteq(by_math, exact)}")
print(f"numpy совпал с эталоном: {mp.almosteq(by_numpy, exact)}")
print("Вывод: два float-результата совпали друг с другом, но оба неверные.")
print("1 + 1e-16 в обычном float равно 1, поэтому оба логарифма дали 0.")
print("Сравнивать float с float без отдельного эталона нельзя: общая ошибка выглядит как согласие.")
