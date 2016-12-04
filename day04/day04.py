#!/usr/bin/env python
import re
import collections

p = re.compile(r"(?P<word>\D+)(?P<sector>\d+)\[(?P<check>\D+)\]")
secs = 0
startIndex = ord("a")

def decrypt(s, shift):
    res = ""
    for c in s:
        newChar = ord(c) + shift
        if newChar > startIndex + 25:
            newChar -= 26
        res += chr(newChar)
    return res

with open("input.txt", "r") as f:
    for line in f:
        #process line
        s = p.search(line)
        word = s.group("word").replace("-","")
        sector = s.group("sector")
        check = s.group("check")

        #count and sort appropriately
        freqs = collections.Counter(word)
        mostFreqs = sorted(freqs.items(), key = lambda pair: (-pair[1], pair[0]))[:5] #use multiple keys for sorting

        #compare to input
        if "".join([x[0] for x in mostFreqs]) == check:
            secs += int(sector)
            name = decrypt(word, int(sector)%26)
            if "northpoleobjects" in name:
                print "Part Two:", name, sector
print "Part One:", secs
