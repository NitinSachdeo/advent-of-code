#!/usr/bin/env python3
import re

result = 0

with open("input.txt", "r") as f:
  enabled = True

  for line in f:
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)

    for match in matches:
      if match == "don't()":
        enabled = False
        continue

      if match == "do()":
        enabled = True
        continue

      if not enabled:
        continue

      a, b = match[4:-1].split(",")
      result += int(a) * int(b)

print(result)
