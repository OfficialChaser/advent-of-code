with open('day4.in') as file:
    data = [i for i in file.read().strip().split('\n')]

pairs = 0

for entry in data:
    first, last = entry.split(",")

    first = [int(i) for i in first.split('-')]
    last = [int(i) for i in last.split('-')]
    
    if first[0] <= last[0] and first[1] >= last[1]:
        pairs += 1
    elif last[0] <= first[0] and last[1] >= first[1]:
        pairs += 1


overlaps = 0
for entry in data:
    first, second = entry.split(",")
    
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        overlaps += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        overlaps += 1

print(f'There are {pairs} pairs. (Part 1)')
print(f'There are {overlaps} overlaps. (Part 2)')