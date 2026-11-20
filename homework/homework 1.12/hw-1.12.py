import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

print("hw-1.12")

mp.mp.dps = 50
xs = np.logspace(2, 16, 8)


def bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)


def exact(x):
    x = mp.mpf(x)
    return mp.sqrt(x + 1) - mp.sqrt(x)


print("x    ошибка плохого")
errs = []
for x in xs:
    ref = exact(x)
    approx = bad(float(x))
    err = float(abs(mp.mpf(approx) - ref) / abs(ref))
    errs.append(err)
    print(f"{x:.3e}   {err:.6e}")

eps = np.finfo(float).eps
theory = eps * xs
p = math.log(errs[-1] / errs[0]) / math.log(xs[-1] / xs[0])
print(f"наклон по концам графика ≈ {p:.2f}")
print("теория: ошибка плохого способа ≈ eps * x, то есть наклон 1")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(xs, errs, "o-", color="crimson", label="факт")
ax.plot(xs, theory, "--", color="gray", label="eps * x")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("x")
ax.set_ylabel("Относительная ошибка")
ax.set_title("sqrt(x+1) - sqrt(x)")
ax.legend()
ax.grid(True, which="both", alpha=0.2)
plt.tight_layout()
fig.savefig("hw-1.12.png", dpi=150, bbox_inches="tight")
print("График сохранён: hw-1.12.png")
print("Вывод: одной точки мало. На маленьком x ошибка ещё тихая, а на большом x плохая формула уже бесполезна.")
print("Наклон близок к 1, как у оценки eps * x: ошибка растёт пропорционально x.")
print("Диапазон на лог-шкале как раз показывает этот рост, одна точка его прячет.")
