#!/usr/bin/env python

from collections import defaultdict

with open("input.txt", "r") as f:
    vals = defaultdict(list)
    instrs = {}

    # parse initial values and instructions
    for line in f:
        words = line.replace("\n", "").split(" ")
        if words[0] == "value":
            vals[words[5]].append(int(words[1]))
        else:
            instrs[words[1]] = words[5:7] + words[10:12]

    # let's just simulate it
    found = None
    outsFound = False
    outs = defaultdict(int)
    while not found or not outsFound:
        bots = vals.keys()
        for bot in bots:
            botVals = vals[bot]
            if len(botVals) == 2:
                if botVals[0] < botVals[1]:
                    low, high = botVals[0], botVals[1]
                else:
                    high, low = botVals[0], botVals[1]

                if low == 17 and high == 61:
                    found = bot

                if instrs[bot][0] == "bot":
                    vals[instrs[bot][1]].append(low)
                else:
                    outs[instrs[bot][1]] = low
                if instrs[bot][2] == "bot":
                    vals[instrs[bot][3]].append(high)
                else:
                    outs[instrs[bot][3]] = high
                vals[bot] = []
        if not (outs["0"] * outs["1"] * outs["2"] == 0):
            outsFound = True

    print "Part One:", bot
    print "Part Two:", outs["0"] * outs["1"] * outs["2"]
