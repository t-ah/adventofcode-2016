import sys

numbers = []

with open("input.txt", "r") as f:
    for line in f:
        l = line.replace("\n", "").split("-")
        numbers.append([int(l[0]), "F"])
        numbers.append([int(l[1]), "T"])

numbers.sort()

# Part 1:
f = 0
prevT = sys.maxint
for item in numbers:
    if item[1] == "F":
        if f == 0 and prevT < item[0] - 1:
            break
        f += 1
    else:
        f -= 1
        if f == 0:
            prevT = item[0]

print "Part 1:", prevT + 1 # 19449262

# Part 2:
f = 0
prevF = -1
ipCount = 0
for item in numbers:
    if item[1] == "F":
        if f == 0:
            prevF = item[0]
        f += 1
    else:
        f -= 1
        if f == 0:
            ipCount += (item[0] - prevF) + 1

print "Part 2:", 4294967295 - ipCount + 1 # do not forget IP 0
