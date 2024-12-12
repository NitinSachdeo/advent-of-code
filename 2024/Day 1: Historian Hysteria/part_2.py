#!/usr/bin/env python3
from collections import defaultdict

result = 0

with open("input.txt", "r") as f:
    left, right = defaultdict(int), defaultdict(int)
    for line in f:
        a, b = line.split()
        left[int(a)] += 1
        right[int(b)] += 1

    for a in left:
        result += a * left[a] * right[a]

print(result)
