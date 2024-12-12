#!/usr/bin/env python3
from tqdm import tqdm

result = 0
grid = []
turn_map = {"up": "right", "right": "down", "down": "left", "left": "up"}

with open("input.txt", "r") as f:
  for line in f:
    grid.append(list(line.strip()))
    if "^" in grid[-1]:
      start_row, start_col = len(grid) - 1, grid[-1].index("^")

height = len(grid)
width = len(grid[0])

for h in tqdm(range(height)):
  for w in range(width):
    direction = "up"
    visited = set()
    row, col = start_row, start_col

    if grid[h][w] != ".":
      continue

    grid[h][w] = "#"
    while True:
      if (row, col, direction) in visited:
        result += 1
        break

      visited.add((row, col, direction))
      match direction:
        case "up":
          next_row, next_col = row - 1, col
        case "right":
          next_row, next_col = row, col + 1
        case "down":
          next_row, next_col = row + 1, col
        case "left":
          next_row, next_col = row, col - 1

      if not 0 <= next_row < height or not 0 <= next_col < width:
        break

      if grid[next_row][next_col] != "#":
        row, col = next_row, next_col
        continue

      direction = turn_map[direction]

    grid[h][w] = "."

print(result)
