partTwo = True

pInput = "01111010110010011"
length = 272
if partTwo: length = 35651584

l = list(pInput)

while len(l) < length:
    l.append("0")
    end = len(l) - 2
    for i in range(len(l) - 1):
        l.append("0" if l[end - i] == "1" else "1")

def checksum(li, length):
    out = []
    for i in range(length/2):
        if li[2 * i] == li[2 * i + 1]:
            out.append("1")
        else:
            out.append("0")
    return out

out = checksum(l, length)
while len(out) % 2 == 0:
    out = checksum(out, len(out))

print "Part", "Two:" if partTwo else "One:", "".join(out)

# there is definitely some pattern to be found ..
# w 0 w(IR) 0 w 1 w(IR) ,0, w 0 w(IR) 1 w 1 w(IR) ,0, w 0 w' 0 w ...
