import numpy as np

print("hw-3.01")

a = np.arange(60).reshape(3, 4, 5)
print("shape:", a.shape)
print("ndim:", a.ndim)
print("size:", a.size)
print("dtype:", a.dtype)
print("strides:", a.strides)
print("C_CONTIGUOUS:", a.flags["C_CONTIGUOUS"])
