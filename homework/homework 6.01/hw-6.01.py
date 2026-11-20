import timeit

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("hw-6.01")

sizes = [100, 1_000, 10_000, 100_000]
target = -1
number = 1000
repeat = 5

time_list = []
time_set = []
time_dict = []

print("Поиск элемента, которого нет в коллекции. target =", target)
print(f"timeit: number={number}, repeat={repeat}, берём минимум.")
print()

for n in sizes:
    data_list = list(range(n))
    data_set = set(range(n))
    data_dict = {i: i for i in range(n)}

    times_list = timeit.repeat(
        "target in data_list",
        globals={"target": target, "data_list": data_list},
        number=number,
        repeat=repeat,
    )
    times_set = timeit.repeat(
        "target in data_set",
        globals={"target": target, "data_set": data_set},
        number=number,
        repeat=repeat,
    )
    times_dict = timeit.repeat(
        "target in data_dict",
        globals={"target": target, "data_dict": data_dict},
        number=number,
        repeat=repeat,
    )

    best_list = min(times_list) / number * 1_000_000
    best_set = min(times_set) / number * 1_000_000
    best_dict = min(times_dict) / number * 1_000_000
    time_list.append(best_list)
    time_set.append(best_set)
    time_dict.append(best_dict)

    print(
        f"n={n:<7}  list={best_list:10.3f} мкс   "
        f"set={best_set:8.3f} мкс   "
        f"dict={best_dict:8.3f} мкс   "
        f"set быстрее list в {best_list / best_set:.1f} раз   "
        f"dict быстрее list в {best_list / best_dict:.1f} раз"
    )

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(sizes, time_list, "o-", color="crimson", linewidth=2, label="x in list  O(n)")
ax.plot(sizes, time_set, "s-", color="steelblue", linewidth=2, label="x in set  O(1)")
ax.plot(sizes, time_dict, "^-", color="seagreen", linewidth=2, label="x in dict  O(1)")
ax.set_xlabel("Размер коллекции (n)", fontsize=12)
ax.set_ylabel("Время одной проверки (мкс)", fontsize=12)
ax.set_title("Вхождение: list, set и dict, худший случай", fontsize=14, fontweight="bold")
ax.set_yscale("log")
ax.legend(fontsize=11)
ax.grid(True, which="both", alpha=0.2)
plt.tight_layout()
fig.savefig("hw-6.01.png", dpi=150, bbox_inches="tight")
print()
print("График сохранён: hw-6.01.png")
print("Вывод: list на лог-шкале растёт вместе с n, это худший случай O(n), потому что числа -1 в списке нет.")
print("set и dict почти горизонтальные: поиск по хеш-таблице не зависит от длины.")
print("dict чуть тяжелее set, потому что хранит и ключ, и значение, но на графике это почти незаметно.")
