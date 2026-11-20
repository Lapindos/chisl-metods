import numpy as np

print("hw-3.09")

A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)
print("A @ B форма", (A @ B).shape)
print(A @ B)
print("A.T @ B.T форма", (A.T @ B.T).shape)
print(A.T @ B.T)
print("A * A форма", (A * A).shape)
print(A * A)
try:
    print(A * B)
except ValueError as e:
    print("A * B ошибка:", e)

D = np.diag([1.0, 2.0, 3.0])
print("для диагональной матрицы * и @ совпали:", np.array_equal(D * D, D @ D))
print(D * D)
