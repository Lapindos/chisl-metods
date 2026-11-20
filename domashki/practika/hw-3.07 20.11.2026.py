import numpy as np

print("hw-3.07 20.11.2026")

v = np.arange(5)
col = v[:, None]
row = v[None, :]
print("v[:, None] форма", col.shape, "столбец из вектора")
print("v[None, :] форма", row.shape, "строка из вектора")
print("squeeze форма", np.squeeze(col).shape, "лишняя ось длины 1 убрана")
t = np.arange(6).reshape(2, 3).T
print("транспонирование форма", t.shape)
print(t)
table = v[:, None] + v[None, :]
print("сумма форм", table.shape)
print(table)
print("Вывод: первая операция делает столбец (5, 1), вторая — строку (1, 5).")
print("squeeze возвращает обычный вектор длины 5. .T меняет (2, 3) на (3, 2) и переворачивает таблицу.")
print("Сложение столбца и строки даёт таблицу сумм: клетка [i, j] равна i + j, форма (5, 5).")
