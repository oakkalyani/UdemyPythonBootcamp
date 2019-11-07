# Tictacktoe game
# Step1: Create an empty 3x3 array - can be of any initialization
import numpy as np
board = np.zeros((3,3))

# def empty_board():
#     board = np.zeros((3,3))
#     print(board)
#     return board
# empty_board()

def display_board():
    print(board)

#Ask player for x or o marker
def player_marker():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        marker = input('Player: Select a valid marker x or o: ')
        print(marker)
    if marker == 'x' or marker == 'o':
        return marker

# Accept player position on board
# Condition: Board is not occupied and inputs are valid in range
selection_list=[]
def player_position():
    selection = 0
    while(selection>9 or selection<1):
        selection = int(input('Player: Select a valid location between 1-9: '))
    if ((selection<=9 or selection>=1) and selection not in selection_list):
        selection_list.append(selection)
        print('selection: ',selection)
        return selection
    else:
        print('Invalid Input or occupied cell')

# player_position()

######################################
## Is there a way to do this better?
######################################

# # Assign marker to correct position on board
def marker_position_assign(board,marker,selection):
    # Check if position is emp
    if selection == 1:
        board[0][0]=marker
    elif selection == 2:
        board[0][1]=marker
    elif selection == 3:
        board[0][2]=marker
    elif selection == 4:
        board[1][0]=marker
    elif selection == 5:
        board[1][1]=marker
    elif selection == 6:
        board[1][2]=marker
    elif selection == 7:
        board[2][0]=marker
    elif selection == 8:
        board[2][1]=marker
    elif selection == 9:
        board[2][2]=marker
    else:
        print('Invalid!')
marker_position_assign(board,'x',5)
display_board(board)

# Check for wins :
# Logic : Check each row and column and diagonal. For a win, it should contain only one unique element in case of a win
def checkrow(board):
    for row in board:
        if len(set(row))==1:
            return row[0]
    return 0
def checkdiag(board):
    for i in range(len(board)):
        if len(set(board[i][i]))==1:
            return board[0]
        if len(set(board[i][len(board)-i-1])):
            return board[0][len(board)-1]
    return 0
def checkwins(board):
    for newBoard in (board,np.transpose(board)):
        result = checkrow(newBoard)
        if result:
            return result
    return checkdiag(board)

# Driver Code
print('Welcome!')

while (True):
    board = np.zeros((3,3))
        player1_marker,player2_marker = player_marker()
        start_game = input('Begin Playing? Enter Y or N')
        if start_game.lower=='y':
            game_on = True
        else:
            game_on = False

        while game_on:
            display_board(board)
            position = player_position()
            marker_position_assign(board,player1_marker)

            if checkwins(board):
                display_board(board)
                print('Congratulations! You have won!!')
                game_on = False
            else:
                print('Draw!')
