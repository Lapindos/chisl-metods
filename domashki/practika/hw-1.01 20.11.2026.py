import math

print("hw-1.01 20.11.2026")


def cond_number(x, f_value, df_value):
    return abs(x * df_value / f_value)


x1 = 1e-8
c1 = cond_number(x1, math.sqrt(x1), 1 / (2 * math.sqrt(x1)))

x2 = 1.001
c2 = cond_number(x2, math.log(x2), 1 / x2)

x3 = 1.000001
c3 = cond_number(x3, x3 - 1, 1)

x4 = math.pi / 2
c4 = cond_number(x4, math.sin(x4), math.cos(x4))

names = ["sqrt(x)", "ln(x)", "x - 1", "sin(x)"]
values = [c1, c2, c3, c4]
points = [x1, x2, x3, x4]

for name, x, c in zip(names, points, values):
    if c < 10:
        kind = "хорошо обусловлена"
    else:
        kind = "плохо обусловлена"
    print(f"{name} при x={x}: cond={c:.6g}  {kind}")

order = sorted(zip(values, names))
print("По возрастанию cond:", ", ".join(name for _, name in order))
print("Вывод: самая опасная задача — f(x) = x - 1 рядом с единицей.")
print("Там ответ почти ноль, а cond около миллиона: маленькая ошибка во входе сильно портит результат.")
print("sin в точке pi/2 и корень обусловлены хорошо: cond у них маленький.")
