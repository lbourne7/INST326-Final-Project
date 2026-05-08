
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
 
                   
        
