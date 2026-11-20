import math

print("hw-1.03")

print("Уравнение x^2 - 2x + 1 = 0 имеет корень x = 1 кратности 2.")
print("Меняем свободный член на 1 - eps: x^2 - 2x + (1 - eps) = 0.")
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

print("Вывод: eps уменьшается в 100 раз, а сдвиг корня только в 10 раз.")
print("У кратного корня сдвиг ведёт себя как корень из eps, а не как сам eps.")
print("Поэтому кратный корень плохо обусловлен: маленькая помеха в коэффициенте заметно двигает ответ.")
