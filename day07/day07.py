#!/usr/bin/env python
import re
from itertools import product

pBrac = re.compile("(\[[^]]*\])")
p = re.compile("(?P<a>\D)(?P<b>\D)(?P=b)(?P=a)")

count = 0

with open("input.txt", "r") as f:
    for line in f:
        splits = re.split(pBrac, line)
        tls = "POS"
        for item in splits:
            if tls == "IMP": break
            for abba in re.findall(p, item):
                if abba[0] == abba[1]: continue # this could be done in the regex, see part 2
                if item[0] == "[":
                    tls = "IMP"
                    break
                else:
                    tls = "CONF"
        if tls == "CONF": count += 1

print "Part One:", count

# capture a letter, assert it does not repeat and capture it again; lookahead in the beginning to allow for overlapping
pABA = re.compile("(?=((?P<a>\D)(?!(?P=a))\D(?P=a)))")

count2 = 0

with open("input.txt", "r") as f:
    for line in f:
        hseqs, rest, abas = [], [], []
        splits = re.split(pBrac, line)
        for item in splits: # sort by super and hypernets
            if item[0] == "[":
                hseqs.append(item)
            else:
                rest.append(item)
        for item in rest:
            for aba in re.findall(pABA, item):
                abas.append(aba[0][1]+aba[0][0]+aba[0][1])
        for (item, aba) in product(hseqs, abas):
            if aba in item:
                count2 += 1
                break

print "Part Two:", count2
