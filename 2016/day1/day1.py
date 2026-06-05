with open('day1.in',  'r') as file:
    directions =  [i for i in file.read().strip().split(', ')]

# directons: N:1, E:2, S:3, W:4
orientation = 1
x = 0
y = 0
locations = []
duplicate_location = []

def bound_orientation(a: int):
    if a > 4:
        a = 1
    if a < 1:
        a = 4
    return a

def existing_location(location):
    return location in locations

for direction in directions:
    if  'L' in direction:
        orientation -= 1
    elif  'R' in direction:
        orientation += 1

    orientation  = bound_orientation(orientation)
    steps = int(direction[1:])

    if orientation % 2 == 0:
        old_x = x
        x += (orientation - 3) * steps

        if duplicate_location:
            continue

        min_x = min(old_x, x)
        max_x = max(old_x, x)
        for i in range(min_x, max_x):
            location = [i,y]
            if existing_location(location):
                duplicate_location = location
            else:
                locations.append([i, y])
    else:
        old_y = y
        y += (orientation - 2) * steps

        if duplicate_location:
            continue

        min_y = min(old_y, y)
        max_y = max(old_y, y)
        for i in range(min_y, max_y):
            location = [x,i]
            if existing_location(location):
                duplicate_location = location
            else:
                locations.append([x, i])

print(f"Part 1: {abs(x) + abs(y)}")
print(f"Part 2: {abs(duplicate_location[0]) + abs(duplicate_location[1])}")
