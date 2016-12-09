#!/usr/bin/env python

import re

pat = re.compile(r"\((\d+)x(\d+)\)")

with open("input.txt", "r") as f:
    line = f.read().replace("\n", "")
    continueAt = 0
    length = 0
    for item in pat.finditer(line):
        if item.start() >= continueAt:
            length += item.start() - continueAt
            length += int(item.groups()[0]) * int(item.groups()[1])
            continueAt = item.end() + int(item.groups()[0])
    length += len(line) - continueAt

print "Part One:", length # 99145

# okay let's change everything, keep it simple
# walk through the line and remember how often to count each letter
# assumptions:
# 1) a decomp instruction is never "split" by (being copied by) another
with open("input.txt", "r") as f:
    line = f.read().replace("\n", "")

    prevBrac = -1
    doCount = True
    length = 0
    factor = 1
    actives = []
    for i in range(len(line)):
        c = line[i]
        if c == "(":
            doCount = False
            prevBrac = i
        elif c == ")":
            doCount = True
            nums = [int(x) for x in line[prevBrac + 1 : i].split("x")]
            nums[0] += i
            actives.append(nums) # 0: until, 1: factor
            factor *= nums[1]
        else:
            if doCount:
                length += factor
        # remove now inactive decomps
        remove = []
        for item in actives:
            if i == item[0]:
                remove.append(item)
                factor /= item[1]
        for r in remove:
            actives.remove(r)

print "Part 2:", length # 10943094568
