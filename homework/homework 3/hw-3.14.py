import numpy as np

print("hw-3.14")

rng = np.random.default_rng(1)
X = rng.normal(size=(100, 3))
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
print("средние столбцов", X_norm.mean(axis=0))
print("std столбцов", X_norm.std(axis=0))
print("средние ≈ 0:", np.allclose(X_norm.mean(axis=0), 0))
print("std ≈ 1:", np.allclose(X_norm.std(axis=0), 1))

diff = X_norm[:, None, :] - X_norm[None, :, :]
D = np.sqrt((diff ** 2).sum(axis=2))
print("D.shape", D.shape)
print("диагональ ≈ 0:", np.allclose(np.diag(D), 0))
print("симметрична:", np.allclose(D, D.T))
print("Вывод: среднее и std столбца имеют форму (3,), NumPy сам вычитает их из всех 100 строк. Цикл не нужен.")
print("Расстояния тоже без цикла: вычитание формы (100, 1, 3) и (1, 100, 3) даёт все пары сразу.")
print("Диагональ нулевая, потому что расстояние от строки до себя равно нулю, а матрица симметрична, потому что ||i-j|| = ||j-i||.")
