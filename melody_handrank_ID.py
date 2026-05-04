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

class Hand:
    """Represents a ranked poker hand."""

    def __init__(self, rank):
        self.rank = rank

    # TECHNIQUE 2: magic methods other than __init__()
    def __str__(self):
        return HAND_NAMES[self.rank]

    # __lt__ lets us compare two Hands with < and >
    def __lt__(self, other):
        return self.rank < other.rank


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
        
 # TECHNIQUE 1: max() with a key function
    # Finds the best 5-card combo directly using score_five_cards
    all_cards = player_hand + community_cards
    best_combo = max(combinations(all_cards, 5), key=score_five_cards)
    best_rank = score_five_cards(best_combo)

    # __str__ is called when printing the Hand object
    result = Hand(best_rank)
    print(f"Best hand found: {result}!")
    return result

   
