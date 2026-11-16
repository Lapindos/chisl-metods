import timeit
import tracemalloc

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Задача 1. x in list и x in set
# Худший случай: числа в коллекции нет, list проходит её до конца.

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


# Задача 2. Три способа создать список квадратов.

N_values = [100_000, 1_000_000]
methods = {
    "цикл с append": "out = []\nfor i in range(N):\n    out.append(i*i)",
    "list comprehension": "out = [i*i for i in range(N)]",
    "map + lambda": "out = list(map(lambda i: i*i, range(N)))",
}

res_time = {name: [] for name in methods}
res_mem = {name: [] for name in methods}

print("\n" + "=" * 60)
print("Задача 2. Список квадратов: время и пиковая память")
print("timeit: number=1, repeat=5, берём минимум.\n")


def measure_peak_mb(stmt, n):
    """Пик tracemalloc при создании того же списка, что мерит timeit."""
    ns = {"N": n}
    tracemalloc.start()
    exec(stmt, ns)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / (1024 * 1024)


for n in N_values:
    print(f"N={n}:")
    for name, stmt in methods.items():
        times = timeit.repeat(stmt, globals={"N": n}, number=1, repeat=5)
        best_ms = min(times) * 1000
        peak_mb = measure_peak_mb(stmt, n)
        res_time[name].append(best_ms)
        res_mem[name].append(peak_mb)
        print(f"  {name:20s}  время={best_ms:8.2f} мс  память={peak_mb:7.2f} МБ")
    print()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

for name, data in res_time.items():
    ax1.plot(N_values, data, "o-", linewidth=2, label=name)
ax1.set_xlabel("N", fontsize=12)
ax1.set_ylabel("Время (мс)", fontsize=12)
ax1.set_title("Время создания списка квадратов", fontsize=13, fontweight="bold")
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

x = list(range(len(N_values)))
width = 0.25
for i, (name, data) in enumerate(res_mem.items()):
    ax2.bar([pos + (i - 1) * width for pos in x], data, width, label=name, alpha=0.85)
ax2.set_xticks(x)
ax2.set_xticklabels([f"N={n}" for n in N_values])
ax2.set_ylabel("Пиковая память (МБ)", fontsize=12)
ax2.set_title("Пиковая память", fontsize=13, fontweight="bold")
ax2.legend(fontsize=10)
ax2.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
fig.savefig("hw6_task2.png", dpi=150, bbox_inches="tight")

print("График сохранён: hw6_task2.png")
print(
    """
Вывод:
а) По памяти все три способа примерно равны: результат — один и тот же
   список целых чисел, а краткоживущие объекты append и lambda почти
   не поднимают пик. Память определяется результатом, а не способом.
б) По времени list comprehension быстрее: цикл идёт на уровне C,
   без вызова append на каждый элемент.
в) map + lambda медленнее из-за накладных расходов на вызов lambda
   для каждого элемента.
Лучший способ — list comprehension: то же потребление памяти и
меньшее время.
"""
)
