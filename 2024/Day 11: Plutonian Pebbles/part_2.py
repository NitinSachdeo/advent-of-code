#!/usr/bin/env python3
from collections import Counter
from tqdm import tqdm

result = 0
stones = []
cache = {}

with open("input.txt", "r") as f:
  for line in f:
    stones = list(map(int, line.strip().split()))

STEPS = 75
PART_ONE = 40
PART_TWO = STEPS - PART_ONE

def simulate_blink(stone, steps, cache, do_cache_array=True):
  if (key := (stone, steps)) in cache:
    return cache[key][0], cache[key][1], cache

  stones = [stone]
  for i in range(steps):
    new_stones = []
    for sub_stone in stones:
      if sub_stone == 0:
        new_stones.append(1)
      elif (l := len(str(sub_stone))) % 2 == 0:
        new_stones.extend([
          int(str(sub_stone)[:l // 2]),
          int(str(sub_stone)[l // 2:])
        ])
      else:
        new_stones.append(sub_stone * 2024)

      if i == PART_TWO:
        cache[(stone, i + 1)] = len(new_stones), (new_stones if do_cache_array else [])
    stones = new_stones

  return len(new_stones), new_stones, cache

new_stones = []
for stone in tqdm(stones):
  _, l, cache = simulate_blink(stone, PART_ONE, cache)
  new_stones.extend(l)
stones = new_stones

counts = Counter(stones)
for stone, count in tqdm(counts.items()):
  if (key := (stone, PART_TWO)) in cache:
    result += cache[key][0] * count
  else:
    c, _, cache = simulate_blink(stone, PART_TWO, cache, do_cache_array=False)
    result += c * count

print(result)
