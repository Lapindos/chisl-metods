import math

print("hw-1.03")

print("eps    сдвиг корня    отношение к предыдущему сдвигу")

eps_list = [1e-2, 1e-4, 1e-6]
prev_shift = None
for eps in eps_list:
    disc = 4 - 4 * (1 - eps)
    root = (2 - math.sqrt(disc)) / 2
    shift = abs(root - 1)
    if prev_shift is None:
        ratio_text = "-"
    else:
        ratio_text = f"{shift / prev_shift:.6g}"
    print(f"{eps:.0e}   {shift:.6e}   {ratio_text}")
    prev_shift = shift
