# For part one: A* because why not
# For part two: well.. as always part one does not help me much
from collections import defaultdict
import sys

pInput = 1358
start = (1,1)
goal = (31,39)

def isWall(x, y):
    return str(bin((3+x)*x + 2*x*y + (y+1)*y +pInput))[2:].count("1") % 2 == 1

def h(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def neighbors(x, y):
    for neighbor in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if neighbor[0] >= 0 and neighbor[1] >= 0 and not isWall(neighbor[0], neighbor[1]):
            yield neighbor

# it would be nice to have a p-queue with set property here
def findCurrent(openSet, fScore):
    score = sys.maxint
    ret = False
    for n in openSet:
        if fScore[n] < score:
            score = fScore[n]
            ret = n
    return ret

def reconstruct(cameFrom, current):
    path = []
    while current in cameFrom:
        current = cameFrom[current]
        path.append(current)
    return path

def aStar(start, goal):
    closedSet = set()
    openSet = set()
    openSet.add(start)
    cameFrom = {}

    gScore = defaultdict(lambda: sys.maxint)
    gScore[start] = 0
    fScore = defaultdict(lambda: sys.maxint)
    fScore[start] = h(start, goal)

    while len(openSet) > 0:

        current = findCurrent(openSet, fScore)

        if current == goal:
            return reconstruct(cameFrom, current)
        closedSet.add(current)
        openSet.remove(current)
        for neighbor in neighbors(current[0], current[1]):
            if neighbor in closedSet:
                continue
            tentGScore = gScore[current] + 1
            if not neighbor in openSet:
                openSet.add(neighbor)
            elif tentGScore >= gScore[neighbor]:
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentGScore
            fScore[neighbor] = gScore[neighbor] + h(neighbor, goal)

    return False

path = aStar(start, goal)
print "Part One:", len(path)

#for y in range(10):
#    s = ""
#    for x in range(10):
#        s += ("#" if isWall(x,y) else " ")
#    print s

# Part Two
visited = set()
fringe = set()
fringe.add(start)

for _ in range(50):
    newFringe = set()
    for current in fringe:
        for neighbor in neighbors(current[0], current[1]):
            if (not neighbor in fringe) and (not neighbor in visited):
                newFringe.add(neighbor)
    visited = visited.union(fringe)
    fringe = newFringe
print "Part Two:", len(visited.union(fringe))
