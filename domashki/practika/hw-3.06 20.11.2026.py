import numpy as np

print("hw-3.06 20.11.2026")

M = np.arange(12).reshape(3, 4)
f = M.flatten()
r = M.ravel()
print("flatten это копия, base is None:", f.base is None)
print("ravel.base is not None:", r.base is not None)
print("ravel делит память с M:", np.shares_memory(r, M))
print("M до правок:\n", M)
f[0] = 999
print("после f[0] = 999 M не изменился:\n", M)
r[1] = 888
print("после r[1] = 888 M изменился:\n", M)
print("Вывод: ravel — это view, его правка портит исходную матрицу. Он быстрее и не тратит память.")
print("flatten всегда делает копию. Его берут, когда дальше массив будут менять, а оригинал надо сохранить.")
print("Если нужна только прочитать числа подряд и ничего не писать, хватает ravel.")
