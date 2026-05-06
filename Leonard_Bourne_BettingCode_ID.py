def update_player_points(players, player_points, bets, hand_ranks):
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
    
    bet_multipliers = {1: 1, 2: 2, 3: 3}
    
    round_summary = {}
    
    for player in players: 
        if not all(player in d for d in [player_points, bets, hand_ranks]):
            raise ValueError(f"Incomplete data: {player}")
        
        bet = bets[player]
        rank = hand_ranks[player]
        
        if bet not in bet_multipliers:
            raise ValueError(f"Bet needs to be between 1-3. {bet} for {player}")
        
        raw_score = rank * bet_multipliers[bet]
        
        risk_penalty = bet
        
        net_gain = raw_score - risk_penalty
        
        player_points[player] += net_gain
        
        round_summary[player] = net_gain
        
    return round_summary

def build_round_data(players, community_cards): 
    """ 
    This function structures the data for scoring from raw player objects.
    
    Primary author: Leonard Bourne
    Techniques: Dictionary comprehension, f-strings
    
    
    Args:
        players (list of dict): Each player has 'name', 'hand', 'current_bet'
        community_cards (list of dict): Shared cards
        
    Returns: 
        tuple: 
            player_names (list of strings)
            bets (dict[str, int])
            hand_ranks (dict[str, int])
        
    """
    
    player_names = []
    bets = {}
    hand_ranks = {}
    
    for player in players:
        name = player['name']
        hand = player['hand']
        bet = player['current_bet']
        
        player_names.append(name)
        bets[name] = bet
        
        rank = rank_hand(hand, community_cards)
        hand_ranks[name] = rank
        
    return player_names, bets, hand_ranks



