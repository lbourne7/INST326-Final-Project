# INST326-Final-Project

### File purpose
- Finale Program.py : The code file used to run our current game in terminal
- game_data.py: all the values and ranking used in our code used for cards, values, hand names , and any card attributes
- Following files:
            Individual files for each team members contributed code used to organize the code before compiling it all into the finale code of the project.

### How to Run Program
1. Ensure Python 3 is installed on your computer.
2. Download or clone the project files from the GitHub repository.
3. Then open the project folder in VS Code or related terminal.
4. Please ensure that both FinalProjectCode.py and game_data.py are in the same folder or the program will not work.
5. Open the terminal in the project directory.
6. Then run the follwing command python FinalProjectCode.py

### How to use Program 
1. After starting the program, enter in how many players you would like to partake in the game.
2. Each player will need to enter in their name.
3. The program will then privately display each player's hand one at a time.
4. The player can then choose to either "fold" or "play".
   fold: Removes the current player from the round
   play: Continues the round with that player.
5. Community cards will be revealed in stages:
               Flop
               Turn
               River
6. During each stage, the active players must place bets by entering a number between 1-3.
7. After all betting rounds are finished:
               The program will evaluate all of the active hands
               Determine who the winner is
               Display the round points and total scores
8. Players can opt to play again or end the game by selecting yes or no in the terminal after being prompted to play again.

### Annotated Bibliography 
- Jacoby, Oswald. “Poker | Principles, Types, Play, & History | Britannica.” Encyclopædia Britannica, 2021,                         www.britannica.com/topic/poker-card-game.

  Texas Hold’em Poker is a subset of the main game Poker. Given this, it was imperative that we                        first learned Poker itself to understand the ranking system and the rules prior to adding the Texas                          Hold’em Poker modifications, then onto our Maryland twist.
  
- “Poker Hand Rankings & the Best Texas Hold’em Hands.” PokerCoaching Blog -, 20 June 2024, pokercoaching.com/blog/poker-            hands/.

  This was used to understand the poker hands to help team members understand more about the hand
   ranks and rules.
  
- “Texas Hold’em Poker.” Bicyclecards.com, bicyclecards.com/how-to-play/texas-holdem-poker. 

     We used this source to find out the rules of the Texas hold 'em poker card game. For the rules of our game we
  used it to have background information on the plays of the card game. 

### Attribution Chart

| Method/Function | Primary Author| Techniques Demonstrated |
|----------|----------|----------|
| Hand.__str__     | Melody Sims   | magic methods other than __init__()   |
| Hand.__lt__     | Melody Sims     |      |
| Hand.__gt__     | Melody Sims     |      |
| Hand.__eq__     | Melody Sims     |      |
| rank_hand     | Melody Sims     | max() with a key function     |
| Player.__init__     | Melody Sims    |     |
|Hand.__init__     | Melody Sims     |    |
|score_five_cards     | Melody Sims     |    |
|take_players_bets    | Laurencia Aparin   |   |
|determine_winners  | Laurencia Aparin  | sequence unpacking, conditional expression   |
|create_deck    | Jonathan Sanchez     | f-strings containing expressions  |
|shuffle_and_deal     | Jonathan Sanchez     | set operations using difference  |
|build_round_data     | Leonard Bourne     | List comprehensions and Dictionary comprehensions  |
|update_player_points     | Leonard Bourne     |    |
|player_decision     | Leonard Bourne      |    |
|display_private_hands     | Leonard Bourne     | optional parameters and/or keyword arguments   |
|reveal_all_hands    | Leonard Bourne     |    |
|play_game()     | Leonard Bourne     |    |



 
 
 
