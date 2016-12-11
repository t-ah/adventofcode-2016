# 1) kind of BFS today.
# 2) Part Two very slow, I'm sorry.
# 2a) coincidentally(?), moving the additional parts to floor 4 and moving the elevator
# back to floor one (using other parts on the way and ignoring possible contradictions)
# supplies the correct answer (adding the moves to the answer for part one).

import re, copy
from itertools import product

patGen = re.compile(r" (\S+) generator")
patChip = re.compile(r" (\S+)-compatible")

items = {0:[], 1:[], 2:[], 3:[]}
found = False
step = 0
nodes = [[0, items]]
floor = 0
itemCount = 0

lookup = {}
visitList = {}

# check if node was already visisted, if not, treat it as visited from now on
def visited(floor, nodeItems):
    code = str(floor)
    for floor in range(4):
        code += str(floor)
        nodeItems[floor].sort()
        code += "".join(nodeItems[floor])
    if code in visitList:
        return True
    else:
        visitList[code] = True
        return False

# get a shorter alias for the string (optimize string lengths a bit)
def getAlias(name):
    if not name in lookup:
        lookup[name] = str(len(lookup))
    return lookup[name]

# parse input
with open("input.txt", "r") as f:
    # items[0] += ["ga", "ca", "gb", "cb"] # enable this line for part two (kind of bad running time)
    for line in f:
        items[floor] += ["g" + getAlias(x) for x in patGen.findall(line)]
        items[floor] +=  ["c" + getAlias(x) for x in patChip.findall(line)]
        itemCount += len(items[floor])
        floor += 1

# check if old and new floor still valid
def isValid(node, oldFloor):
    newFloor = node[0]
    items = node[1]
    for floor in [oldFloor, newFloor]:
        gen = False
        for item in items[floor]:
            if item[0] == "g":
                gen = True
                break
        if gen:
            for item in items[floor]:
                if item[0] == "c" and not "g"+item[1:] in items[floor]:
                    return False
    return True

# expand the node, append new nodes to the given list
def expand(node, appendTo):
    floor = node[0]
    items = node[1]

    nextFloors = []
    if floor > 0:
        nextFloors.append(floor - 1)
    if floor < 3:
        nextFloors.append(floor + 1)

    for nextFloor in nextFloors:
        # move one item
        for item in items[floor]:
            newNode = [nextFloor, copy.deepcopy(items)]
            newNode[1][floor].remove(item)
            newNode[1][nextFloor].append(item)
            if len(newNode[1][3]) == itemCount:
                return True
            if (not visited(nextFloor, newNode[1])) and isValid(newNode, floor):
                appendTo.append(newNode)
        # move two items
        for (it1, it2) in product(items[floor], items[floor]):
            if not it1 == it2:
                newNode = [nextFloor, copy.deepcopy(items)]
                for it in [it1, it2]:
                    newNode[1][floor].remove(it)
                    newNode[1][nextFloor].append(it)
                if len(newNode[1][3]) == itemCount:
                    return True
                if (not visited(nextFloor, newNode[1])) and isValid(newNode, floor):
                    appendTo.append(newNode)
    return False

while not found:
    step += 1
    print step, len(nodes) # progress
    newNodes = []
    for node in nodes:
        if expand(node, newNodes):
            found = True
            break
    nodes = newNodes
    if step == 100: break # this is hopefully big enough

print "Part One/Two:", step, "steps"
