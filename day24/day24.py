# A* borrowed from day 13

from collections import defaultdict
from itertools import permutations
import sys

lines = []
goals = {}
grid = defaultdict(str)

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        grid[(i,j)] = line[j]
        if line[j] not in [".", "#"]:
            goals[line[j]] = (i,j)

def h(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def neighbors(x, y, grid):
    for neighbor in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if grid[neighbor] != "#":
            yield neighbor

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

def aStar(start, goal, grid):
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
        for neighbor in neighbors(current[0], current[1], grid):
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

# calculate all shortest paths
shortestPaths = {}
for i in range(len(goals)):
    startXY = goals[str(i)]
    for j in range(len(goals) - i - 1):
        index = i + j + 1
        goalXY = goals[str(index)]
        shortestPaths[(i,index)] = len(aStar(startXY, goalXY, grid))
        shortestPaths[(index, i)] = shortestPaths[(i, index)] # we afford some convenience, it's christmas

# basically, it's a TSP now

minPath = sys.maxint
for p in permutations(range(1, len(goals))):
    path = shortestPaths[(0, p[0])]
    for i in range(len(p) - 1):
        path += shortestPaths[(p[i], p[i+1])]
    minPath = min(path, minPath)
print "Part 1:", minPath

# Part 2

minPath = sys.maxint
for p in permutations(range(1, len(goals))):
    path = shortestPaths[(0, p[0])]
    for i in range(len(p) - 1):
        path += shortestPaths[(p[i], p[i+1])]
    path += shortestPaths[p[i+1], 0] # this is new
    minPath = min(path, minPath)
print "Part 2:", minPath
