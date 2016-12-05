#!/usr/bin/env python

import hashlib # oh how I missed this last year
from collections import defaultdict

puzzleInput = "ugkcyxxp" # no file today

pw = ""
pw2 = defaultdict(str)
counter = 0

while True:
    hexa = hashlib.md5(puzzleInput + str(counter)).hexdigest()
    #m.update(puzzleInput + str(counter))
    #hexa = m.hexdigest()
    if hexa.startswith("00000"):
        if len(pw) < 8: pw += hexa[5]
        pos = int(hexa[5], 16)
        if pos < 8 and not pw2[pos]: pw2[pos] = hexa[6]
        if len(pw) == 8 and len(pw2) == 8: break
    counter += 1

print "Part One:", pw
print "Part Two:", "".join(pw2.values())
