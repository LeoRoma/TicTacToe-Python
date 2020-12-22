# from IPython.display import clear_output
import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('------')
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():
    marker = ''

    while marker != 'O' and marker != 'X':
        player1 = input('Player 1, please choose a mark: O or X: ')
        marker = player1
        if marker == 'X':
            player2 = 'O'
        else: 
            player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark or board[0] == mark and board[5] == mark and board[9] == mark or board[2] == mark and board[5] == mark and board[7] == mark or board[0] == mark and board[4] == mark and board[7] == mark or board[1] == mark and board[5] == mark and board[8] == mark or board[2] == mark and board[6] == mark and board[9] == mark:
        return True
    return False

def choose_first():
    random_start = random.randint(0,1)
    if random_start == 0:
        return 'Player 1 start'
    return 'Player 2 start'

display_board(board)
player1_marker, player2_marker = player_input()
display_board(board)
print(win_check(test_board, 'X'))


# display_board(test_board)
# game_list = [0,1,2]
# game_on = True

# def display_game(game_list):
#     print('Here is the current list: ')
#     print(game_list)

# def position_choice():
#     choice = 'wrong'

#     while choice not in ['0', '1', '2']:
#         choice = input('Pick a position (0, 1, 2): ')
#         if choice not in ['0', '1', '2']:
#             print('Sorry, invalid choice!')
    
#     return int(choice)


# def replacement_choice(game_list, position):
#     user_placemente = input('Type a string to place at position: ')
#     game_list[position] = user_placemente
#     return game_list






# def gameon_choice():
#     choice = 'wrong'

#     while choice not in ['Y', 'N']:
#         choice = input('Keep playing? (Y or N) ')
#         if choice not in ['Y', 'N']:
#             print('Sorry, I dont understand, please choose Y or N!')
#         if choice == 'Y':
#             return True
#         else:
#             return False
    
#     return int(choice)

# while game_on:
#     display_game(game_list)

#     position = position_choice()

#     game_list = replacement_choice(game_list, position)

#     display_game(game_list)

#     game_on = gameon_choice()
