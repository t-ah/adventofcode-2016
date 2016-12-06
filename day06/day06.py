#!/usr/bin/env python
from collections import Counter

counters = []
for i in range(8):
    counters.append(Counter())

with open("input.txt", "r") as f:
    for line in f:
        for i in range(8):
            counters[i][line[i]] += 1

result, result2 = "", ""
for i in range(8):
    result += counters[i].most_common(1)[0][0]
    result2 += counters[i].most_common()[:-2:-1][0][0]
print "Part One:", result, "\nPart Two:", result2
