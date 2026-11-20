import numpy as np

print("hw-3.11")

rng = np.random.default_rng(42)
X = rng.normal(size=(5, 3))
m0 = X.mean(axis=0)
m0k = X.mean(axis=0, keepdims=True)
print("mean axis=0", m0.shape)
print("mean keepdims", m0k.shape)
a = X - m0
b = X - m0k
print("без keepdims", a.shape, "с keepdims", b.shape)
print("обе формы (5, 3):", a.shape == (5, 3) and b.shape == (5, 3))

s1 = X.std(axis=1)
s1k = X.std(axis=1, keepdims=True)
print("std axis=1", s1.shape, "keepdims", s1k.shape)
rows = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
print("средние по строкам", np.round(rows.mean(axis=1), 10))
print("std по строкам", np.round(rows.std(axis=1), 10))
print("средние ≈ 0:", np.allclose(rows.mean(axis=1), 0))
print("std ≈ 1:", np.allclose(rows.std(axis=1), 1))
try:
    print((X - X.mean(axis=1)).shape)
except ValueError:
    print("X - X.mean(axis=1) без keepdims не считается: форма (5,) не подходит к (5, 3)")
print("Вывод: для столбцов mean без keepdims имеет форму (3,) и спокойно вычитается из (5, 3).")
print("Для строк mean без keepdims имеет форму (5,), и вычитание падает. keepdims оставляет (5, 1).")
print("Тогда broadcasting вычитает из каждой строки своё среднее, и нормировка получается одной формулой.")
