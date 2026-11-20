import numpy as np

print("hw-3.03")

e32 = float(np.float32(0.1)) - 0.1
e64 = float(np.float64(0.1)) - 0.1
print("float32:", repr(e32), f"{e32:.20e}")
print("float64:", repr(e64), f"{e64:.20e}")
if e64 != 0:
    print("ошибка float32 больше ошибки float64 в", abs(e32) / abs(e64), "раз")
