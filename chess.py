#chess?
#TODO: Taking pieces? other piece movment
#create board
chess_board = [[1] * 8 for i in range(8)]
#chess row numbering from top of board to bottom
chess_rows = [8,7,6,5,4,3,2,1]
#column lettering for board
column_letters = ['a','b','c','d','e','f','g','h']
#size of chess board
CHESS_BOARD_SIZE = 8
count = 0

#print chess board
def print_board():
    print()
    for row in range(0,CHESS_BOARD_SIZE):
        print(chess_board[row])

#Check if piece is in the way.
def collision_detect(check_space):
    column = column_letters.index(check_space[0])
    row = chess_rows.index(int(check_space[1]))
    if chess_board[row][column] != '  ':
        return False

def white_control():
    move = input('Enter a chess move: ')
    if move.startswith('p'):
        destination = move.strip('p')
        if white_pawn(destination) != True:
            return False
    elif move.startswith('r'):
        pass
    elif move.startswith('b'):
        pass
    elif move.startswith('n'):
        pass
    elif move.startswith('q'):
        pass
    elif move.startswith('k'):
        pass
    else:
        print('Enter an appropriate move')
        return False

def black_control():
    move = input('Enter a chess move: ')
    if move.startswith('p'):
        destination = move.strip('p')
        if black_pawn(destination) != True:
            return False
    elif move.startswith('r'):
        pass
    elif move.startswith('b'):
        pass
    elif move.startswith('n'):
        pass
    elif move.startswith('q'):
        pass
    elif move.startswith('k'):
        pass
    else:
        print('Enter an appropriate move')
        return False
                         

#TODO: Add colision detection - pawn can't move foward if another piece is in the way.
#Supports movement of 2 squares if pawn is on original square.
#Returns False if the move is illegal
def white_pawn(desired_square):
    desired_square = list(desired_square)
    try:
        if collision_detect(desired_square) == False:
            print('Enter an appropriate move')
            return False
        desired_row = chess_rows.index(int(desired_square[1]))
        desired_column = column_letters.index(desired_square[0])
        for row in range(0,CHESS_BOARD_SIZE):
            if 'Wp' == chess_board[row][desired_column]:
                if row - desired_row == 1:
                    chess_board[row][desired_column] = '  '
                    chess_board[desired_row][desired_column] = 'Wp'
                    return True
                elif (row - desired_row == 2) and (chess_board[6][desired_column] == 'Wp'):
                    #collision_detect takes a list in the form ['%c', #]
                    if (collision_detect([desired_square[0], desired_row - 1]) == False):
                        print('Enter an appropriate move. Unit in the way')
                        return False
                    chess_board[row][desired_column] = '  '
                    chess_board[desired_row][desired_column] = 'Wp'
                    return True
        print('Enter an appropriate move for white')
        return False

    #inappropriate row entered
    except:
        print('Enter an appropriate move ex: pe4')
        return False

def black_pawn(desired_square):
    desired_square = list(desired_square)
    if collision_detect(desired_square) == False:
        print('Enter an appropriate move')
        return False
    try:
        desired_row = chess_rows.index(int(desired_square[1]))
        desired_column = column_letters.index(desired_square[0])
        for row in range(0,CHESS_BOARD_SIZE):
            if 'Bp' == chess_board[row][desired_column]:
                if desired_row - row == 1:
                    chess_board[row][desired_column] = '  '
                    chess_board[desired_row][desired_column] = 'Bp'
                    return True
                elif (desired_row - row == 2) and (chess_board[1][desired_column] == 'Bp'):
                    if (collision_detect([desired_square[0], 6]) == False):
                        print('Enter an appropriate move. Unit in the way')
                        return False
                    chess_board[row][desired_column] = '  '
                    chess_board[desired_row][desired_column] = 'Bp'
                    return True
        print('Enter an appropriate move for black')
        return False

    #inappropriate row entered
    except:
        print('Enter an appropriate move ex: pe4')
        return False
    
#modify rows for startup
for row in range(0,CHESS_BOARD_SIZE):
    if row == 0:
        chess_board[row] = ['BR','BB','BN','BQ','BK','BN','BB','BR']
    elif row == 1:
        chess_board[row] = ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp']
    elif row == CHESS_BOARD_SIZE - 1:
        chess_board[row] = ['WR','WB','WN','WQ','WK','WN','WB','WR']
    elif row == CHESS_BOARD_SIZE - 2:
        chess_board[row] = ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp']
    else:
        chess_board[row] = ['  ','  ','  ','  ','  ','  ','  ','  ',]

print_board()

while True:
    #if turn = 0 then white's move, else black's move
    turn = count % 2                    
    if turn == 0:
        print("\nWhite's move!")
        #white control
        if white_control() == False:
            print_board()
            continue
    else:
        print("\nBlack's move!")
        #black control
        if black_control() == False:
            print_board()
            continue
    print_board()
    count = count + 1
