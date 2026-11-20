import numpy as np

print("hw-3.10")

M = np.arange(12).reshape(3, 4)
print(M)
print("sum axis=0", M.sum(axis=0))
print("sum axis=1", M.sum(axis=1))
print("mean axis=0", M.mean(axis=0))
print("mean axis=1", M.mean(axis=1))
print("argmax axis=0", M.argmax(axis=0))
print("argmax axis=1", M.argmax(axis=1))

by_hand = []
for j in range(M.shape[1]):
    s = 0
    for i in range(M.shape[0]):
        s = s + M[i, j]
    by_hand.append(s)
print("сумма по столбцам руками", by_hand)
print("совпало с sum(axis=0):", np.array_equal(by_hand, M.sum(axis=0)))
