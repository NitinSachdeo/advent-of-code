#!/usr/bin/env python3
from collections import deque

result = 0
grid = []

with open("input.txt", "r") as f:
  for line in f:
    grid.append(list(map(int, line.strip())))

height = len(grid)
width = len(grid[0])

for row in range(height):
  for col in range(width):
    if grid[row][col] != 0:
      continue

    positions = deque([(row, col)])
    while positions:
      x, y = positions.popleft()
      for x_move, y_move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (
          0 <= (next_x := x + x_move) < height and
          0 <= (next_y := y + y_move) < width and
          (h := grid[next_x][next_y]) == grid[x][y] + 1
        ):
          if h == 9:
            result += 1
            continue
          positions.append((next_x, next_y))

print(result)
