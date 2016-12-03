#!/usr/bin/env python
import re
from itertools import islice

def isTriang(sides):
    return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

p = re.compile("\d+")
f = open("input.txt")
result = 0

for line in f:
    nums = p.findall(line)
    nums = [ int(x) for x in nums ]
    if isTriang(nums):
        result += 1

print "Part One:", result

# Part Two (start anew, yay)
with open("input.txt", "r") as f:
    result = 0
    while True:
        lines = list(islice(f, 3)) # read 3 lines at once
        if not lines: break
        nums = []
        for line in lines: # parse numbers
            nums.append([int(x) for x  in p.findall(line)])
        for i in range(3): # check the correct numbers against each other
            if isTriang([nums[0][i],nums[1][i],nums[2][i]]):
                result += 1
print "Part Two:", result
