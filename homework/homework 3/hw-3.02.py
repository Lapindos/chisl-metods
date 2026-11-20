import numpy as np

print("hw-3.02")

a = np.array([1, 2, 3, 4])
print("a =", a, "dtype", a.dtype)
print("a / 2 =", a / 2, "dtype", (a / 2).dtype)
print("a // 2 =", a // 2, "dtype", (a // 2).dtype)
print("a / 2.0 =", a / 2.0, "dtype", (a / 2.0).dtype)
print("a после деления всё ещё", a)

b = np.array([1, 2, 3], dtype=np.int8)
print("b + 127 =", b + 127, "dtype", (b + 127).dtype)
