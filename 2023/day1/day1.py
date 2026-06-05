with open('day1.in', 'r') as file:
    data = [i for i in file.read().strip().split('\n')]

# ----- PART 1 ----- #
total1 = 0
total2 = 0
for line in data:
    lineTotal = 0
    for char in line:
        if char.isnumeric():
            lineTotal += (int(char) * 10)
            break
    for char in line[::-1]:
        if char.isnumeric():
            lineTotal += int(char)
            break

    total1 += lineTotal

if __name__ == '__main__':  
    print(total1)

# ----- PART 2 ----- #
with open('Day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

total2 = 0

def replaceWords(line):
    line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three")
    line = line.replace("four", "four4four").replace("five", "five5five").replace("six", "six6six")
    line = line.replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    return line

for line in data:
    line = replaceWords(line)

    numList = []
    for char in line:
        if char.isnumeric():
            numList.append(char)

    firstNum = int(numList[0])
    lastNum = int(numList[-1])

    lineTotal = (firstNum * 10 + lastNum)

    total2 += lineTotal
    print(lineTotal)

print(total2)