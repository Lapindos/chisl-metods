import numpy as np

print("hw-3.04")

arrays = [
    ("zeros float64", np.zeros((2, 3), dtype=np.float64)),
    ("zeros float32", np.zeros((2, 3), dtype=np.float32)),
    ("ones int16", np.ones((2, 3), dtype=np.int16)),
    ("full uint8", np.full((2, 3), 7, dtype=np.uint8)),
]
for name, arr in arrays:
    print(name, "dtype", arr.dtype, "nbytes", arr.nbytes)

a64 = np.zeros((1000, 1000), dtype=np.float64)
a32 = np.zeros((1000, 1000), dtype=np.float32)
print("на (1000, 1000) float32 экономит байт:", a64.nbytes - a32.nbytes)
