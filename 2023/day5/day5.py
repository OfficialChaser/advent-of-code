def parse_sections(data):
    sections = []
    current_section = []

    for line in data[3:]:
        if line == "":
            sections.append(current_section)
            current_section = []
        elif ":" not in line:
            current_section.append([int(i) for i in line.split()])
    
    if current_section:
        sections.append(current_section)
    
    return sections

# Part 1
with open("day5.in", "r") as f:
    data = [line.strip() for line in f.readlines()]

seed_list = [int(i) for i in data[0].lstrip("seeds: ").split()]
sections = parse_sections(data)

locations = []

for seed in seed_list:
    value = seed

    for section in sections:
        for dest_range, src_range, range_len in section:

            if src_range <= value < src_range + range_len:
                value = dest_range + (value - src_range)
                break  
    
    locations.append(value)

print(min(locations))

# Part 2 (UNFINISHED)
# temp_seed_list = [int(i) for i in data[0].lstrip("seeds: ").split()]
# sections = parse_sections(data)

# max_value = 0
# /*for group in sections[0]:
#     if group[1] + group[2] > max_value:
#         max_value = group[1] + group[2]

# seed_list = []
# for i, seed in enumerate(temp_seed_list[::2]):
#     for j in range(temp_seed_list[i + 1]):
#         if seed + j > max_value:
#             break
#         seed_list.append(seed + j)

# locations = []

# for seed in seed_list:
#     value = seed

#     for section in sections:
#         for dest_range, src_range, range_len in section:

#             if src_range <= value < src_range + range_len:
#                 value = dest_range + (value - src_range)
#                 break  
    
#     locations.append(value)

# print(min(locations))