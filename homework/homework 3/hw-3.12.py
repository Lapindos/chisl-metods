import numpy as np

print("hw-3.12")

a = np.arange(10)
b = a[2:5]
print("a", a)
b[0] = 999
print("после правки среза a стал", a)
a = np.arange(10)
c = a[2:5].copy()
c[0] = 999
print("после правки копии a остался", a)
