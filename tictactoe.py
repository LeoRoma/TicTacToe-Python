# from IPython.display import clear_output
import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
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
    print(board, mark)
    if board[1] == mark and board[2] == mark and board[3] == mark or board[1] == mark and board[5] == mark and board[9] == mark or board[3] == mark and board[5] == mark and board[7] == mark or board[1] == mark and board[4] == mark and board[7] == mark or board[2] == mark and board[5] == mark and board[8] == mark or board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    return False

def choose_first():
    random_start = random.randint(0,1)
    if random_start == 0:
        return True
    return False

def space_check(board, position):
    if board[position] == ' ':
        return True
    return False


def full_board_check(board):
    marked_position_counter = 0
    for index in range(1, 10):
        if board[index] != ' ':
            marked_position_counter += 1
    if marked_position_counter == 9:
        return True
    return False

def player_choice(board):
    choice = 'wrong'
    choice_list = [f'{index}' for index in range(1, 10)]
    available = False

    while choice not in choice_list or available == False:
        choice = input('Please choose a position from 1 to 9: ')
        if choice.isdigit() == False or choice not in choice_list:
            print('Sorry, invalid choice')
        elif space_check(board, int(choice)) == False:
            print('Sorry, position not available')
        else:
            available = True
    
    return int(choice)


def replay():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input('Play again? Press Y or N: ')

        if choice not in ['Y', 'N']:
            print('Please enter Y or N')
        if choice == 'Y':
            return True
    return False


print('Welcome to Tic Tac Toe!')
gameon = True
play = True
player1 = True
while gameon == True:
    player1_marker, player2_marker = player_input()
    random_pick = choose_first()
    if random_pick == True:
        print('Player 1 turn')
    else:
        print('Player 2 turn')
        player1 = False

    while play == True:
        display_board(board)

        if player1 == True:
            print('Player 1 turn')
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker) == True:
                print('Player 1 won!')
                play = False
           
            player1 = False
        else:
            print('Player 2 turn')
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker) == True:
                print('Player 2 won!')
                play = False
            player1 = True

        if full_board_check(board) == True:
            play = False
            print('Game Over! Is a Draw!')

    if replay() == False:
            play = False
            gameon = False
    else:
        play = True  
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']             

