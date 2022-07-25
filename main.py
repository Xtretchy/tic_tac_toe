import random
from display_html import push_to_html

# introduction and welcome
def introduction():
    print('Hello. Welcome to the Tic Tac Toe game.')

# instructions?
def instructions():
    inst = input('Would you like to read the instructions (y/n)? ').lower()

    if (inst == 'y'):
        print('\nFor this game, 1 or 2 players are required. Player 1 is O, and Player 2 is X.')
        print('''
    This is the layout of the game:

         |     |     
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     

    To play, each player has to enter a number which specifies a position on the layout.

    N.B.: Any player who loses the current game plays first in the next.''')
    else: print('...')
    input('\nPress Enter to continue...')

# number and names of players
def player_info():
    try:
        num_of_players = int(input('\nEnter number of players (1 for Human vs Computer, 2 for Human vs Human): '))
    except:
        print('Wrong input! Player set to 1.'); num_of_players = 1
    # player names
    if num_of_players == 1:
        player_1 = input('Enter name of human Player: ').capitalize()
        player_2 = 'CoMpUtEr'
        diff = input('\nEnter difficulty level; m for mercy, f for fatality ;) (f/m): ').lower()
    if num_of_players == 2:
        player_1 = input('Enter name of Player 1: ').capitalize()
        player_2 = input('Enter name of Player 2: ').capitalize(); diff = 'Human'
    input('\nPress Enter to begin game...')
    return player_1, player_2, diff

# prints layout of the game
def layout(game):
    print('\n------------------------------')
    print(game)

# registers the position
def pos_finder():
    game = '     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     '
    one = game.find('1'); two = game.find('2'); thr = game.find('3'); fou = game.find('4'); fiv = game.find('5');
    six = game.find('6'); sev = game.find('7'); eig = game.find('8'); nin = game.find('9')
    pos = {1 : one, 2 : two, 3 : thr, 4 : fou, 5 : fiv, 6 : six, 7 : sev, 8 : eig, 9 : nin}
    return pos

# insert the player's sign into the number position 
def insert_num(game, num, var):
    pos = pos_finder()
    game = list(game)
    game[pos[num]] = var
    return ''.join(game)

# checks if player wins
def check_for_wins(game, var):
    pos = pos_finder()
    win = ((var in game[pos[1]] and var in game[pos[2]] and var in game[pos[3]]) or
            (var in game[pos[4]] and var in game[pos[5]] and var in game[pos[6]]) or
            (var in game[pos[7]] and var in game[pos[8]] and var in game[pos[9]]) or
            (var in game[pos[1]] and var in game[pos[4]] and var in game[pos[7]]) or  
            (var in game[pos[2]] and var in game[pos[5]] and var in game[pos[8]]) or
            (var in game[pos[3]] and var in game[pos[6]] and var in game[pos[9]]) or  
            (var in game[pos[1]] and var in game[pos[5]] and var in game[pos[9]]) or
            (var in game[pos[3]] and var in game[pos[5]] and var in game[pos[7]]))
    return win

# function for deciding computer best move
def make_best_move(game, num_list, turn, determiner):
    best_score = -3; best_move = None
    num_list_copy = num_list.copy()
    for move in num_list:
        if turn % 2 == 0: game = insert_num(game, move, 'O')
        else: game = insert_num(game, move, 'X')
        num_list_copy.remove(move)
        score = minimax(game, num_list_copy, turn + 1, determiner)
        game = insert_num(game, move, ' ')
        num_list_copy.insert(0, move)
        if (score > best_score):
            best_score = score; best_move = move
    return best_move

# minimax algorithm
def minimax(game, num_list, turn, det):
    if det == 'O':
        if check_for_wins(game, 'X'): return -1
        elif check_for_wins(game, 'O'): return 1
    else:
        if check_for_wins(game, 'X'): return 1
        elif check_for_wins(game, 'O'): return -1
    if len(num_list) == 0: return 0     
    num_list_copy = num_list.copy()
    scores = []
    for move in num_list:
        if turn % 2 == 0: game = insert_num(game, move, 'O')
        else: game = insert_num(game, move, 'X')
        num_list_copy.remove(move)      
        scores.append(minimax(game, num_list_copy, turn + 1, det))
        game = insert_num(game, move, ' ')
        num_list_copy.insert(0, move)  
        if det == 'O' and turn % 2 == 0 and max(scores) == 1: break
        if det == 'X' and turn % 2 == 1 and max(scores) == 1: break
    if (det == 'O' and turn % 2 == 0): return max(scores)
    elif (det == 'X' and turn % 2 == 1): return max(scores)  
    else: return min(scores)

# prints results for each game iteration
def conclusion(game, win, full, turn, player_1, player_2, sc_pl1, sc_pl2, draw):
    layout(game)
    if win:
        if turn == 0:
            print(f'{player_1}(O) wins!')
            sc_pl1 += 1; turn = 1; # making the loser be the first to play
        elif turn == 1:
            print(f'{player_2}(X) wins!')
            sc_pl2 += 1;  turn = 0; # making the loser be the first to play    
    elif full:
        print("Board is full. No Player wins. It's a draw")
        draw += 1
    return sc_pl1, sc_pl2, draw, turn

# prints the final conclusion of the game
def total_conclusion(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff, tot_scs):
    # game statistics
    print('\n----------------------------------------')
    print(f'Total scores {tot_scs}; {player_1} = {sc_pl1}, {player_2} = {sc_pl2}, Draws = {draw}')
    print(f'Total number of plays is {num_of_play}')
    # writing results to html
    try:
        push_to_html(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff)
        print('\nResults added to "results.html" file.')
    except Exception as err:
        print('\nUnable to write results to the html file :(')
        print(err)
    # end
    print('\nThank you playing, we hope you had a nice game session.')
    input('Press Enter to exit...')
    
# each start of the game (for the same players)
def iteration(turn_counter, player_1, player_2, diff, sc_pl1, sc_pl2, draw):
    num_list = list(range(1, 10))
    full = False; win = False # setting win and full to False
    game = '     |     |     \n     |     |     \n_____|_____|_____\n     |     |     \n     |     |     \n_____|_____|_____\n     |     |     \n     |     |     \n     |     |     \n'

    # while loop
    while (win != True and full != True):
        layout(game) # prints the current game layout

        if turn_counter % 2 == 0:
            if player_1 == 'Tkx': # testing algorithm against algorithm
                num = make_best_move(game, num_list, turn_counter, 'O')
                print(f'Turn of {player_1}(0): {num}')
            else:
                while True:
                    try:
                        num = int(input(f'Turn of {player_1}(O): ')) # only an int
                        while (num not in num_list): # present in list
                            num = int(input(f'Turn of {player_1}(O): '))
                        break
                    except: continue
            turn = 0
            game = insert_num(game, num, 'O')
            win = check_for_wins(game, 'O')
        else:
            if player_2 == 'CoMpUtEr':
                if diff == 'f': num = make_best_move(game, num_list, turn_counter, 'X')
                else: num = random.choice(num_list)
                print(f'Turn of {player_2}(X): {num}')
            else:                
                while True:
                    try:
                        num = int(input(f'Turn of {player_2}(X): ')) # only an int
                        while (num not in num_list): # present in list
                            num = int(input(f'Turn of {player_2}(X): '))
                        break
                    except: continue
            turn = 1
            game = insert_num(game, num, 'X')
            win = check_for_wins(game, 'X')
        num_list.remove(num); turn_counter += 1

        if win: break
        if (len(num_list) <= 0): full = True; break

    if win or full:
        (sc_pl1, sc_pl2, draw, turn) = conclusion(game, win, full, turn, player_1, player_2, sc_pl1, sc_pl2, draw)

    print(f'Score: {player_1} is {sc_pl1}, and {player_2} is {sc_pl2}')
    gpq = input('Do you want to play again (y/n)? ')
    return(gpq, player_1, player_2, diff, sc_pl1, sc_pl2, draw, turn)

# function to begin game playing
def game_play():
    game_play_question = 'y'
    introduction()
    instructions()
    player_1, player_2, diff = player_info()
    sc_pl1 = 0; sc_pl2 = 0; draw = 0; tot_scs = 0; num_of_play = 0; turn = 0

    while game_play_question == 'y' or game_play_question == '' :
        game_play_question, player_1, player_2, diff, sc_pl1, sc_pl2, draw, turn = iteration(turn, player_1, player_2, diff, sc_pl1, sc_pl2, draw)
        num_of_play += 1
        tot_scs = sc_pl1 + sc_pl2

    total_conclusion(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff, tot_scs)

# function call of game
game_play()
