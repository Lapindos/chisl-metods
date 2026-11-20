import timeit
import tracemalloc

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sizes = [100, 1_000, 10_000]
target = -1
number = 1000
repeat = 5

time_list = []
time_set = []

print("Задача 1. Проверка вхождения: list и set")
print(f"Ищем target={target}, которого нет в коллекции.")
print(f"timeit: number={number}, repeat={repeat}, берём минимум.\n")

for n in sizes:
    data_list = list(range(n))
    data_set = set(range(n))

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

    # Суммарное время number проверок -> микросекунды на одну проверку.
    best_list = min(times_list) / number * 1_000_000
    best_set = min(times_set) / number * 1_000_000
    time_list.append(best_list)
    time_set.append(best_set)

    print(
        f"n={n:<6}  list={best_list:10.3f} мкс   "
        f"set={best_set:8.3f} мкс   "
        f"set быстрее в {best_list / best_set:.1f} раз"
    )

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(sizes, time_list, "o-", color="crimson", linewidth=2, label="x in list  O(n)")
ax.plot(sizes, time_set, "s-", color="steelblue", linewidth=2, label="x in set  O(1)")
ax.set_xlabel("Размер коллекции (n)", fontsize=12)
ax.set_ylabel("Время одной проверки (мкс)", fontsize=12)
ax.set_title("Вхождение: list и set, худший случай", fontsize=14, fontweight="bold")
ax.set_yscale("log")
ax.legend(fontsize=11)
ax.grid(True, which="both", alpha=0.2)
plt.tight_layout()
fig.savefig("hw6_task1.png", dpi=150, bbox_inches="tight")
print("\nГрафик сохранён: hw6_task1.png")
print(
    "На лог-шкале set почти горизонтален (O(1)), "
    "list растёт вместе с n (O(n))."
)
