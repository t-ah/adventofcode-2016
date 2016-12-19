import Queue

no = 3014387 # the input
partOne = False
partTwo = True

if partOne:
    # for part one, we make an accurate simulation of course
    q = Queue.Queue(no)
    for i in range(no):
        q.put((i + 1, 1))

    while q.qsize() > 1:
        print q.qsize()
        receiver = q.get()
        giver = q.get()
        q.put((receiver[0], receiver[1] + giver[1]))

    lastElfStanding = q.get()

    print "Part One:", lastElfStanding[0], "Check:", lastElfStanding[1]

if partTwo:
    # for part two, the q is not the best of ideas..
    # this is also not a good approach but I do not have time to improve it today :<
    presents = []
    for i in range(no):
        presents.append(i + 1)

    while len(presents) > 1:
        print len(presents)
        giver = presents.pop(len(presents) / 2)
        receiver = presents.pop(0)
        presents.append(receiver)

    print "Part Two:", presents[0]
