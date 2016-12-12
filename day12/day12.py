# tries to parse a string, uses string as address if it's not a number
def getValue(registers, val):
    try:
        value = int(val)
    except ValueError:
        value = registers[val]
    return value

# set False to run Part Two
partOne = True

registers = {"a": 0, "b": 0, "c": 0, "d": 0}
if not partOne: registers["c"] = 1

pc = 0

# parse input
instrs = []
with open("input.txt", "r") as f:
    instrs = f.read().split("\n")

while not instrs[pc] == "":
    parts = instrs[pc].split(" ")
    if parts[0] == "cpy":
        value = getValue(registers, parts[1])
        registers[parts[2]] = value
        pc += 1
    elif parts[0] == "jnz":
        value = getValue(registers, parts[1])
        if not value == 0:
            pc += int(parts[2])
        else:
            pc += 1
    else:
        registers[parts[1]] += 1 if parts[0] == "inc" else -1
        pc += 1

print "Part " + ("One:" if partOne else "Two:"), registers["a"]
