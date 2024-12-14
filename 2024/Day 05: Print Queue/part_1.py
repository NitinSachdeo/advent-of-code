#!/usr/bin/env python3
result = 0
ordering = set()
pages_list = []

with open("input.txt", "r") as f:
  for line in f:
    if "|" in line:
      ordering.add(tuple(map(int, line.strip().split("|"))))
    elif "," in line:
      pages_list.append(tuple(map(int, line.strip().split(","))))

for pages in pages_list:
  unsafe = False
  for i, left in enumerate(pages):
    for right in pages[i + 1:]:
      if (right, left) in ordering:
        unsafe = True
        break

    if unsafe: break
  if unsafe: continue
  result += pages[len(pages) // 2]

print(result)
