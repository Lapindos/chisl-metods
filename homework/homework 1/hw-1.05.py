import math

import mpmath as mp

print("hw-1.05")

mp.mp.dps = 50

def bad_root(a, b, c):
    disc = math.sqrt(b * b - 4 * a * c)
    return (-b + disc) / (2 * a)

def good_root(a, b, c):
    disc = math.sqrt(b * b - 4 * a * c)
    return 2 * c / (-b - disc)

def exact_root(b):
    a = mp.mpf(1)
    b = mp.mpf(b)
    c = mp.mpf(1)
    disc = mp.sqrt(b * b - 4 * a * c)
    return (-b + disc) / (2 * a)

def rel_err(approx, exact):
    return abs(mp.mpf(approx) - exact) / abs(exact)

print("b    ошибка плохого    ошибка хорошего")
for b in [1e4, 1e8, 1e12]:
    exact = exact_root(b)
    err_bad = rel_err(bad_root(1, b, 1), exact)
    err_good = rel_err(good_root(1, b, 1), exact)
    print(f"{b:.0e}   {float(err_bad):.6e}   {float(err_good):.6e}")
