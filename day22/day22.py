import re
from collections import defaultdict

pat = re.compile(r"x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T")

inputData = []
data = defaultdict(list)
rows = {}
with open("input.txt", "r") as f:
    inputData = f.read().split("\n")

for i in range(len(inputData) - 3):
    m = pat.search(inputData[i + 2])
    x, y, used, avail = m.groups()
    data[(int(x), int(y))] = [int(used), int(avail)]
    rows[x] = y

viables = set() # only count distinct pairs

for dx, dy in data.keys():
    used, _ = data[(dx, dy)]
    if used == 0:
        continue
    #for x, y in [(dx + 1, dy), (dx - 1, dy), (dx, dy + 1), (dx, dy - 1)]:
    for x, y in data.keys():
        #if data[(x, y)]:
        if x != dx or y != dy:
            _, avail = data[(x, y)]
            if used <= avail:
                pair = [(x,y), (dx,dy)]
                pair.sort()
                viables.add(tuple(pair))

print "Part 1:", len(viables)

#######################################################

# move the empty tile left of the goal tile, then move the goal tile left with the
# help of the empty tile; this only works because of the special input
# which was probably to be found out in part 1
# which I really do not like
# but well
# whatever

gx = len(rows) - 1
empty = (26, 12) # spied from input data, of course needs to be changed for general input
# then again, general input does not seem to be today's topic

# compute shortest path (of the empty tile!!) with an optional forbidden tile
def shortest((fx, fy), (tx, ty), data, forbidden):
    nodes = set([(fx,fy)])
    visited = set()
    path = 0
    while not (tx,ty) in nodes:
        path += 1
        newNodes = []
        for (nx, ny) in nodes:
            use, avail = data[(nx, ny)]
            for (x,y) in [(nx + 1, ny), (nx - 1, ny), (nx, ny + 1), (nx, ny - 1)]:
                if not (x, y) in visited:
                    if (x, y) == forbidden:
                        continue
                    if data[(x, y)]:
                        use2, _ = data[(x, y)]
                        if avail + use > use2:
                            visited.add((x, y))
                            newNodes.append((x,y))
        nodes = newNodes
    return path

count = shortest(empty, (gx - 1, 0), data, (-1, -1))
for i in range(gx - 1):
    count += shortest((gx - i, 0), (gx - i - 2, 0), data, (gx - i - 1, 0))
count += gx

print "Part 2:", count
