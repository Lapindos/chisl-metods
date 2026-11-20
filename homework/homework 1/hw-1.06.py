import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

print("hw-1.06")

mp.mp.dps = 50

def bad(x):
    return (1 - math.cos(x)) / (x * x)

def good(x):
    s = math.sin(x / 2)
    return 2 * s * s / (x * x)

def exact(x):
    x = mp.mpf(x)
    return (1 - mp.cos(x)) / (x * x)

def rel_err(approx, exact_value):
    return abs(mp.mpf(approx) - exact_value) / abs(exact_value)

xs = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
err_bad = []
err_good = []
crossed = None

print("x    ошибка плохого    ошибка хорошего")
for x in xs:
    ref = exact(x)
    e_bad = float(rel_err(bad(x), ref))
    e_good = float(rel_err(good(x), ref))
    err_bad.append(e_bad)
    err_good.append(e_good)
    print(f"{x:.0e}   {e_bad:.6e}   {e_good:.6e}")
    if e_bad > 0.01 and crossed is None:
        crossed = x

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(xs, err_bad, "o-", color="crimson", label="плохо: (1 - cos x) / x^2")
ax.plot(xs, err_good, "s-", color="steelblue", label="хорошо: 2 sin(x/2)^2 / x^2")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("x")
ax.set_ylabel("Относительная ошибка")
ax.set_title("1 - cos x при малых x")
ax.legend()
ax.grid(True, which="both", alpha=0.2)
plt.tight_layout()
fig.savefig("hw-1.06.png", dpi=150, bbox_inches="tight")
print("График сохранён: hw-1.06.png")
if crossed is None:
    print("На этих x ошибка плохого способа ещё не превысила 1%.")
else:
    print(f"Ошибка плохого способа превышает 1% начиная с x = {crossed:.0e}.")
