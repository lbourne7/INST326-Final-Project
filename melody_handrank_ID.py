#Melody Sims , Hand Ranking 
from itertools import combinations

HAND_NAMES = {
    1: "High Tide",
    2: "Lucky Pair",
    3: "Double Shell",
    4: "Triple Threat",
    5: "On a Roll",
    6: "Red Flush",
    7: "Full library",
    8: "Quad Squad",
    9: "Gold Flush",
    10: "Testudo Flush"
}


def rank_hand(player_hand, community_cards):
    VALUE_MAP = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14
    }

    def score_five_cards(five_cards):
        values = []
        suits = []

        #puting each card into a number and a suit
        for card in five_cards:
            parts = card.lower().split(" of ")
            values.append(VALUE_MAP[parts[0]])
            suits.append(parts[1])

        #checking for flush or straight
        values.sort(reverse=True)
        is_flush = len(set(suits)) == 1
        is_straight = values == list(range(values[0], values[0] - 5, -1))

        # counting any repeated cards 
        counts = {}
        for v in values:
            counts[v] = counts.get(v, 0) + 1
        freq = sorted(counts.values(), reverse=True)

        # returning rank based on cards
        if is_straight and is_flush:
            return 10 if set(values) == {10, 11, 12, 13, 14} else 9
        if freq[0] == 4: return 8
        if freq[0] == 3 and freq[1] == 2: return 7
        if is_flush: return 6
        if is_straight: return 5
        if freq[0] == 3: return 4
        if freq[0] == 2 and freq[1] == 2: return 3
        if freq[0] == 2: return 2
        return 1

    # all possible 5-card combo from all 7 cards and keeping the best ranked 
    #hand to print
    all_cards = player_hand + community_cards
    best_rank = 0
    for combo in combinations(all_cards, 5):
        rank = score_five_cards(combo)
        if rank > best_rank:
            best_rank = rank
    print(f"Best hand found: {HAND_NAMES[best_rank]}!")
    return best_rank



# Test 
player_hand = ["ace of spades", "king of spades"]
community_cards = ["queen of spades", "jack of spades", "10 of spades",
"2 of hearts", "5 of clubs"]
print(rank_hand(player_hand, community_cards))  # Should print 10 (Testudo Flush)
