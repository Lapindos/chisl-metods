import numpy as np

print("hw-3.10")

M = np.arange(12).reshape(3, 4)
print(M)
print("sum axis=0", M.sum(axis=0), "свернули строки, остались суммы столбцов")
print("sum axis=1", M.sum(axis=1), "свернули столбцы, остались суммы строк")
print("mean axis=0", M.mean(axis=0), "среднее по каждому столбцу")
print("mean axis=1", M.mean(axis=1), "среднее по каждой строке")
print("argmax axis=0", M.argmax(axis=0), "номер строки, где в столбце максимум")
print("argmax axis=1", M.argmax(axis=1), "номер столбца, где в строке максимум")

by_hand = []
for j in range(M.shape[1]):
    s = 0
    for i in range(M.shape[0]):
        s = s + M[i, j]
    by_hand.append(s)
print("сумма по столбцам руками", by_hand)
print("совпало с sum(axis=0):", np.array_equal(by_hand, M.sum(axis=0)))
print("Вывод: axis=0 идёт вниз по строкам и схлопывает их. Для обычной таблицы это сумма столбца.")
print("axis=1 идёт вправо по столбцам и схлопывает их. Это сумма строки.")
print("Маленький пример руками подтверждает: sum(axis=0) — это не суммы строк.")
