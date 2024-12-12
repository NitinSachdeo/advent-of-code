#!/usr/bin/env python3
from bisect import insort

result = 0

with open("input.txt", "r") as f:
    left, right = [], []
    for line in f:
        a, b = line.split()
        insort(left, int(a))
        insort(right, int(b))

    for a, b in zip(left, right):
        result += abs(a - b)

print(result)
