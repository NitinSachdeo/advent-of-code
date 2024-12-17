#!/usr/bin/env python3
result = 0
grid = []

with open("input.txt", "r") as f:
  for line in f:
    grid.append(line.strip())

height = len(grid)
width = len(grid[0])

def dfs(grid, row, col, seen):
  result = set([(row, col)])
  c = grid[row][col]

  for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    if 0 <= (new_row := row + x) < height and 0 <= (new_col := col + y) < width:
      if (new_row, new_col) in seen:
        continue

      if grid[new_row][new_col] != c:
        continue

      seen.add((new_row, new_col))
      result.add((new_row, new_col))
      result.update(dfs(grid, row + x, col + y, seen))

  return result

def perimeter(grid, points):
  edges = 0
  c = None
  for row, col in points:
    if c is None:
      c = grid[row][col]

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      if not 0 <= (new_row := row + x) < height or not 0 <= (new_col := col + y) < width:
        edges += 1
        continue

      if grid[new_row][new_col] != c:
        edges += 1

  return edges

plot_id = 0
plots = {}
seen = set()
for row in range(height):
  for col in range(width):
    if (row, col) in seen:
      continue

    points = dfs(grid, row, col, seen)
    seen.update(points)
    plots[plot_id] = points
    plot_id += 1

for points in plots.values():
  result += len(points) * perimeter(grid, points)

print(result)
