#!/usr/bin/env python3
from collections import defaultdict
from operator import add, sub

result = 0
grid = []
antennas_map = defaultdict(list)
antinodes = set()

with open("input.txt", "r") as f:
  for row, line in enumerate(f):
    grid.append(line.strip())
    for col, c in enumerate(line.strip()):
      if c != ".":
        antennas_map[c].append((row, col))

height = len(grid)
width = len(grid[0])

for antennas in antennas_map.values():
  for i, a in enumerate(antennas):
    for b in antennas[i + 1:]:
      row_diff, col_diff = a[0] - b[0], a[1] - b[1]

      for antenna, op in ((a, add), (b, sub)):
        if 0 <= (x := op(antenna[0], row_diff)) < width and 0 <= (y := op(antenna[1], col_diff)) < height:
          antinodes.add((x, y))

result = len(antinodes)
print(result)
