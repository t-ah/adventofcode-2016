# 2016/12/12: Added some optimization to the visited() method to implicitly check for equivalent states now
# running in kind of good time now (I'm satisfied at least)

# 1) kind of BFS today.
# 2) Part Two very slow, I'm sorry.
# 2a) coincidentally(?), moving the additional parts to floor 4 and moving the elevator
# back to floor one (using other parts on the way and ignoring possible contradictions)
# supplies the correct answer (adding the moves to the answer for part one).

import re, copy
from itertools import product

partTwo = False

patGen = re.compile(r" (\S+) generator")
patChip = re.compile(r" (\S+)-compatible")

items = {0:[], 1:[], 2:[], 3:[]}
found = False
step = 0
nodes = [[0, items]]
floor = 0
itemCount = 0

visitList = {}

# check if node was already visisted, if not, treat it as visited from now on
def visited(floor, nodeItems):
    lookup = {}
    code = str(floor)

    gens = {}
    # prepare optimization
    for floorNo in range(4):
        for item in nodeItems[floorNo]:
            if item[0] == "g":
                gens[item[1]] = str(floorNo)

    for floor in range(4):
        code += ":"

        #nodeItems[floor].sort()
        # first optimization attempt for historic reasons
        #code += "".join([x[:1] + getAlias(x[1:], lookup) for x in nodeItems[floor]]) # catches a few equivalent states (but not many)

        # try some weird code now (only store chips pointing to their gen, sort chips)
        chips = []
        for item in nodeItems[floor]:
            if item[0] == "c":
                chips.append(gens[item[1]]) # append floorNo of the corresp. generator
        chips.sort()
        code += "".join( chips )
        # oh daym it worked

    if code in visitList:
        return True
    else:
        visitList[code] = True
        return False

# get a shorter alias for the string (optimize string lengths a bit)
def getAlias(name, lookup):
    if not name in lookup:
        lookup[name] = str(len(lookup))
    return lookup[name]

# parse input
with open("input.txt", "r") as f:
    if partTwo:
        items[0] += ["ga", "ca", "gb", "cb"] # enable this line for part two
    lookup = {}
    for line in f:
        items[floor] += ["g" + getAlias(x, lookup) for x in patGen.findall(line)]
        items[floor] +=  ["c" + getAlias(x, lookup) for x in patChip.findall(line)]
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
