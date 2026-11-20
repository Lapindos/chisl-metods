import numpy as np

print("hw-3.07")

v = np.arange(5)
col = v[:, None]
row = v[None, :]
print("v[:, None] форма", col.shape)
print("v[None, :] форма", row.shape)
print("squeeze форма", np.squeeze(col).shape)
t = np.arange(6).reshape(2, 3).T
print("транспонирование форма", t.shape)
print(t)
table = v[:, None] + v[None, :]
print("сумма форм", table.shape)
print(table)
