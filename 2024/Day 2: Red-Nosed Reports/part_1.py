#!/usr/bin/env python3
result = 0

with open("input.txt", "r") as f:
  m = []
  for line in f:
    m.append(list(map(int, line.split())))

  for row in m:
    safe = True
    pos_diff = row[0] < row[1]

    for i, j in zip(row[0:len(row) - 1], row[1:len(row)]):
      if (not 0 < abs(i - j) < 4) or (pos_diff ^ ((j - i) > 0)):
        safe = False
        break

    if safe:
      result += 1

print(result)
