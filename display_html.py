import time

# check if file exist
def check_file_exist():
    with open('results.html', 'r') as f:
        f.readlines()

# create file if file not exist
def create_file():
    with open('results.html', 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<style>')
        f.write('\nbody {')
        f.write("\n\tbackground-image: url('resources/bgd_pic1.jpg');")
        f.write('\n\tbackground-size: cover;}')
        f.write('\ntable, th, td {border:1px solid black;}')
        f.write('\ntd {text-align: center;}')
        f.write('\n</style>\n<body>')
        f.write('\n\n<h2>Score board of the Tic Tac Toe game.</h2>')
        f.write('\n\n<table width = "75%">')
        f.write('\n  <tr>')
        f.write('\n\t<th>Name of Player 1</th>')
        f.write('\n\t<th>Name of Player 2</th>')
        f.write('\n\t<th>Score of Player 1</th>')
        f.write('\n\t<th>Score of Player 2</th>')
        f.write('\n\t<th>Draws</th>')
        f.write('\n\t<th>Total Gameplay</th>')
        f.write('\n\t<th>Difficulty</th>')
        f.write('\n\t<th>Timestamp</th>')
        f.write('\n  </tr>')
        f.write('\n' * 5)
    
# write new info to the file
def write_new_info_to_file(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff):
    if diff == 'f': diff = 'Hard'
    elif diff == 'Human': diff = 'Human' 
    else: diff = 'Easy'

    # keep former file info
    with open('results.html', 'r') as f:
        lines = f.readlines()[:-4]

    # write old info, then new info
    with open('results.html', 'w') as f:
        f.writelines(lines)
        f.write('\n  <tr>')
        f.write(f'\n\t<td>{player_1}</td>')
        f.write(f'\n\t<td>{player_2}</td>')
        f.write(f'\n\t<td>{sc_pl1}</td>')
        f.write(f'\n\t<td>{sc_pl2}</td>')
        f.write(f'\n\t<td>{draw}</td>')
        f.write(f'\n\t<td>{num_of_play}</td>')
        f.write(f'\n\t<td>{diff}</td>')
        f.write(f'\n\t<td>{time.ctime()}</td>')
        f.write('\n  </tr>\n')

    # add end to file
    with open('results.html', 'a') as f:
        f.write('</table>')
        f.write('\n</body>')
        f.write('\n</html>')

# full function call
def push_to_html(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff):
    try: check_file_exist()
    except: create_file()

    write_new_info_to_file(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff)

'''
player_1 = 'me'; player_2 = 'CoMpUtEr'; sc_pl1 = 5; sc_pl2 = 5
draw = 7; num_of_play = 17; diff = 'm'

# function call
push_to_html(player_1, player_2, sc_pl1, sc_pl2, draw, num_of_play, diff)
#'''
