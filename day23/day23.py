# tries to parse a string, uses string as address if it's not a number
def getValue(registers, val):
    try:
        value = int(val)
    except ValueError:
        value = registers[val]
    return value

# set False to run Part Two
partOne = True

registers = {"a": 7, "b": 0, "c": 0, "d": 0}
if not partOne:
    registers["a"] = 12

pc = 0

# parse input
instrs = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        instrs.append(line.split(" "))
    instrs.append([""])

while not instrs[pc][0] == "":
    parts = instrs[pc]

    # behold the perfect multiplication detection
    if parts[0] == "cpy":
        if (not partOne) and parts[1] in registers and parts[2] in registers:
            if instrs[pc + 1][0] == "inc":
                if instrs[pc + 2][0] == "dec":
                    if instrs[pc + 3] == ["jnz", instrs[pc + 2][1] , "-2"]:
                        if instrs[pc + 4][0] == "dec":
                            if instrs[pc + 5] == ["jnz", instrs[pc + 4][1], "-5"]:
                                a = instrs[pc + 1][1]
                                b = parts[1]
                                c = parts[2]
                                d = instrs[pc + 4][1]
                                if len(set([a, b, c, d])) == 4:
                                    registers[a] += registers[b] * registers[d]
                                    registers[c] = 0
                                    registers[d] = 0
                                    pc += 6
                                    continue
                                    # end of the perfect multiplication detection
        if parts[2] in registers:
            value = getValue(registers, parts[1])
            registers[parts[2]] = value
        pc += 1
    elif parts[0] == "jnz":
        value = getValue(registers, parts[1])
        if value != 0:
            pc += getValue(registers, parts[2])
        else:
            pc += 1
    elif parts[0] == "inc":
        registers[parts[1]] += 1
        pc += 1
    elif parts[0] == "dec":
        registers[parts[1]] -= 1
        pc += 1
    else: # tgl
        change = pc + registers[parts[1]]
        if change >= 0 and change < len(instrs) - 1:
            instr = instrs[change]
            if len(instr) == 2:
                if instr[0] == "inc":
                    instr[0] = "dec"
                else:
                    instr[0] = "inc"
            else:
                if instr[0] == "jnz":
                    instr[0] = "cpy"
                else:
                    instr[0] = "jnz"
        pc += 1

print "Part " + ("One:" if partOne else "Two:"), registers["a"]
