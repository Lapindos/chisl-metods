print("hw-1.02 20.11.2026")

print("f(a, b) = a - b. Производная по a равна 1, производная по b равна -1.")
print("cond по a = |a / (a - b)|, cond по b = |b / (a - b)|.")
print("Когда a почти равно b, знаменатель маленький, поэтому оба числа обусловленности большие.")

a = 1 + 1e-8
b = 1
delta_a = 1e-9
f = a - b
f_new = (a + delta_a) - b
delta_f = f_new - f
cond_a = abs(a / (a - b))
relative_input = abs(delta_a / a)
relative_output = abs(delta_f / f)
predicted = cond_a * relative_input

print(f"a={a}, b={b}, f={f}")
print(f"cond по a = {cond_a:.6g}")
print(f"фактическое |Δf / f| = {relative_output:.6g}")
print(f"предсказание cond * |δa / a| = {predicted:.6g}")
print(f"Δf / δa = {delta_f / delta_a:.6g}")
print("Вывод: фактическое относительное изменение совпало с предсказанием по cond.")
print("Δf / δa около 1, потому что производная равна 1. Плохо здесь не производная, а деление на маленькую разность a - b.")
print("Задача вычитания близких чисел плохо обусловлена: относительная ошибка ответа намного больше относительной ошибки входа.")
