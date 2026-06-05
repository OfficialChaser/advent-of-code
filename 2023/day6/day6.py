import math

def parse_line(data, index, strip_phrase, in_a_list=True):
    char_list = list(filter(None, data[index].lstrip(strip_phrase).strip("\n").split(" ")))

    if in_a_list == True:
        return [int(i) for i in char_list]
    
    return int("".join(char_list))

# PART 1
with open("day6.in", "r") as file:
    data = [line for line in file.readlines()]

time_list = parse_line(data, 0, "Time:")
distance_list = parse_line(data, 1, "Distance:")

ways_to_win = []

for i, time in enumerate(time_list):
    winning_nums = 0
    for x in range(time):
        if (time - x) * x >= distance_list[i]:
            winning_nums += 1
    
    ways_to_win.append(winning_nums)

print(ways_to_win)
print(math.prod(ways_to_win))

# PART 2
time = parse_line(data, 0, "Time:", False)
distance = parse_line(data, 1, "Distance:", False)

ways_to_win2 = 0
for x in range(time):
    if (time - x) * x > distance:
        ways_to_win2 += 1

print(ways_to_win2)