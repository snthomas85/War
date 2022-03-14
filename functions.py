import random

rulebook_general = 'Play a soldier from your hand. If your soldier\'s value is greater than your opponent\'s soldier\'s, you receive a flag point. If you capture six flag points before the computer captures four flag points, you win!'
rulebook_cadet = 'Play a soldier from your hand. If your soldier\'s value is greater than your opponent\'s soldier\'s, you receive a flag point. If you capture five flag points before your opponent does, you win!'

J = 11
Q = 12
K = 13
A = 14

deck = [{A: ['red', 'diamonds']}, {A: ['red', 'hearts']}, {A: ['black', 'spades']}, {A: ['black', 'clubs']}, 
{2: ['red', 'diamonds']}, {2: ['red', 'hearts']}, {2: ['black', 'spades']}, {2: ['black', 'clubs']},
{3: ['red', 'diamonds']}, {3: ['red', 'hearts']}, {3: ['black', 'spades']}, {3: ['black', 'clubs']},
{4: ['red', 'diamonds']}, {4: ['red', 'hearts']}, {4: ['black', 'spades']}, {4: ['black', 'clubs']},
{5: ['red', 'diamonds']}, {5: ['red', 'hearts']}, {5: ['black', 'spades']}, {5: ['black', 'clubs']},
{6: ['red', 'diamonds']}, {6: ['red', 'hearts']}, {6: ['black', 'spades']}, {6: ['black', 'clubs']},
{7: ['red', 'diamonds']}, {7: ['red', 'hearts']}, {7: ['black', 'spades']}, {7: ['black', 'clubs']},
{8: ['red', 'diamonds']}, {8: ['red', 'hearts']}, {8: ['black', 'spades']}, {8: ['black', 'clubs']},
{9: ['red', 'diamonds']}, {9: ['red', 'hearts']}, {9: ['black', 'spades']}, {9: ['black', 'clubs']},
{10: ['red', 'diamonds']}, {10: ['red', 'hearts']}, {10: ['black', 'spades']}, {10: ['black', 'clubs']},
{J: ['red', 'diamonds']}, {J: ['red', 'hearts']}, {J: ['black', 'spades']}, {J: ['black', 'clubs']},
{Q: ['red', 'diamonds']}, {Q: ['red', 'hearts']}, {Q: ['black', 'spades']}, {Q: ['black', 'clubs']},
{K: ['red', 'diamonds']}, {K: ['red', 'hearts']}, {K: ['black', 'spades']}, {K: ['black', 'clubs']}]


def play_game():
    """ This code starts the game by getting the name of the player, storing 
    it in 'player', and running the 'introduce'function.
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    none
    """
    player = get_player()
    introduce(player)

def get_player():
    """ This code gets the self-inputted name of the player and stores it in 'player'. 
    
    PARAMETERS
    ----------
    none
    
    RETURNS
    -------
    player : str
        Name of the player
    """
    player = input('Welcome to the squad! What\'s your name?')
    return player

def introduce(player):
    """ This code starts the game of war. It asks for the inputs of difficulty level
    (either General, which is more difficult, or Cadet, which is easier). It also assesses 
    whether or not the player needs to know how to play and will 
    print the rulebook accordingly. It then starts the player on their game of war at the 
    level the player requested.
    
    PARAMETERS
    ----------
    player : str
        Name of the player
    
    RETURNS
    -------
    none
    """

    difficulty = input('How much training do you have(General or Cadet)?')
    if difficulty == 'General':
        title = 'General'
    elif difficulty == 'Cadet':
        title = 'Cadet'
    
    
    # The statement asks if the General-level player wants a review of the instructions and prints instructions accordingly.
    # Cadet automatically receives rulebook
    # Correct level of game is run. 
    if difficulty == 'General':
        rule_review = input('Okay, General ' + player + ', even experienced leaders sometimes need a run-down of the rules. Do you need to review the rulebook(Yes or No)?')
        if rule_review == 'Yes':
            print(rulebook_general)
            general(player)
        else:
            general(player)
    elif difficulty == 'Cadet':
        print('Okay, Cadet ' + player + ', you\'re new around here. Let\'s take a look at the rulebook.')
        print(rulebook_cadet)
        cadet(player)

def player_flag_points(score):
    """Prints out the number of flags that corresponds 
    to the player's score. 
    
    Parameters
    ----------
    score : int
        The number of rounds the player has won. 
    
    Returns
    -------
    player_flag_points * score : str
        The same number of flags as the player's points
    """
    
    player_flag_points = ('🏳️')
    return(player_flag_points * score)

def computer_flag_points(score):
    """Prints out the number of flags that corresponds 
    to the computer's score. 
    
    Parameters
    ----------
    score : int
        The number of rounds the computer has won. 
    
    Returns
    -------
    computer_flag_points * score : str
        The same number of flags as the computer's points
    """
    
    computer_flag_points = ('🏴‍☠️')
    return(computer_flag_points * score)
        
        

def cadet(player, cards=deck):
     
    """ This code creates the player's hand of 26 unique cards, each of which is randomly chosen 
     from parameter,'cards'. The player's hand is printed. It then does the same for an opponent hand. 
     This hand is not printed. Then, a random card is chosen from each hand and compared. If
     the card from the player hand is greater than the card from the computer hand, a flag 
     point is awarded to the player. Otherwise, a flag point is awarded to the computer. 
     If the player gets 5 flag points first, they receive a 'winner' statement. If 
     the computer gets 5 flag points first, the player receives a 'loser' statement.
    
    PARAMETERS
    ----------
    player : str
        Name of the player
    cards : list
        The deck of cards that will divide into player and computer hands. Default is 'deck' list. 
    
    RETURNS
    -------
    
    """
    print('Time for a draft. Let\'s see who\'s in your army.')
   
    # The player's hand of 26 unique cards is created and printed.
    player_hand = []
    for value in cards:
        value = random.choice(cards)
        if value not in player_hand:
            player_hand.append(value)
        if len(player_hand) == 26:
            break 
    print('Your army:' + str(player_hand))
    
    ready = input('Are you ready to march to battle (Yes or No)?')
    if ready == 'No':
        print('Well, it looks like your opponent\'s ready. Better get ready fast. Time to start!')
     
    # The computer's hand of 26 unique cards is created.       
    comp_hand = []
    for value in cards:
        value = random.choice(cards)
        if value not in comp_hand and player_hand:
            comp_hand.append(value)
        if len(comp_hand) == 26:
            break 
    
    # Creates a list of all the dictionary keys in the player's hand.
    player_keys = []
    for value in player_hand:
        player_keys.append(list(value.keys())[0])
   
    # Creates a list of all the dictionary keys in the computer's hand.
    computer_keys = []
    for value in comp_hand:
        computer_keys.append(list(value.keys())[0])
    
    player_score = 0
    computer_score = 0 
    
    # Chooses a random key from the player's hand and a random key from the computer's hand
    if len(player_hand) > 0 and len(comp_hand) > 0:
        player_soldier = random.choice(player_keys)
        comp_soldier = random.choice(computer_keys)
    
    # One random value from each hand(computer and player) is compared and a point's given for larger value
    for player_soldier, comp_soldier in zip(player_keys, computer_keys): 
        if player_score == 5:
            winner_statement = 'Congratulations, Cadet ' + player + ', you\'ve won the war.'
            print(winner_statement)
            break
        elif computer_score == 5:
            loser_statement = 'Tough luck, Cadet ' + player + ', you\'ve lost the war.'
            print(loser_statement)
            break
        if player_soldier > comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            player_score = player_score + 1 
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
        if player_soldier < comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            computer_score = computer_score + 1 
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
        elif player_soldier == comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
            
        
def general(player, cards=deck):
     
    """ This code creates the player's hand of 26 unique cards, each of which is randomly chosen 
     from parameter,'cards'. The player's hand is printed. It then does the same for an opponent hand. 
     This hand is not printed. Then, a random card is chosen from each hand and compared. If
     the card from the player hand is greater than the card from the computer hand, a flag 
     point is awarded to the player. Otherwise, a flag point is awarded to the computer. 
     If the player gets 6 flag points before the computer gets 4 flag points, they receive a 'winner' statement. 
     Otherwise, the player receives a 'loser' statement.
    
    PARAMETERS
    ----------
    player : str
        Name of the player.
    cards : list
        The deck of cards that will divide into player and computer hands. Default is 'deck' list.
        
    
    RETURNS
    -------
    
    """
    print('Let\'s begin!')
    # The player's hand of 26 unique cards is created and printed.
    player_hand = []
    for value in cards:
        value = random.choice(cards)
        if value not in player_hand:
            player_hand.append(value)
        if len(player_hand) == 26:
            break 
    print('Your army:' + str(player_hand))

    
    # The computer's hand of 26 unique cards is created.       
    comp_hand = []
    for value in cards:
        value = random.choice(cards)
        if value not in comp_hand and player_hand:
            comp_hand.append(value)
        if len(comp_hand) == 26:
            break 
    
    ready = input('Are you ready to march to battle (Yes or No)?')
    if ready == 'No':
        print('Well, it looks like your opponent\'s ready. Better get ready fast. Time to start!')
    
    # Creates a list of all the dictionary keys in the player's hand.
    player_keys = []
    for value in player_hand:
        player_keys.append(list(value.keys())[0])
   
    # Creates a list of all the dictionary keys in the computer's hand.
    computer_keys = []
    for value in comp_hand:
        computer_keys.append(list(value.keys())[0])
    
    player_score = 0
    computer_score = 0 
    
    # Chooses a random key from the player's hand and a random key from the computer's hand
    if len(player_hand) > 0 and len(comp_hand) > 0:
        player_soldier = random.choice(player_keys)
        comp_soldier = random.choice(computer_keys)
    
    # One random value from each hand(computer and player) is compared and a point's given for larger value
    for player_soldier, comp_soldier in zip(player_keys, computer_keys): 
        
        if player_score == 6:
            winner_statement = 'Congratulations, General ' + player + ', you\'ve won the war.'
            print(winner_statement)
            break
        elif computer_score == 4:
            loser_statement = 'Tough luck, General ' + player + ', you\'ve lost the war.'
            print(loser_statement)
            break
        if player_soldier > comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            player_score = player_score + 1 
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
        if player_soldier < comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            computer_score = computer_score + 1 
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
        elif player_soldier == comp_soldier:
            print('Your soldier has value ' + str(player_soldier) + ', and the opponent\'s soldier has value ' + str(comp_soldier) + '.')
            print(player_flag_points(player_score))
            print(computer_flag_points(computer_score))
        

