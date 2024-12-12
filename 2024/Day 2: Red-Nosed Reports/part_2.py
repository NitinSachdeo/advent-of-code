#!/usr/bin/env python3
result = 0

with open("input.txt", "r") as f:
  m = []
  for line in f:
    l = list(map(int, line.split()))
    m.append(l)

  for row in m:
    for skip_idx in range(len(row)):
      safe = True
      temp_row = row.copy()
      temp_row.pop(skip_idx)
      pos_diff = temp_row[0] < temp_row[1]

      for i, j in zip(temp_row[0:len(temp_row) - 1], temp_row[1:len(temp_row)]):
        if (not 0 < abs(i - j) < 4) or (pos_diff ^ ((j - i) > 0)):
          safe = False
          break

      if safe:
        result += 1
        break

print(result)
