from string import ascii_letters

with open('day3.in') as file:
    data = [i for i in file.read().strip().split('\n')]


Sum = 0
for line in data:
    half1, half2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    for priority, char in enumerate(ascii_letters):
        if char in half1 and char in half2:
            Sum += priority + 1

j = 3
Sum2 = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3
    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            Sum2 += priority + 1
    
print("Answer to part 1:", Sum)
print("Answer to part 2:", Sum2)