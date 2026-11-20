import math

import mpmath as mp

print("hw-1.07")

mp.mp.dps = 50


def bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)


def good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))


def exact(x):
    x = mp.mpf(x)
    return mp.sqrt(x + 1) - mp.sqrt(x)


def rel_err(approx, exact_value):
    return abs(mp.mpf(approx) - exact_value) / abs(exact_value)


xs = [1e4, 1e8, 1e12, 1e14, 1e16]
err_bad = []
print("x    ошибка плохого    ошибка хорошего")
for x in xs:
    ref = exact(x)
    e_bad = float(rel_err(bad(x), ref))
    e_good = float(rel_err(good(x), ref))
    err_bad.append(e_bad)
    print(f"{x:.0e}   {e_bad:.6e}   {e_good:.6e}")

p = math.log(err_bad[-1] / err_bad[0]) / math.log(xs[-1] / xs[0])
print(f"показатель роста ошибки плохого способа ≈ {p:.2f}")
print("Вывод: ошибка плохого способа растёт примерно как x в первой степени.")
print("При больших x корень из x+1 и корень из x в float становятся почти одинаковыми, разность теряет цифры.")
print("Хорошая формула делит 1 на сумму корней и остаётся точной даже при x = 1e16.")
