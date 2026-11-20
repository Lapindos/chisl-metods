import numpy as np

print("hw-3.05")

a = np.arange(24)
shapes = [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]
current = a
for shape in shapes:
    current = current.reshape(shape)
    same = np.array_equal(a, current.ravel())
    print("shape", current.shape, "данные на месте", same, "общая память", np.shares_memory(a, current))

b = a.reshape(4, 6).T
flat = b.reshape(24)
print("после транспонирования reshape копирует:", not np.shares_memory(b, flat))
