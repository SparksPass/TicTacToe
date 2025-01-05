#DECLARING VARIABLES
aValid = [11, 12, 13, 21, 22, 23, 31, 32, 33]
aTic = []
aToe = []
aTrack = []
vTic = 0
vToe = 0

#DISPLAY
def display():
    for x in range(1, 4):
        for y in range(1, 4):
            if int(str(x) + str(y)) in aTic:
                print ("X", end = "")
            elif int(str(x) + str(y)) in aToe:
                print ("0", end = "")
            else:
                print ("#", end = "")
        print(end="\n")

#CHECK IF X OR O HAS WON
def check(z):
    global aTrack
    if z == "x":
        for i in range(len(aTic)):
            aTrack.append(str(aTic[i - 1])[0])

        for u in range(len(aTic)):
            if aTrack.count(aTrack[u - 1]) == 3:
                return "X"
        aTrack = []
        for i in range(len(aTic)):
            aTrack.append(str(aTic[i - 1])[1])

        for u in range(len(aTic)):
            if aTrack.count(aTrack[u - 1]) == 3:
                return "X"
        aTrack = []
        if 11 in aTic and 22 in aTic and 33 in aTic or 31 in aTic and 22 in aTic and 13 in aTic:
            return "X"
    elif z == "o":
        for i in range(len(aToe)):
            aTrack.append(str(aToe[i - 1])[0])

        for u in range(len(aToe)):
            if aTrack.count(aTrack[u - 1]) == 3:
                return "O"
        aTrack = []
        for i in range(len(aToe)):
            aTrack.append(str(aToe[i - 1])[1])

        for u in range(len(aToe)):
            if aTrack.count(aTrack[u - 1]) == 3:
                return "O"
        aTrack = []
        if 11 in aToe and 22 in aToe and 33 in aToe or 31 in aToe and 22 in aToe and 13 in aToe:
            return "O"

display()
#GAME LOOP
while True:
    #GET X POSITION
    while not vTic in aValid or vTic in aTic or vTic in aToe:
        vTic = int(input("Enter X position : "))
        if not vTic in aValid or vTic in aTic or vTic in aToe:
            print ("error, position unavailable.")
    aTic.append(vTic)
    if check("x") == "X":
        print ("X WIN")
        display()
        break
    vTic = 0
    display()

    #GET O POSITION
    while not vToe in aValid or vToe in aTic or vToe in aToe:
        vToe = int(input("Enter O position : "))
        if not vToe in aValid or vToe in aTic or vToe in aToe:
            print ("error, position unavailable.")
    aToe.append(vToe)
    if check("o") == "O":
        print ("O WIN")
        display()
        break
    vToe = 0
    display()