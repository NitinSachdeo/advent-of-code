#!/usr/bin/env python3
result = 0
blocks = []

with open("input.txt", "r") as f:
  for line in f:
    s = line.strip()

s += "0"
for file_id, (file, gap) in enumerate(zip(s[::2], s[1::2])):
  blocks.append([file_id, int(file)])
  blocks.append([".", int(gap)])
blocks.pop()

right = len(blocks) - 1
while right > 0:
  if blocks[right][0] == ".":
    right -= 1
    continue

  left = 0
  while left < right:
    if blocks[left][0] == "." and blocks[left][1] >= blocks[right][1]:
      if blocks[left][1] != blocks[right][1]:
        blocks.insert(left + 1, [".", blocks[left][1] - blocks[right][1]])
        right += 1
      blocks[left] = blocks[right].copy()
      blocks[right][0] = "."
      break

    left += 1
  right -= 1

i = 0
for block, size in blocks:
  while size > 0:
    if block != ".":
      result += block * i
    size -=1
    i += 1

print(result)
