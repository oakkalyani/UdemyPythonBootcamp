# Tictacktoe game
# Step1: Create an empty 3x3 array - can be of any initialization
def empty_board():
    return np.empty([3,3])

#Step2: Accept player input
def accept_markers():
    marker=''
    markers = ['x','o']
    if marker not in markers:
        marker = input('Choose marker between "x" or "o"')
        if marker == 'x':
            return('x','o')
        else:
            return('o','x')

# Step3: Accept player loaction
def player_position(row,column,marker):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='x' or board[i][j]=='o':
                print('Position occupied. Choose another location')
            else:
                board[i][j]=marker

# Step4: Winning situation
