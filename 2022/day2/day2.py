with open('day2.in') as file:
    rounds = [i for i in file.read().strip().split('\n')]
print(rounds)

resultDict = {
    'A X': 4, 'A Y': 8,'A Z': 3, 
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6,
}

resultDict2 = {
    'A X': 3, 'A Y': 4,'A Z': 8, 
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7,
}

count = 0
for round in rounds:
    count += resultDict[round]

count2 = 0
for round in rounds:
    count2 += resultDict2[round]

print('The total score for part 1 would be:', count)
print('The total score for part 2 would be:', count2)