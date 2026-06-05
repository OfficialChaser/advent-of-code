with open("day3.in", "r") as f:
    data = [i for i in f.read().split("\n")]

binary_dict = {}

for i in range(len(data[0])):
    binary_dict[i] = 0

for line in data:
    for i in range(len(line)):
        if line[i] == "1":
            binary_dict[i] += 1
        else:
            binary_dict[i] -= 1

gamma = "0"
epsilon = "0"

for key in binary_dict:
    if binary_dict[key] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma_dec = 0
mult = 1
for num in gamma[::-1]:
    gamma_dec += int(num) * mult
    mult *= 2

epsilon_dec = 0
mult = 1
for num in epsilon[::-1]:
    epsilon_dec += int(num) * mult
    mult *= 2

print(gamma_dec * epsilon_dec)