#edited by melody
#Helloooooooo

## edited by laurencia
# hi
# hello 

# The following will be Jonathan Sanchez code: 

import random

def shuffle_and_deal(num_players, deck, comm_count, cards_per_player):
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
    
    if num_players <= 0: 
        raise ValueError("Number of players must be greater than 0!")
    
    if cards_per_player <= 0:
        raise ValueError("Cards per player must be greater than 0!")
    
    if comm_count < 0:
        raise ValueError("Community card count cannot be a negative number!")
    
    total_cards_needed =(num_players * cards_per_player) + comm_count
    
    if total_cards_needed > len(deck):
        raise ValueError("Not enough cards in the deck!")
    
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
        
        
#End of Jonathan Sanchez code 
