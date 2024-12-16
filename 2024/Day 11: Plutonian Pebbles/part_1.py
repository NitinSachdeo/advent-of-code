#!/usr/bin/env python3
result = 0
stones = []

with open("test.txt", "r") as f:
  for line in f:
    stones = list(map(int, line.strip().split()))

for _ in range(25):
  new_stones = []

  for stone in stones:
    if stone == 0:
      new_stones.append(1)
    elif (l := len(str(stone))) % 2 == 0:
      new_stones.extend([
        int(str(stone)[:l // 2]),
        int(str(stone)[l // 2:])
      ])
    else:
      new_stones.append(stone * 2024)

  stones = new_stones

result = len(stones)
print(result)
