discs = []

partTwo = False

with open("input.txt", "r") as f:
    for line in f:
        words = line.replace("\n", "").split(" ")
        discs.append([int(words[3]), int(words[11][:-1])])

    if partTwo:
        discs.append([11, 0])

    for i in range(len(discs)):
        discs[i][1] = (discs[i][1] + i + 1) % discs[i][0]

index = 0
found = False

def rotate(l):
    l[1] = (l[1] + 1) % l[0]

while not found:
    map(rotate, discs)
    index += 1
    found = True
    for disc in discs:
        if not disc[1] == 0:
            found = False
            break

print "Part", "Two:" if partTwo else "One:", index
