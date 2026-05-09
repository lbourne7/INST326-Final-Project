# Melody Sims - Hand Ranking
from itertools import combinations
import random

from game_data import (
    HAND_NAMES,
    VALUE_MAP,
    SUITS,
    VALUES,
    BET_LIMITS,
    BET_MULTIPLIERS
)

class Player:
    """
    Represents a player in the game.

    Attributes:
        name: The player's name.
        hand: The cards currently held by the player.
        current_bet: The amount the player has bet.
        folded: True if the player has folded and is out of the round.
        status: The player's current status.
    """

    def __init__(self, name):
        """
        Initializes a Player with a name and default game state.

        Args:
            name: The player's name.

        Side Effects:
            Sets self.name to the given name.
            Sets self.hand to an empty list.
            Sets self.current_bet to 0.
            Sets self.folded to False.
            Sets self.status to "Standard".
        """

        self.name = name
        self.hand = []
        self.current_bet = 0
        self.folded = False
        self.status = "Standard"


class Hand:
    """
    Represents a ranked poker hand with a numeric rank and name.

    Attributes:
        rank (int): The numeric rank of the hand (1-10).

    Side Effects:
        Sets self.rank to the given rank value.
    """

    def __init__(self, rank):
        """
        Initializes a Hand with a rank.

        Args:
            rank (int): The numeric rank of the hand (1-10).
        """

        self.rank = rank

    def __str__(self):
        """
        Returns the display name of the hand.

        Returns:
            str: The name of the hand.
        """

        return HAND_NAMES[self.rank]

    def __lt__(self, other):
        """
        Compares this hand to another hand by rank.

        Args:
            other: The other Hand to compare.

        Returns:
            bool: True if this hand's rank is lower.
        """

        return self.rank < other.rank

    def __gt__(self, other):

        return self.rank > other.rank

    def __eq__(self, other):
        """
        Checks if this hand is equal in rank to another.

        Args:
            other: The other Hand to compare.

        Returns:
            bool: True if both hands have the same rank.
        """

        return self.rank == other.rank


def rank_hand(player_hand, community_cards):
    """
    Determines the best possible poker hand from a player's cards
    and the community cards.

    Evaluates all possible 5-card combinations, scores each one,
    and returns the highest-ranking combination found.

    Args:
        player_hand: A list of cards held by the player.
        community_cards: A list of shared community cards.

    Returns:
        Hand: A Hand object representing the best combination.

    Side Effects:
        Prints the best hand found.
    """

    def score_five_cards(five_cards):
        """
        Scores a specific 5-card hand.

        Args:
            five_cards: A tuple of exactly 5 cards.

        Returns:
            int: Rank from 1-10.
        """

        values = []
        suits = []

        # putting each card into a number and suit
        for card in five_cards:

            value, suit = card.lower().split(" of ")

            values.append(VALUE_MAP[value])
            suits.append(suit)

        # checking for flush or straight
        values.sort(reverse=True)

        is_flush = len(set(suits)) == 1

        is_straight = values == list(
            range(values[0], values[0] - 5, -1)
        )

        # counting repeated cards
        counts = {}

        for value in values:
            counts[value] = counts.get(value, 0) + 1

        freq = sorted(counts.values(), reverse=True)

        # returning rank based on cards
        if is_straight and is_flush:
            return 10 if set(values) == {10, 11, 12, 13, 14} else 9

        if freq[0] == 4:
            return 8

        if freq[0] == 3 and freq[1] == 2:
            return 7

        if is_flush:
            return 6

        if is_straight:
            return 5

        if freq[0] == 3:
            return 4

        if freq[0] == 2 and freq[1] == 2:
            return 3

        if freq[0] == 2:
            return 2

        return 1

    # all possible 5-card combinations from all 7 cards
    all_cards = player_hand + community_cards

    best_combo = max(
        combinations(all_cards, 5),
        key=lambda combo: score_five_cards(combo)
    )

    best_rank = score_five_cards(best_combo)

    result = Hand(best_rank)

    print(f"Best hand found: {result}!")

    return result


# end of Melody Sims's section


def take_players_bets(players):
    """
    Author: Laurencia Aparin

    Takes the players' bets and stores them for active players
    in the current round.

    Args:
        players (list):
            A list of Player objects. Each object has to have
            'folded', 'name', and 'current_bet' attributes.
    Returns:
        int:
            Total sum of bets collected during the round.

    Side Effects:
        Changes the current_bet attribute of players.
        Prints error messages for invalid input.
        Waits for user input.


    Raises:
        ValueError: If a non-numeric string is entered by the user (this 
        is caught and makes the user enter a correct input)
    """

    total_players = 0

    print("Betting round")

    for player in players:

        if player.folded:
            continue

        while True:

            try:
                bet = int(
                    input(f"{player.name}, enter your bet: ")
                )

                player.current_bet = bet

                total_players += bet

                break

            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a number for your bet."
                )

    return total_players


def determine_winners(players, community_cards):
    """
    Author: Laurencia Aparin

    Evaluates each player's hand and determines
    the winner or winners.

    Techniques Used:
        Sequence Unpacking
        Conditional Expressions

    Args:
        players (list):
            List of Player objects. The players have the attributes
            of the name(str) as a string for each player and hand(list) as a list
            folded (bool) if player is playing or not

        community_cards (list):
            Shared community cards.

    Returns:
        tuple:
            winners_names (str):
                Names of winners.

            highest_score (Hand):
                Highest ranked hand.

    Side Effects:
        Prints community cards, player hands,
        and ranking information.

    Raises:
        if player object is missing attributes   
    """

    highest_score = None

    winners_inalist = []

    print("Final Hand Ranking")

    print(
        f"Community Cards: "
        f"{', '.join(community_cards)}"
    )

    for player in players:

        if player.folded:
            continue

        # sequence unpacking
        name, hand = player.name, player.hand

        score = rank_hand(hand, community_cards)

        rank_name = str(score)

        print(f"{name} had: {' '.join(hand)}")

        print(f"Result: {rank_name}")

        # conditional expression
        winners_inalist = (
            [name]
            if highest_score is None or score > highest_score
            else winners_inalist + [name]
            if score == highest_score
            else winners_inalist
        )

        if highest_score is None or score > highest_score:
            highest_score = score

    winners_names = " and ".join(winners_inalist)

    return winners_names, highest_score


def create_deck():
    """
    Creates a standard 52-card deck.
    
    Primary author: Jonathan Sanchez
    Techniques: Use of F-strings containing expressions

    Returns:
        list[str]: List of card strings.
    """

    deck = []

    for suit in SUITS:
        for value in VALUES:
            deck.append(f"{value} of {suit}")

        
    return deck


def shuffle_and_deal(
    num_players,
    deck,
    comm_count,
    cards_per_player=2
):
    """
    Shuffles and deals cards.
    
    Primary author: Jonathan Sanchez
    Techniques: Set operations using difference

    Args:
        num_players (int): Number of players.
        deck (list[str]): Deck of cards.
        comm_count (int): Number of community cards.
        cards_per_player (int): Cards per player.

    Returns:
        tuple:
            player_hand (list[list[str]])
            comm_cards (list[str])

    Side Effects:
        Shuffles and removes cards from deck.
    """

    random.shuffle(deck)
    
    original_deck = set(deck)

    player_hand = []

    for _ in range(num_players):

        hand = []

        for _ in range(cards_per_player):
            hand.append(deck.pop())

        player_hand.append(hand)

    comm_cards = []

    for _ in range(comm_count):
        comm_cards.append(deck.pop())
        
    # Use of set operations using difference
    dealt_cards = original_deck.difference(set(deck))
    
    print(f"Cards dealt this round: {len(dealt_cards)} ")

    return player_hand, comm_cards


def build_round_data(players, community_cards):
    """
    Structures round data for scoring.

    Primary Author: Leonard Bourne
    Techniques: List Comprehensions and Dictionary Comprehensions

    Args:
        players (list[Player]): List of players.
        community_cards (list[str]): Shared cards.

    Returns:
        tuple:
            player_names
            bets
            hand_ranks

    Side Effects:
        Calls rank_hand().
    """
    # List Comprehension
    active_players = [
        player for player in players
        if not player.folded
    ]

    player_names = [
        player.name for player in active_players
    ]
    # Dictionary Comprehension
    bets = {
        player.name: player.current_bet
        for player in active_players
    }

    hand_ranks = {
        player.name: rank_hand(
            player.hand,
            community_cards
        )
        for player in active_players
    }

    return player_names, bets, hand_ranks


def update_player_points(player_points, bets, hand_ranks):
    """
    Updates player point totals.

    Primary Author: Leonard Bourne

    Args:
        player_points (dict): Player total scores.
        bets (dict): Player bets.
        hand_ranks (dict): Player hand ranks.

    Returns:
        dict: Round point gains.

    Side Effects:
        Modifies player_points dictionary.

    Raises:
        ValueError: Invalid bet amount.
    """

    bet_multipliers = BET_MULTIPLIERS

    round_summary = {}

    for player in bets:

        bet = bets[player]
        rank = hand_ranks[player]

        if bet not in bet_multipliers:
            raise ValueError(
                f"Bet needs to be between 1-3. "
                f"{bet} for {player}"
            )

        raw_score = (
            rank.rank * bet_multipliers[bet]
        )

        risk_penalty = bet

        net_gain = raw_score - risk_penalty

        player_points[player] += net_gain

        round_summary[player] = net_gain

    return round_summary


def player_decision(player):
    """
    Allows player to fold or continue.

    Primary Author: Leonard Bourne

    Args:
        player (Player): Player object.

    Returns:
        str: Player decision.

    Side Effects:
        Reads console input.
    """

    while True:

        choice = input(
            f"{player.name} --- fold or play? --- "
        ).lower()

        if choice in ["fold", "play"]:
            return choice

        print("Invalid input.")


def display_private_hands(players, pause=True):
    """
    Displays each player's hand privately.

    Primary Author: Leonard Bourne
    Techniques: optional parameter and/or keyword arguments

    Args:
        players (list[Player]): List of players.

    Side Effects:
        Prints to console.
        Waits for input().
    """

    for player in players:

        print(f"\n{player.name}, it's your turn.")
        
        if pause:
            input("Press Enter when you are ready to view hand\n")
            
        print(f"Your hand: {', '.join(player.hand)}")
        
        if pause:
            input("Press Enter when you are finished, check behind you.")


def reveal_all_hands(players):
    """
    Reveals all player hands.

    Primary Author: Leonard Bourne

    Args:
        players (list[Player]): List of players.

    Side Effects:
        Prints all hands to console.
    """

    print("\n-- Final Hands --")

    for player in players:
        print(f"{player.name}: {', '.join(player.hand)}")


def play_game():
    """
    Controls the overall game flow.

    Primary Author: Leonard Bourne

    Side Effects:
        Reads user input.
        Prints game information.
        Updates player objects.
    """

    while True:

        try:
            num_players = int(
                input("How many players? ")
            )

            if num_players > 0:
                break

            print("At least 1 player required.")

        except ValueError:
            print("Enter valid number.")

    players = []

    for i in range(num_players):

        name = input(
            f"Enter name for player {i + 1}: "
        )

        players.append(Player(name))

    player_points = {
        player.name: 0
        for player in players
    }

    while True:

        print("\nNew Round")

        for player in players:
            player.folded = False
            player.current_bet = 0

        deck = create_deck()

        player_hands, community_cards = (
            shuffle_and_deal(
                len(players),
                deck,
                5
            )
        )

        for i, player in enumerate(players):
            player.hand = player_hands[i]

        print("\n-- Private Hands --")

        display_private_hands(players)

        for player in players:

            if player_decision(player) == "fold":
                player.folded = True

        flop = community_cards[:3]

        print("\nFLOP:", ", ".join(flop))

        take_players_bets(players)

        turn = community_cards[:4]

        print("\nTURN:", ", ".join(turn))

        take_players_bets(players)

        river = community_cards

        print("\nRIVER:", ", ".join(river))

        take_players_bets(players)

        winners, top_score = determine_winners(
            players,
            river
        )

        reveal_all_hands(players)

        names, bets, ranks = build_round_data(
            players,
            river
        )

        summary = update_player_points(
            player_points,
            bets,
            ranks
        )

        print("\nWinner:", winners)
        print("Round results:", summary)
        print("Total points:", player_points)

        again = input(
            "\nWanna go again? (yes/no): "
        ).lower()

        if again not in ["yes", "y"]:

            print("\nFinal Scores:", player_points)

            break


if __name__ == "__main__":
    play_game()
