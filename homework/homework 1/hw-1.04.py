import math

print("hw-1.04")

def taylor_exp(x, n=60):
    s = 1.0
    term = 1.0
    for k in range(1, n + 1):
        term = term * x / k
        s = s + term
    return s

xs = [-1, -5, -10, -15, -20]
print("x    cond    ряд Тейлора    math.exp    относ. ошибка ряда")
for x in xs:
    bad = taylor_exp(x)
    good = math.exp(x)
    err = abs(bad - good) / abs(good)
    print(f"{x:4}   {abs(x):5.1f}   {bad:.6e}   {good:.6e}   {err:.3e}")
