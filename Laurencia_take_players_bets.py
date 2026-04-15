# Laurencia's function to take players bets and return winner while giving 
# player feedback 

from random import choice
def take_players_bets(players):
    """"
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
        while True: 
            try:
                bet = int(input(f"{player['name']}, enter your bet ")) 
                player['current_bet'] = bet 
                total_players += bet
                break 
            except ValueError:
                print("Invalid input. Please enter a number for your bet.")
    return total_players 


def determine_winners(players, community_cards):
    
    """"
     This is used to evalute the state of the game and identify the players with 
     the higest score 
     
     Attributes: 
            player[name],player[hand]
     Args:
         players(list): List of player in dictonary having the value of hand 
         community_cards(list): The shared cards on the table 
        
     Returns:
        tuple: winners_names (str), highest_score(int)
    """
    
    highest_score = -1
    winners_name = "None"
    calculate_hands = 0
    
    print("Final Hand Ranking ")
    print(f"Community Cards: {', ' .join(community_cards)}")
  
    for player in players: 
      
        total_cards = player['hand'] + community_cards
       
        if calculate_hands is not None:
           rank_name, score =  mock_hands(total_cards)
           
        if calculate_hands is None:
            score = int(1,100)
            rank_name = "High card"
       
        """rank_name, score = mock_hands(total_cards)
         """   
      
        print (f"{player['name']} had: { ', '.join(player['hand'])}")
        print(f"Result: {rank_name} (Score: {score})")
    
        if score > highest_score:
            highest_score = score
            winners_name = player['name']
        else:
            if score == highest_score:
                if player['name']:
                
                 winners_name = winners_name + " and " + player["name"]
        
        
    return winners_name, highest_score
 
            
            
def mock_hands(total_cards):
    """"
    This is a mock function that acts as the hand logic 
    
    Returns:
         tuple: (str) rank_name , int score 
    """

    
    options = [
        ("Royal Flush", 49),
        ("Full House", 30),
        ("Two Pair", 20),
        ("High Card", 1)
    ]
    return choice(options)
    
  
        
def begin_game():

    """""
    This is used as a mock to test my code and the game
    """
    
    players = [
        {"name": "Jerry", "hand": ["Ace of Hearts", "Ace of Spades"], "current_bet": 0},
        {"name": "Tom", "hand": ["5 of Clubs", "7 of Diamonds"], "current_bet": 0}
    ]
    
    community_cards = ["Ace of Diamonds", "King of Hearts", "10 of Spades", "3 of Clubs", "7 of Hearts"]
        
    
    pick = take_players_bets(players)
    print(f"The total of the pick is: {pick}")
    
    winners, top_score = determine_winners(players, community_cards)
    print(f"Winner is {winners.upper()} with score of {top_score}")
    
    
if __name__ == "__main__":
    begin_game()

                
            
                
