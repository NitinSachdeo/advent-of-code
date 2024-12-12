#!/usr/bin/env python3
result = 0
ordering = set()
pages_list = []

with open("input.txtc", "r") as f:
  for line in f:
    if "|" in line:
      ordering.add(tuple(map(int, line.strip().split("|"))))
    elif "," in line:
      pages_list.append(tuple(map(int, line.strip().split(","))))

for pages in pages_list:
  unsafe = set()
  for i, left in enumerate(pages):
    for right in pages[i + 1:]:
      if (right, left) in ordering:
        unsafe.add(i)

  if unsafe:
    ordered_pages = [page for i, page in enumerate(pages) if i not in unsafe]
    for unsafe_idx in unsafe:
      for i, page in enumerate(ordered_pages):
        if (page, pages[unsafe_idx]) in ordering:
          continue

        ordered_pages.insert(i, pages[unsafe_idx])
        break
      else:
        ordered_pages.append(pages[unsafe_idx])

    result += ordered_pages[len(pages) // 2]

print(result)
