#!/usr/bin/env python3
from collections import defaultdict

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

def sides(grid, points):
  horizontal_edge_points, vertical_edge_points = set(), set()
  c = None
  for row, col in points:
    if c is None:
      c = grid[row][col]

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      if (
        not 0 <= (new_row := row + x) < height
        or not 0 <= (new_col := col + y) < width
        or grid[new_row][new_col] != c
      ):
        if x != 0:
          horizontal_edge_points.add((row, col))
        if y != 0:
          vertical_edge_points.add((row, col))

  horizontal_edges, vertical_edges = defaultdict(set), defaultdict(set)
  for row, col in horizontal_edge_points:
    if row == 0 or grid[row - 1][col] != c:
      horizontal_edges[row - 0.1].add(col)
    if row + 1 >= height or grid[row + 1][col] != c:
      horizontal_edges[row + 0.1].add(col)

  for row, col in vertical_edge_points:
    if col == 0 or grid[row][col - 1] != c:
      vertical_edges[col - 0.1].add(row)
    if col + 1 >= width or grid[row][col + 1] != c:
      vertical_edges[col + 0.1].add(row)

  result = 0
  for points in list(horizontal_edges.values()) + list(vertical_edges.values()):
    last_point = None
    for i in sorted(list(points)):
      if last_point is None or i != last_point + 1:
        result += 1

      last_point = i

  return result

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
  result += len(points) * sides(grid, points)

print(result)
