def init_board():
    board = [ ['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_'] ]
    return board

def print_board(board):
    for row in board:
        print(row)

def make_move(board, position, player):
    x = position[0]
    y = position[1]

    board[x][y] = player

    return board

def get_available_moves(board):
    available = []

    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                available.append((x,y))

    return available

def is_board_full(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                return False
    return True