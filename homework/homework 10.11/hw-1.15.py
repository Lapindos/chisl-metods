import math

import mpmath as mp
import numpy as np

print("hw-1.15")

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
