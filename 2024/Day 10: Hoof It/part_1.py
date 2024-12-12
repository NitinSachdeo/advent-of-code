#!/usr/bin/env python3
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

    positions = {(row, col)}
    ends = set()
    while positions:
      x, y = positions.pop()
      for x_move, y_move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (
          0 <= (next_x := x + x_move) < height and
          0 <= (next_y := y + y_move) < width and
          (h := grid[next_x][next_y]) == grid[x][y] + 1
        ):
          positions.add((next_x, next_y)) if h < 9 else ends.add((next_x, next_y))

    result += len(ends)

print(result)
