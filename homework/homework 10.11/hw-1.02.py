print("hw-1.02")

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
