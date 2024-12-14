#!/usr/bin/env python3
result = 0
row, col = 0, 0
grid = []
turn_map = {"up": "right", "right": "down", "down": "left", "left": "up"}

with open("input.txt", "r") as f:
  for line in f:
    grid.append(line.strip())
    if "^" in grid[-1]:
      row, col = len(grid) - 1, grid[-1].find("^")

height = len(grid)
width = len(grid[0])
direction = "up"
visited = set()

while True:
  visited.add((row, col))

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

result = len(visited)
print(result)
