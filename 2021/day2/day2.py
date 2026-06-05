with open("day2.in", "r") as f:
    data = [i for i in f.read().split("\n")]


# PART 1
distance = 0
depth = 0

for line in data:
    direction, mag = line.split(" ")
    mag = int(mag)

    if direction == "forward":
        distance += mag    
    elif direction == "up":
        depth -= mag
    else:
        depth += mag
    
print(distance * depth)

# PART 2
distance = 0
depth = 0
aim = 0

for line in data:
    direction, mag = line.split(" ")
    mag = int(mag)

    if direction == "forward":
        distance += mag
        depth += aim * mag    
    elif direction == "up":
        aim -= mag
    else:
        aim += mag
    
print(distance * depth)