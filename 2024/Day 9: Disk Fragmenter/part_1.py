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

i = 0
for block, size in blocks:
  if block != ".":
    while size > 0:
      result += i * block
      i += 1
      size -= 1
  else:
    while size > 0:
      while blocks[-1][0] == "." or blocks[-1][1] == 0:
        blocks.pop()

      result += i * blocks[-1][0]
      blocks[-1][1] -= 1
      size -= 1
      i += 1

print(result)
