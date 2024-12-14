#!/usr/bin/env python3
from tqdm import tqdm

result = 0
equations = []
operators = ["+", "*"]

with open("input.txt", "r") as f:
  for line in f:
    out, ins = line.strip().split(": ")
    equations.append((int(out), list(map(int, ins.split()))))

for out, ins in tqdm(equations):
  answers = {ins[0]}
  for n in ins[1:]:
    next_answers = set()
    for a in answers:
      for operator in operators:
        next_answers.add(eval(f"{a}{operator}{n}"))

    answers = next_answers

  if out in answers:
    result += out

print(result)
