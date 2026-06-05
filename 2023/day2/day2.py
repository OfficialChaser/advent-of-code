with open('day2.in') as file:
    data = [i for i in file.read().strip().split("\n")]

# ----- PART 1 ----- #
def getGameNum(info):
    gameNum = ""
    gameNumList = []
    for char in gameInfo:
        if char.isnumeric():
            gameNumList.append(char)

    for cNum in gameNumList:
        gameNum += cNum

    gameNum = int(gameNum)
    return gameNum

total1 = 0

for line in data:
    valid = True
    gameInfo, dice = line.split(":")

    gameNum = getGameNum(gameInfo)

    rounds = dice.split(";")

    for round in rounds:
        roundInfo = round.split(",")
        for info in roundInfo:
            amt, color = info.strip().split(" ")
            amt = int(amt)
            if (color == "red" and amt > 12):
                valid = False
            elif (color == "green" and amt > 13):
                valid = False
            elif (color == "blue" and amt > 14):
                valid = False

    if (valid):
        total1 += gameNum


if __name__ == '__main__':
    print(total1)



    

# ----- PART 2 ----- #
total2 = 0

for line in data:
    valid = True
    gameInfo, dice = line.split(":")

    gameNum = getGameNum(gameInfo)

    rounds = dice.split(";")

    minRed = 0
    minGreen = 0
    minBlue = 0
    for round in rounds:
        roundInfo = round.split(",")
        for info in roundInfo:
            amt, color = info.strip().split(" ")
            amt = int(amt)
            if (color == "red" and amt > minRed):
                minRed = amt
            elif (color == "green" and amt > minGreen):
                minGreen = amt
            elif (color == "blue" and amt > minBlue):
                minBlue = amt

    roundMin = (minRed * minGreen * minBlue)
    total2 += roundMin

if __name__ == '__main__':
    print(total2)