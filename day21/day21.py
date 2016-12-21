from itertools import permutations

def rotateBased(word, letter):
    index = word.index(letter)
    if index >= 4:
        index += 1
    index += 1
    index = len(word) - index # make it a left rotation
    index = index % len(word)
    return word[index:] + word[:index]

def rotateLeft(word, times):
    return word[times:] + word[:times]

def move(word, x, y):
    letter = word[x]
    word = word[:x] + word[x + 1:]
    stop = y

    return word[:stop] + [letter] + word[stop:]

def reverse(word, x, y):
    rev = word[x:y+1]
    rev.reverse()
    return word[:x] + rev + word[y+1:]

def scramble(word, instructions):
    for parts in instructions:
        if parts[0] == "swap":
            if parts[1] == "position":
                x, y = int(parts[2]), int(parts[5])
                t = word[x]
                word[x], word[y] = word[y], t
            else:
                x, y = parts[2], parts[5]
                for i in range(len(word)):
                    if word[i] == x:
                        word[i] = y
                    elif word[i] == y:
                        word[i] = x
        elif parts[0] == "rotate":
            if parts[1] == "based":
                word = rotateBased(word, parts[6])
            else:
                direction = parts[1]
                times = int(parts[2])
                if direction == "right":
                    times = len(word) - times # only use left rotation
                times = times % len(word) # for safety
                word = rotateLeft(word, times)
        elif parts[0] == "move":
            x, y = int(parts[2]), int(parts[5])
            word = move(word, x, y)
        elif parts[0] == "reverse":
            x, y = int(parts[2]), int(parts[4])
            word = reverse(word, x, y)
    return word

word = list("abcdefgh")
instructions = []

with open("input.txt", "r") as f:
    for line in f:
        instructions.append(line.replace("\n", "").split(" "))

print "Part 1:", "".join(scramble(word, instructions))

# that is not so many possibilities, check all of them ... rotateBased also does not seem to be reversible
inputPartTwo = "fbgdceah"
for p in permutations(word):
    if "".join(scramble(list(p), instructions)) == inputPartTwo:
        print "Part 2:", "".join(p)
        break
