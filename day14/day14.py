import hashlib, re

partTwo = False

pat3 = re.compile(r"(\w)\1{2,}")
pat5 = re.compile(r"(\w)\1{4,}")

salt = "zpqevtbw"
index = 0

possibleKeys = {}
hashes = set()

relevantIndex = -1
while relevantIndex == -1:
    key = hashlib.md5(salt + str(index)).hexdigest()

    if partTwo:
        for i in range(2016):
            key = hashlib.md5(key).hexdigest()

    pat = pat3.search(key)
    possibleKeys[index] = (pat.groups()[0] if pat else "Z")

    for x in pat5.findall(key):
        for i in range (1000):
            if x[0] == possibleKeys[index - 1000 + i]:
                hashes.add(index - 1000 + i)
                if len(hashes) == 64:
                    relevantIndex = index - 1000 + i
                    break

    index += 1

print "Part", "Two:" if partTwo else "One:", relevantIndex
