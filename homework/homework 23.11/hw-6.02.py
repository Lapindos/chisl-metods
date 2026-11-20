import timeit
import tracemalloc

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("hw-6.02")

sizes = [50_000, 200_000, 800_000]
names = ["append", "comprehension", "map+lambda"]
codes = [
    "out = []\nfor i in range(N):\n    out.append(i*i)",
    "out = [i*i for i in range(N)]",
    "out = list(map(lambda i: i*i, range(N)))",
]

times = [[], [], []]
memory = [[], [], []]

for n in sizes:
    print(f"N={n}")
    for i, code in enumerate(codes):
        measured = timeit.repeat(code, globals={"N": n}, number=1, repeat=5)
        best = min(measured)
        times[i].append(best * 1000)

        tracemalloc.start()
        exec(code, {"N": n})
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory[i].append(peak / 1024 / 1024)

        print(f"  {names[i]:<14} время={best*1000:8.2f} мс   память={peak / 1024 / 1024:6.2f} МБ")
    print()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
colors = ["crimson", "steelblue", "seagreen"]
markers = ["o", "s", "^"]
for i, name in enumerate(names):
    ax1.plot(sizes, times[i], markers[i] + "-", color=colors[i], linewidth=2, label=name)

ax1.set_xlabel("N")
ax1.set_ylabel("Время (мс)")
ax1.set_title("Время создания списка квадратов")
ax1.legend()
ax1.grid(True, alpha=0.3)

x = list(range(len(sizes)))
width = 0.25
for i, name in enumerate(names):
    shift = (i - 1) * width
    xs = [item + shift for item in x]
    ax2.bar(xs, memory[i], width=width, color=colors[i], label=name)

ax2.set_xticks(x)
ax2.set_xticklabels([f"N={n}" for n in sizes])
ax2.set_ylabel("Пиковая память (МБ)")
ax2.set_title("Память")
ax2.legend()
ax2.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
fig.savefig("hw-6.02.png", dpi=150, bbox_inches="tight")
print("График сохранён: hw-6.02.png")
