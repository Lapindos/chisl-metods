import numpy as np

print("hw-3.15 20.11.2026")

rng = np.random.default_rng(42)
raw = rng.normal(loc=20, scale=2, size=(30, 4))
raw[7, 2] = 100

print("1. shape", raw.shape, "dtype", raw.dtype, "size", raw.size)

mask = np.abs(raw - raw.mean(axis=0)) > 3 * raw.std(axis=0)
print("2. выбросов:", int(mask.sum()))
print(mask)

cleaned = raw.astype(float).copy()
cleaned[mask] = np.nan
col_mean = np.nanmean(cleaned, axis=0)
cleaned = np.where(np.isnan(cleaned), col_mean, cleaned)
print("3. после замены выброса средними по столбцам:\n", np.round(cleaned, 3))

there = cleaned.T
back = there.T
print("4. туда и обратно .T, данные те же:", np.array_equal(back, cleaned))

flat = cleaned.ravel()
restored = flat.reshape(30, 4)
print("5. ravel и обратно reshape, данные те же:", np.array_equal(restored, cleaned))

print("6. средние датчиков", cleaned.mean(axis=0))
print("6. std датчиков", cleaned.std(axis=0))

norm = (cleaned - cleaned.mean(axis=0)) / cleaned.std(axis=0)
print("7. средние после нормировки", norm.mean(axis=0))
print("7. std после нормировки", norm.std(axis=0))
print("средние ≈ 0:", np.allclose(norm.mean(axis=0), 0))
print("std ≈ 1:", np.allclose(norm.std(axis=0), 1))

print("Вывод: copy() понадобился, чтобы замена выброса на nan не портила исходные измерения.")
print("Broadcasting сработал в маске выброса, в замене nan на среднее и в нормировке столбцов: вектор длины 4 сам лёг на все строки.")
print(".T и ravel здесь view, они не копируют таблицу. Ошибка формы была бы, если вычесть среднее строк без keepdims из таблицы (30, 4).")
print("ravel потом reshape вернул ту же таблицу, потому что число элементов 120 = 30 * 4.")
