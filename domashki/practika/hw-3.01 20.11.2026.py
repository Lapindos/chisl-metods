import numpy as np

print("hw-3.01 20.11.2026")

a = np.arange(60).reshape(3, 4, 5)
print("shape:", a.shape)
print("ndim:", a.ndim)
print("size:", a.size)
print("dtype:", a.dtype)
print("strides:", a.strides)
print("C_CONTIGUOUS:", a.flags["C_CONTIGUOUS"])
print("Каждое число в strides — это сколько байт нужно перешагнуть до соседа по этой оси.")
print("Последний шаг равен 8, потому что один элемент int64 занимает 8 байт. Средний шаг 5*8, внешний 4*5*8.")
print("size = 60, потому что в массиве 3 * 4 * 5 = 60 элементов, а не потому что shape как-то складывается.")
