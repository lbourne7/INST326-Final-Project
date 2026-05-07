# Laurencia's function to take players bets and return winner while giving 
# player feedback 

from random import choice
def take_players_bets(players):
    """"
    Author: Laurencia Aparin
    
    The will be for the betting round and it would get and collct the players 
    bets:
    
    Atributes:
         player[name], player[current_bet]
    Args:
        players(list): A list of dictonaries that holds the players names and 
        current bets 
    
    returns:
       int: The total sum of the bets collected
    """
    total_players = 0
    print("Betting round")
    
    for player in players: 
        if player.folded:
            continue 
        while True: 
            try:
                bet = int(input(f" {player['name']}, enter your bet ")) 
                player['current_bet'] = bet 
                total_players += bet
                break 
            except ValueError:
                print("Invalid input. Please enter a number for your bet.")
    return total_players 


def determine_winners(players, community_cards):
    
    """"
     Author: Laurencia Aparin
     
     This is used to evalute the state of the game and identify the players with 
     the highset score 
     
     Techniques used sequence unpacking and condtional expression
     
     Attributes: 
            player[name],player[hand]
     Args:
         players(list): List of player in dictonary having the value of hand 
         community_cards(list): The shared cards on the table 
        
     Returns:
        tuple: winners_names (str), highest_score(int)
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
 
                   
        
def begin_game():

    """""
    This is used to begin the Texas Hold'em game as a mock but not actual 
    Author: Laurencia Aparin 
    
    
    Technique set opertaions (intersection) 
    checks to see if any players card is in the community cards
    """
    
    players = [
        {"name": "Jerry", "hand": ["Ace of Hearts", "Ace of Spades"], "current_bet": 0},
        {"name": "Tom", "hand": ["5 of Clubs", "7 of Diamonds"], "current_bet": 0}
    ]
    
    community_cards = ["Ace of Diamonds", "King of Hearts", "10 of Spades", "3 of Clubs", "7 of Hearts"]
    
 
    all_player_cards = set(players[0]["hand"] + players[1]["hand"])
    community_set = set(community_cards)
    
    same_cards = all_player_cards.intersection(community_set)
    
    if same_cards: 
        print(f"Found Match{len(same_cards)} cards on the board:{same_cards}")
    
    else:
        print("No direct card match found.")
    
 
    pick = take_players_bets(players)
    print(f"The total of the pick is: {pick}")
    
    winners, top_score = determine_winners(players, community_cards)
    print(f"Winner is {winners.upper()} with score of {top_score}")
    
    
if __name__ == "__main__":
    begin_game()

                
            
            
    
 
