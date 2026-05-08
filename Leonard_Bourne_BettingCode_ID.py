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
