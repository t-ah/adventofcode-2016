import hashlib

code = "udskfozm"
openChars = ["b", "c", "d", "e", "f"]

nodes = [(0, 0, "")]

found = False

res = ["", ""]

def expand(node, nodes, res):
    h = hashlib.md5(code + node[2]).hexdigest()[:4]
    x, y = node[0], node[1]
    if h[0] in openChars and y > 0: # up
        nodes.append((x, y - 1, node[2] + "U"))
    if h[1] in openChars and y < 3: # down
        if x == 3 and y == 2:
            if res[0] == "":
                res[0] = node[2] + "D"
            res[1] = node[2] + "D"
        else:
            nodes.append((x, y + 1, node[2] + "D"))
    if h[2] in openChars and x > 0: # left
        nodes.append((x - 1, y, node[2] + "L"))
    if h[3] in openChars and x < 3: # right
        if x == 2 and y == 3:
            if res[0] == "":
                res[0] = node[2] + "R"
            res[1] = node[2] + "R"
        else:
            nodes.append((x + 1, y, node[2] + "R"))

while len(nodes) > 0:
    newNodes = []
    for node in nodes:
        expand(node, newNodes, res)
    nodes = newNodes

print "Part One:", res[0]
print "Part Two:", len(res[1])
