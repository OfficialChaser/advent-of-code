high_cards = {"A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10}

def card_to_value(card):
    return high_cards[card] if card in high_cards else int(card)

with open("day7.in", "r") as file:
    data = [i for i in file.readlines()]

hands = []
earnings = 0

for line in data:
    hand, bid = line.split()
    bid = int(bid)

    instances = {}
    for card in hand:
        amount_of_instances = hand.count(card)
        instances[card] = amount_of_instances
    
    max_instances = 0
    max_instance_cards = []
    second_max_instance_card = ""
    for card in instances:
        if instances[card] >= max_instances:
            max_instance_cards.append(card)

            prev_max_instances = max_instances
            max_instances = instances[card]

            if prev_max_instances != max_instances and len(max_instance_cards) > 1:
                max_instance_cards.pop(0)
            
        elif instances[card] == 2:
            second_max_instance_card = instances[card]
                
    max_instance_cards = [card_to_value(i) for i in max_instance_cards]
    # No pairs
    if len(max_instance_cards) == 5:
        hands.append([1.0, max(max_instance_cards), bid])
    
    # Two pair
    elif len(max_instance_cards) == 2:
        hands.append([2.5, max(max_instance_cards), bid])
    
    # Full house
    elif second_max_instance_card != "":
        hands.append([3.5, max_instance_cards[0], bid])

    # 1 pair, 3 of a kind, 4 of a kind, 5 of a kind
    else:
        hands.append([float(max_instances), max(max_instance_cards), bid])

hands.sort()
j = 0
for i in range(len(hands)):
    if i == 0 or hands[i - 1][1] != hands[i][1] or hands[i - 1][0] != hands[i][0]:
        j += 1
    earnings += j * hands[i][2]
    

print(earnings)