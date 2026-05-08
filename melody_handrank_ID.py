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
    """
    Represents a ranked poker hand with a numeric rank and name.

    Attributes:
        rank (int): The numeric rank of the hand (1-10)
    """

    def __init__(self, rank):
        """
        Initializes a Hand with a rank.
        Args:
            rank: The numeric rank of the hand (1-10).
        """
        self.rank = rank

    # TECHNIQUE 2: magic methods other than __init__()
    def __str__(self):
        """
        Returns the display name of the hand
        Returns:
            str: The name of the hand 
        """
        return HAND_NAMES[self.rank]

    def __lt__(self, other):
        """
        Compares this hand to another hand by rank
        Args:
            other: The other Hand to compare .
        Returns:
            bool: True if this hand's rank is lower than the other hand's rank.
        """
        return self.rank < other.rank


def rank_hand(player_hand, community_cards):
    """
     Determines the best possible poker hand from a player's cards and the community cards.
    Evaluates all possible 5-card combinations, scores each one, and returns a Hand 
    representing the highest-ranking combination found.

    Args:
        player_hand: A list of cards held by the player                      
        community_cards: A list of shared community card strings in game
                                   
    Returns:
        Hand: A Hand object representing the best 5-card combination found,
    """
    VALUE_MAP = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14
    }

    def score_five_cards(five_cards):
        """
        Scores a specific 5-card hand and returns its rank.

        Args:
            five_cards: A tuple of exactly 5 card strings,
        Returns:
            int: A rank from 1 to 10 representing the strength of the hand:
        """
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

   
