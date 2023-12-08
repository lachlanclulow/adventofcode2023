example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

ranks = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13,
}

hand_ranks = {
    "FIVE": 7,
    "FOUR": 6,
    "FULL": 5,
    "THREE": 4,
    "TWO": 3,
    "ONE": 2,
    "HIGH": 1,
}


hands = []



def compare_hands(hand):
    hand_rank = None
    jokers = 0
    counts = {}
    for card in hand:
        if card == "J":
            jokers += 1
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    
    for key, val in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        if val == 5:
            hand_rank = hand_ranks["FIVE"]
        elif val == 4:
            hand_rank = hand_ranks["FOUR"]
        elif val == 3:
            if hand_rank == hand_ranks["ONE"]:
                hand_rank = hand_ranks["FULL"]
            else:
                hand_rank = hand_ranks["THREE"]
        elif val == 2:
            if hand_rank == hand_ranks["THREE"]:
                hand_rank = hand_ranks["FULL"]
            elif hand_rank == hand_ranks["ONE"]:
                hand_rank = hand_ranks["TWO"]
            else:
                hand_rank = hand_ranks["ONE"]
        elif val == 1:
            if not hand_rank:
                hand_rank = hand_ranks["HIGH"]

    if hand_rank == hand_ranks["FOUR"] and jokers >= 1:
            hand_rank = hand_ranks["FIVE"]
    elif hand_rank == hand_ranks["FULL"] and jokers >= 2:
        hand_rank = hand_ranks["FIVE"]
    elif hand_rank == hand_ranks["THREE"]:
        if jokers == 1 or jokers == 3:
            hand_rank = hand_ranks["FOUR"]
    elif hand_rank == hand_ranks["TWO"]:
        if jokers == 1:
            hand_rank = hand_ranks["FULL"]
        if jokers == 2:
            hand_rank = hand_ranks["FOUR"]
    elif hand_rank == hand_ranks["ONE"]:
        if jokers == 1:
            hand_rank = hand_ranks["THREE"]
        elif jokers == 2:
            hand_rank = hand_ranks["THREE"]
    elif hand_rank == hand_ranks["HIGH"]:
        if jokers == 1:
            hand_rank = hand_ranks["ONE"]
            
    return tuple([hand_rank] + [ranks[x] for x in hand])
    
for line in example.splitlines():
    hands.append(tuple(line.split()))

total = 0

for i, hand in enumerate(sorted(hands, key=lambda x: compare_hands(x[0]))):
    total += (i+1)*int(hand[1])

print(total)