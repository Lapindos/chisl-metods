import math

import mpmath as mp

print("hw-1.08")

mp.mp.dps = 50

def rel_err(approx, exact_value):
    return abs(mp.mpf(approx) - exact_value) / abs(exact_value)

print("x    ошибка log(1+x)    ошибка log1p")
for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    exact = mp.log(1 + mp.mpf(x))
    e_bad = float(rel_err(math.log(1 + x), exact))
    e_good = float(rel_err(math.log1p(x), exact))
    print(f"{x:.0e}   {e_bad:.6e}   {e_good:.6e}")
