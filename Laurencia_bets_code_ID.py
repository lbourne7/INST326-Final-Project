
from random import choice
def take_players_bets(players):
    """"
    Author: Laurencia Aparin
    
    Take the players bets and keeps them for active player of the round. 
    
    Args:
        players(list): A list of player object. Each object has to have
        'folded', 'name', and 'current_bet' attributes. 
        
    Returns:
       int: The total sum of the bets collected during the round 
       
    Side effects:
         Changes the current_bet attribute to the player object of each of them
         in the list. 
         Prints the error message if invalid and the enter the bet when being ran 
         Waits until the user input is given to continue
         
    Raises:
        ValueError: If a non-numeric string is entered by the user (this 
        is caught and makes the user enter a correct input )
           
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
     
    Args:
        players(list): List of player objects and the players have the attributes
        of the name(str) as a string for each player and hand(list) as a list
        folded (bool) if player is playing or not.
        community cards (list): is a list that of string is being used to
        show the shared/ common cards
        
    Returns:
        A tuple that contains the winners_names and highest_score where the 
        winners_name(str) is a string of names and the highest_score is the 
        winner of the rank value.
         
    Side Effects:
        It prints out the community cards and the players hand as they are playing
        and their rank 
    
    Raises:
        if player object is missing attributes
    
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
 
                   
        
