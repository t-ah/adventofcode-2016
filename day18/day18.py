row = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."
safe = row.count(".")
trap = ["^^.", ".^^", "^..", "..^"]
rows = 40 - 1
partTwo = False

if partTwo:
    rows = 400000 - 1

for _ in range(rows):
    row = "." + row + "." # add walls
    nextRow = ""
    for i in range(len(row) - 2):
        if row[i:i+3] in trap:
            nextRow += "^"
        else:
            nextRow += "."
    row = nextRow
    safe += row.count(".")

print "Part", "Two:" if partTwo else "One:", safe
