
# Getting Data
with open('day1.in', 'r') as file:
    data = [i for i in file.read().strip().split('\n')]


max = 0
max2 = 0
max3 = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count

total_max = max + max2 + max3

print("Answer to part 1:", max)
print("Answer to part 2:", total_max)
