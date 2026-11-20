import numpy as np

a = np.arange(24).reshape(6, 4)
print("1. массив:\n", a)
print("shape:", a.shape)
print("ndim: ", a.ndim)
print("size: ", a.size)
print("dtype:", a.dtype)

original = a.ravel().copy()
b = a.reshape(4, 6)
c = b.reshape(2, 3, 4)
d = c.reshape(24)
print("\n2. (4, 6):\n", b)
print("(2, 3, 4):\n", c)
print("(24,):", d)
print("значения не изменились:", np.array_equal(original, d))

column = a[:, 2]
print("\n3. столбец:", column)
column[0] = -1
print("a[0, 2] после правки среза:", a[0, 2])
print(a)

a = np.arange(24).reshape(6, 4)
selected = a[a > 10]
print("\n4. a[a > 10] =", selected)
print("среднее =", selected.mean())

a = np.arange(24, dtype=np.float64).reshape(6, 4)
row_means = a.mean(axis=1, keepdims=True)
centered = a - row_means
print("\n5. centered.shape =", centered.shape)
print(centered)
print("сумма по строкам ≈ 0:", np.allclose(centered.sum(axis=1), 0))
