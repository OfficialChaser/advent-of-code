with open('day4.in') as file:
    data = [i for i in file.read().strip().split("\n")]


# PART 1
sum = 0
for line in data:
    w_nums_str, p_nums_str = line.lstrip(":").split("|")
    _, w_nums_str = w_nums_str.split(":")

    player_nums = [int(i) for i in list(filter(None, p_nums_str.split(" ")))]
    winning_nums = [int(i) for i in list(filter(None, w_nums_str.split(" ")))]

    line_total = 0
    for num in player_nums:
        if num in winning_nums:
            winning_nums.remove(num)

            if line_total == 0:
                line_total = 1
            else:
                line_total *= 2

    sum += line_total
    
print(sum)

# PART 2
total_cards = len(data)
card_copies = {}

for i in range(1, len(data) + 1):
    card_copies[i] = 1

i = 0
for line in data:
    w_nums_str, p_nums_str = line.lstrip(":").split("|")
    card_num_str, w_nums_str = w_nums_str.split(":")
    

    player_nums = [int(i) for i in list(filter(None, p_nums_str.split(" ")))]
    winning_nums = [int(i) for i in list(filter(None, w_nums_str.split(" ")))]

    card_num = ""
    for char in card_num_str:
        if char.isnumeric():
            card_num += char
    card_num = int(card_num)

    winners = 0

    for num in player_nums:
        if num in winning_nums:
            winners += 1

    
    for i in range(0, winners):
        card_copies[card_num + i + 1] += card_copies[card_num]
        total_cards += card_copies[card_num]

    if (card_num != 220):
        print(f"Card Num: {card_num}. Winners: {winners}. Copies of Next: {card_copies[card_num + 1]}")

    

print(total_cards)    
