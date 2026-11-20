import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

print("hw-1.09 20.11.2026")

mp.mp.dps = 50


def rel_err(approx, exact_value):
    return abs(mp.mpf(approx) - exact_value) / abs(exact_value)


def naive_sum(n):
    s = 0.0
    k = 1
    while k <= n:
        s = s + 1.0 / k
        k = k + 1
    return s


ns = [10**5, 10**6, 10**7]
err_naive = []
err_sum = []
err_fsum = []

print("n    ошибка цикла    ошибка sum    ошибка fsum")
for n in ns:
    arr = [1.0 / k for k in range(1, n + 1)]
    exact = mp.harmonic(n)
    e1 = float(rel_err(naive_sum(n), exact))
    e2 = float(rel_err(sum(arr), exact))
    e3 = float(rel_err(math.fsum(arr), exact))
    err_naive.append(e1)
    err_sum.append(e2)
    err_fsum.append(e3)
    print(f"{n:.0e}   {e1:.6e}   {e2:.6e}   {e3:.6e}")

p = math.log(err_naive[-1] / err_naive[0]) / math.log(ns[-1] / ns[0])
print(f"ошибка наивного способа выросла примерно как n^{p:.2f}")

bad_n = None
for n, err in zip(ns, err_naive):
    if err > 1e-10 and bad_n is None:
        bad_n = n

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ns, err_naive, "o-", color="crimson", label="цикл слева направо")
ax.plot(ns, err_sum, "s-", color="darkorange", label="sum")
ax.plot(ns, err_fsum, "^-", color="steelblue", label="math.fsum")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("n")
ax.set_ylabel("Относительная ошибка")
ax.set_title("Сумма 1/k")
ax.legend()
ax.grid(True, which="both", alpha=0.2)
plt.tight_layout()
fig.savefig("hw-1.09 20.11.2026.png", dpi=150, bbox_inches="tight")
print("График сохранён: hw-1.09 20.11.2026.png")
if bad_n is None:
    print("Вывод: на n до 1e7 ошибка цикла ещё не стала больше 1e-10, но она растёт вместе с n.")
else:
    print(f"Вывод: наивная сумма становится неприемлемой (ошибка > 1e-10) при n = {bad_n:.0e}.")
print("sum и math.fsum на этих n остаются около 1e-16, почти как сам эталон в float.")
print("Цикл в Python копит лишнюю ошибку. Чем больше слагаемых, тем больше шансов потерять младшие цифры.")
