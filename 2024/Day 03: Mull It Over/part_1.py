#!/usr/bin/env python3
import re

result = 0

with open("input.txt", "r") as f:
  for line in f:
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
    for match in matches:
      a, b = match[4:-1].split(",")
      result += int(a) * int(b)

print(result)
