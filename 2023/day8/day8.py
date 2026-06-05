network = {}

def parse_line(line):
    key, values = line.split(" = ")
    network[key] = [values[1:4], values[6:9]]

with open("day8.in", "r") as f:
    data = [i for i in f.readlines()]

instructions = data[0].strip('\n')

for line in data[2:]:
    parse_line(line)

# PART 1
current_node = "AAA"
steps_taken = 0

while current_node != "ZZZ":
    for instruction in instructions:
        steps_taken += 1

        i = 1
        if instruction == "L":
            i = 0

        current_node = network[current_node][i]
        
        print(f"Instruction: {instruction}, Current Node: {current_node}, Steps Taken: {steps_taken}")

print(steps_taken)

# PART 2 (UNFINISHED)
# def nodes_completed_goal(nodes):
#     for node in nodes:
#         if node[2] != "Z":
#             return False
    
#     return True

# current_nodes = []
# for node in network:
#     if node[2] == "A":
#         current_nodes.append(node)

# print(current_nodes)

# steps_taken2 = 0
# while not nodes_completed_goal(current_nodes):

#     for instruction in instructions:

#         i = 1
#         if instruction == "L":
#             i = 0

#         for j, node in enumerate(current_nodes):
#             current_nodes[j] = network[node][i]
        
#         print(f"Instruction: {instruction}, Current Nodes: {current_nodes}, Steps Taken: {steps_taken2}")
    
#     steps_taken2 += 1