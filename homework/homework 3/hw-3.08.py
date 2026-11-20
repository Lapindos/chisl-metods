import numpy as np

print("hw-3.08")

A = np.arange(6).reshape(2, 3)
B = A.T
print("A\n", A)
print("B = A.T\n", B)
print("B.base is not None:", B.base is not None)
print("B делит память с A:", np.shares_memory(A, B))
print("strides A", A.strides, "strides B", B.strides)
B[0, 1] = 999
print("после B[0, 1] = 999 изменился и A:\n", A)
