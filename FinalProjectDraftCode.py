#Melody Sims , Hand Ranking 
from itertools import combinations
import random

from game_data import (HAND_NAMES, VALUE_MAP, SUITS, VALUES, BET_LIMITS, 
                       BET_MULTIPLIERS)

class Player:
 """
    Represents a player in the game.

    Attributes:
        name: The player's name.
        hand: The cards currently held by the player.
        current_bet: The amount the player has bet.
        folded: True if the player has folded and is out of the round.
        status: The player's current status .
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
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __eq__(self, other):
      """
        Checks if this hand is equal in rank to another
        
        Args: 
        other: The other Hand to compare.

        Returns:
            bool: True if both hands have the same rank.
        """
        return self.rank == other.rank



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
        
     Side Effects:
        Prints the best hand found
    """

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
            value, suit = card.lower().split(" of ")
            values.append(VALUE_MAP[value])
            suits.append(suit)

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
    best_combo = max(combinations(all_cards, 5), 
                     key=lambda c: score_five_cards(c))
    best_rank = score_five_cards(best_combo)
    result = Hand(best_rank)
    print(f"Best hand found: {result}!")
    return result

#end of Melody Sims's section


from random import choice
def take_players_bets(players):
    """"
    Author: Laurencia Aparin
    
    Take the players bets and keeps them for active player of the round. 
    
    Atributes:
        in the players 
        name(str): the name of that player in a string 
        folded(bool): if true then they dont contine if false then they do contintue
        playing in the round. Determining if player is playing in current round 
        or not.
        current_bet(int): The amount that the player has in the round.
    Args:
        players(list): A list of player object 
        
    returns:
       int: The total sum of the bets collected during the round 
       
     Side effects:
         Changes the current_bet attribute to the player object of each of them
         in the list. 
         Prints the error message if invalid and the enter the bet when being ran 
         Waits until the user input is given to continue 
    """
    total_players = 0
    print("Betting round")
    
    for player in players: 
        if player.folded:
            continue 
        while True: 
            try:
                bet = int(input(f" {player.name}, enter your bet ")) 
                player.current_bet = bet 
                total_players += bet
                break 
            except ValueError:
                print("Invalid input. Please enter a number for your bet.")
    return total_players 


def determine_winners(players, community_cards):
    
    """"
     Author: Laurencia Aparin
     
     Evaluates each players hand and prints the results and shows who the winner
     or winners are.
     
     Techniques used sequence unpacking and condtional expression
     
     Attributes: 
            player.name: used to see players name and idetify them from others 
            and return a string
            player.hand: Used for caculating the hand rank
            player.folded: used to see if they player skips or not(means that they 
            would be playing instead)
     Args:
         players(list): List of player objects and the players have the attrbuties
         of the name(str) as a string and hand(list) as a list
         the community cards is a list that is being used to show the shared/
         common cards
        
     Returns:
         A tuple that conatins the winners_names and high_score where the 
         winners_name(str) is a string of naes and the highest_score is the 
         winner of the rank value.
         
     Side Effects:
        It prints out the community cards and the players hand as they are playing
        and the rank 
    """
    
    highest_score = None
    winners_inalist = []
    
    
    print("Final Hand Ranking ")
    print(f"Community Cards: {', ' .join(community_cards)}")
  
    for player in players: 
        if player.folded:
            continue
      
      
        name, hand  = player.name, player.hand 
        score = rank_hand(hand, community_cards)

        rank_name = str(score)
       
      
        print(f"{name} had: {' '.join(hand)}")
        print(f"Result: {rank_name}")
       
        winners_inalist = ([name] if highest_score is None or score > highest_score
        else winners_inalist + [name] if score == highest_score
        else winners_inalist)

        
        if highest_score is None or score > highest_score:
           highest_score = score 
        
    winners_names = " and ".join(winners_inalist)       
            
    return winners_names, highest_score
 



def create_deck():
    """
    Creates a 52-card deck.
    
    Returns:
        list[str]: A list of card strings for example "Ace of Spades"
    """

    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append(f"{value} of {suit}")
            
    return deck

def shuffle_and_deal(num_players, deck, comm_count, cards_per_player = 2):
    """Shuffling a deck and dealing cards to players and the community 

        Args: 
            num_players(int): How many players will be playing 
            deck(list[str]): List of card strings represnting the deck
            comm_count(int): Number of community cards we have to deal
            cards_per_player(int): Number of cards dealt to each players 
            
        Returns:
            tuple(s): The tuple will contain a list of players hands and a list
            of community cards
            
        Raises: 
            ValueError: If the input are invalid or there are not enough cards
    """
    random.shuffle(deck)
    
    player_hand = []
    for _ in range(num_players):
        hand = []
        for _ in range(cards_per_player):
            hand.append(deck.pop())
        player_hand.append(hand)
    
    
    comm_cards = []
    for _ in range(comm_count):
        comm_cards.append(deck.pop())
        
    return player_hand, comm_cards
        


def build_round_data(players, community_cards): 
    """ 
    This function structures the data for scoring from raw player objects.
    
    Primary author: Leonard Bourne
    Techniques:  
    
    
    Args:
        players (list of dict): Each player has 'name', 'hand', 'current_bet'
        community_cards (list of dict): Shared cards
        
    Returns: 
        tuple: 
            player_names (list of strings)
            bets (dict[str, int])
            hand_ranks (dict[str, int])
    
    Side Effects: 
        This function calls rank_hand() for the active players.
    """
    
    active_players = [player for player in players if not player.folded]
   
    player_names = [player.name for player in active_players]
   
    bets = {
       player.name: player.current_bet
       for player in active_players
   }
   
    hand_ranks = {
       player.name: rank_hand(player.hand, community_cards)
       for player in active_players
   }
    
    return player_names, bets, hand_ranks



def update_player_points(player_points, bets, hand_ranks):
    """
    This function calculates and updates the player points according to
        the betting strategy and the hand strength
        
    Round score is calculated by:
    - Starting hand rank (1-10)
    - Application of a multiplier based on the players bet
    - Subtraction of the bet cost as a risk factor
    
    Args: 
    
        players: representative of a list of strings, are the names of each player
            partaking in the current round
      
        player_points: is a dictionary that tracks the current points associated 
            with each player. For example, {"Alex": 5, "Jordan": 7}
        
        bets: is a dictionary that stores the amount that each player bets within
            the round between the values 1 through 3. For example, 
                {"Alex": 2, Jordan": 3}
            
        hand_ranks: is a dictionary that maps each of the players to their 
            hand rank. For example, {"Alex": 3, "Jordan": 7} 
       
    Returns: 
       
       a dictionary that shows how many points each player gain within
        the round.
        
    Side Effects:
        Updates each player total points in the dictionary.
        
    Raises:
        ValueError: In the event a player is not in the dictionary or if a bet 
            is somehow outside the numbers 1-3.
            
    """
    
    bet_multipliers = BET_MULTIPLIERS
    
    round_summary = {}
    
    for player in bets: 
        
        bet = bets[player]
        rank = hand_ranks[player]
        
        if bet not in bet_multipliers:
            raise ValueError(f"Bet needs to be between 1-3. {bet} for {player}")
        
        raw_score = rank.rank * bet_multipliers[bet]
        
        risk_penalty = bet
        
        net_gain = raw_score - risk_penalty
        
        player_points[player] += net_gain
        
        round_summary[player] = net_gain
        
    return round_summary

def player_decision(player):
    """
    This function allows to the player to either fold or continue with the game
    
    Primary Author: Leonard Bourne
    
    Side Effects:
        This will read the users input from the console
    """
    while True:
        choice = input(f"{player.name} --- fold or play?---").lower()
        if choice in ["fold", "play"]:
            return choice
        print("Invalid input. Type in 'fold' or 'play'")

def display_private_hands(players):
    """Each player can only view there own hand
    
    Primary author: Leonard Bourne
    
    Side Effects:
        Will Print the players hands into the console
        Will pauses the programs execution with input()
    
    """
    for player in players:
        print(f"\n{player.name}, Careful... it's your turn.")
        input("Press Enter when ready to view your hand")
        
        print(f"Your hand: {', '.join(player.hand)}")
        
        input("Press Enter when you are done(protect yourself. Or else...)")
        
        
def reveal_all_hands(players):
    """Reveal all hands at the end
    
    Primary author: Leonard Bourne
    
    Side Effects:
        This will print all of the players hands into the console
    """
    print("\n--Final Hands--")
    for player in players:
        print(f"{player.name}: {', '.join(player.hand)}")

def play_game():
    """This function establishes control for multiple rounds of the game
    
    Primary author: Leonard Bourne
    Techniques:
    """
    
    while True:
        try:
            num_players = int(input("How many players?"))
            if num_players > 0:
                break
            print("At least 1 player required.")
        except ValueError:
            print("Enter vaild number.")
        
        
    players = []
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        players.append(Player(name))
    


        
    player_points = {player.name: 0 for player in players}
    
    while True:
        print("\nNew Round")
        
        for player in players:
            player.folded = False
            player.current_bet = 0
        
        deck = create_deck()
        
        player_hands, community_cards = shuffle_and_deal(
           len(players), deck, 5
        )
        
        for i, player in enumerate(players):
            player.hand = player_hands[i]
            
        print("\n--Private Hand--")
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
        
        winners, top_score = determine_winners(players, river)
        reveal_all_hands(players)
        
        names, bets, ranks = build_round_data(players, river)
        summary = update_player_points(player_points, bets, ranks)
        
        print("\nWinner:", ", ".join(winners))
        print("Round results:", summary)
        print("Total points:", player_points)
        
        again = input("\nWanna go again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("\nFinal Scores:", player_points)
            break
    
if __name__ == "__main__":
    play_game()


