#!/usr/bin/env python
f = open("input.txt")

button = 5
code = ""

for line in f:
    for char in line:
        if char == "U":
            if button > 3:
                button -= 3
        elif char == "D":
            if button < 7:
                button += 3
        elif char == "L":
            if not button in [1,4,7]:
                button -= 1
        elif char == "R":
            if not button%3 == 0:
                button += 1
        else:
            print "finish line" # catch linebreaks
    code += str(button)

print "Part One:", code

# Part Two - I think this needs a complete overhaul
x, y = 3, 1
code = ""

# I could not quickly find a pattern in the pad :(
pad = [ [False,False,False,False,False,False,False],
        [False,False,False,1,False,False,False],
        [False,False,2,3,4,False,False],
        [False,5,6,7,8,9,False],
        [False,False,"A","B","C",False,False],
        [False,False,False,"D",False,False,False],
        [False,False,False,False,False,False,False],
      ]

f = open("input.txt")
for line in f:
    for char in line:
        if char == "L" and not pad[x][y-1] == False:
            y -= 1
        elif char == "R" and not pad[x][y+1] == False:
            y += 1
        elif char == "U" and not pad[x-1][y] == False:
            x -= 1
        elif char == "D" and not pad[x+1][y] == False:
            x += 1
    code += str(pad[x][y])

print "Part Two:", code
