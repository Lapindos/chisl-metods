import math
import random
import sys

import numpy as np

print("hw-1.13")
print("Python", sys.version.split()[0])
print("numpy", np.__version__)

def make_data(seed):
    random.seed(seed)
    py_data = [random.random() for _ in range(10**5)]
    rng = np.random.default_rng(seed)
    np_data = rng.random(10**5)
    return py_data, np_data

def three_sums(values):
    return sum(values), math.fsum(values), float(np.sum(values))

def report(seed):
    py_data, np_data = make_data(seed)
    py_sums = three_sums(py_data)
    np_sums = three_sums(np_data)
    print(f"seed={seed}")
    print("  random.seed  sum / fsum / numpy.sum:", py_sums)
    print("  default_rng  sum / fsum / numpy.sum:", np_sums)
    print("  |sum - fsum| для random:", abs(py_sums[0] - py_sums[1]))
    print("  |sum - fsum| для rng:   ", abs(np_sums[0] - np_sums[1]))
    return py_sums, np_sums

first = report(42)
second = report(42)
third = report(43)

print("два запуска с seed=42 совпали:", first == second)
print("seed=43 дал другие суммы:", first != third)
