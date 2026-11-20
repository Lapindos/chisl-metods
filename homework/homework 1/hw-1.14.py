import math

import numpy as np

print("hw-1.14")

def show(name, values):
    print(name)
    try:
        print("  sum:  ", sum(values))
    except Exception as e:
        print("  sum:  ", type(e).__name__, e)
    try:
        print("  fsum: ", math.fsum(values))
    except Exception as e:
        print("  fsum: ", type(e).__name__, e)
    try:
        print("  np.sum:", float(np.sum(values)))
    except Exception as e:
        print("  np.sum:", type(e).__name__, e)

base = [1.0, 2.0, 3.0]
show("обычные числа", base)
show("плюс очень большое 1e300", base + [1e300])
show("плюс очень маленькое 1e-300", base + [1e-300])
show("плюс ноль", base + [0.0])
show("плюс денормализованное 1e-320", base + [1e-320])
show("плюс inf", base + [float("inf")])
show("плюс nan", base + [float("nan")])
show("inf и -inf вместе", [float("inf"), float("-inf")])
show("всё сразу", [1e300, 1e-300, 0.0, 1e-320, float("inf"), float("nan")])
