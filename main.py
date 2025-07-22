def init_board():
    board = [ ['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_'] ]
    return board

board = init_board()

def print_board(board):
    for row in board:
        print(row)

print_board(board)

def is_valid_move(board, position):
    x = position[0] - 1
    y = position[1] - 1

    if x < 0 or x > 2:
        print("Row number should be between 1 and 3")
        return False
    
    if y < 0 or y > 2:
        print("Column number should be between 1 and 3")
        return False
    
    if board[x][y] != '_':
        print("Spot already taken")
        return False
    
    return True

def get_move():
    x = int(input("Enter row: "))
    y = int(input("Enter column: "))

    if not is_valid_move(board, (x,y)):
        return get_move()
    
    return (x,y)



def player_turn():
    player = 'X'


# Unifnished, think differently, maybe its not like this
def make_move(board, position, player):
    x = position[0] - 1
    y = position[1] - 1
    new_board = board
    new_board[x][y] = player
    return new_board

board = make_move(board, get_move(), 'X')
print_board(board)