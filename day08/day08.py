#!/usr/bin/env python

lcd = []

width = 50
height = 6

for i in range(height):
    row = []
    for j in range(width):
        row.append(False)
    lcd.append(row)

def printLCD(display):
    for i in range(height):
        row = ""
        for val in lcd[i]:
            if val:
                row += "#"
            else:
                row += "-"
        print row

def countPixels(display):
    count = 0
    for i in range(height):
        count += lcd[i].count(True)
    return count

with open("input.txt", "r") as f:
    for line in f:
        words = line.split(" ")
        if words[0] == "rect":
            dims = words[1].split("x")
            dimX, dimY = int(dims[0]), int(dims[1])
            for i in range(dimY):
                for j in range(dimX):
                    lcd[i][j] = True
        elif words[1] == "row":
            row = int(words[2][2:])
            by = int(words[4][:-1])
            lcd[row] = lcd[row][-by:] + lcd[row][:-by]
        else: #column
            col = int(words[2][2:])
            by = int(words[4][:-1])
            column = [lcd[x][col] for x in range(height)]
            column = column[-by:] + column[:-by]
            for i in range(height):
                lcd[i][col] = column[i]
        printLCD(lcd)

print "Part One:", countPixels(lcd)
print "Alright, nothing (more) to do for Part Two"
