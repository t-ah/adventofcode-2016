#!/usr/bin/env python
from collections import defaultdict

f = open("input.txt")

instrs = f.readline()[:-1].split(", ")
direction = 0
steps = [0,0,0,0]
locations = defaultdict(bool)
locations[0,0] = True
partTwo = False

def location(s):
    return steps[0] - steps[2], steps[1] - steps[3]

for instr in instrs:
    turn = instr[0]
    times = int(instr[1:])
    if turn == "L":
        direction -= 1
    else:
        direction += 1

    # for Part Two, remember all locations
    for i in range(times):
        steps[direction%4] += 1
        if not partTwo:
            x,y = location(steps)
            if (x,y) in locations:
                print "Day 1 - Part Two:", abs(x) + abs(y)
                partTwo = True
            else:
                locations[x,y] = True

    # relic from Part One
    # steps[direction%4] += times

x, y = location(steps)
distance = abs(x) + abs(y)

print "Day 1 - Part One:", distance
