#!/usr/bin/env python3
result = 0

with open("input.txt", "r") as f:
  grid = []
  for line in f:
    grid.append(line.strip())

height = len(grid)
width = len(grid[0])

for row in range(height):
  for col in range(width):
    if grid[row][col] != "X":
      continue

    # Horizontal
    if grid[row][col:col + 4] == "XMAS":
      result += 1

    # Horizontal Backwards
    if grid[row][col - 3:col + 1] == "SAMX":
      result += 1

    # Vertical
    if "".join(s[col] for s in grid[row:row + 4]) == "XMAS":
      result += 1

    # Vertical Backwards
    if "".join(s[col] for s in grid[row - 3:row + 1]) == "SAMX":
      result += 1

    if col > 2:
      # Up Left
      if "".join(s[col - (3 - i)] for i, s in enumerate(grid[row - 3:row + 1])) == "SAMX":
        result += 1
      # Down Left
      if "".join(s[col - i] for i, s in enumerate(grid[row:row + 4])) == "XMAS":
        result += 1

    # Up Right
    if "".join(s[col + (3 - i): col + (4 - i)] for i, s in enumerate(grid[row - 3:row + 1])) == "SAMX":
      result += 1

    # Down Right
    if "".join(s[col + i: col + i + 1] for i, s in enumerate(grid[row:row + 4])) == "XMAS":
      result += 1

print(result)
