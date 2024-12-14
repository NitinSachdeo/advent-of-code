#!/usr/bin/env python3
result = 0

with open("input.txt", "r") as f:
  grid = []
  for line in f:
    grid.append(line.strip())

height = len(grid)
width = len(grid[0])

for row in range(1, height - 1):
  for col in range(1, width - 1):
    if grid[row][col] != "A":
      continue

    corners = "".join((
      grid[row - 1][col - 1],  # Top Left
      grid[row - 1][col + 1],  # Top Right
      grid[row + 1][col + 1],  # Bottom Right
      grid[row + 1][col - 1],  # Bottom Left
    ))
    if corners in ("MMSS", "SMMS", "SSMM", "MSSM"):
      result += 1

print(result)
