def init_board():
    board = [ ['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_'] ];
    return board;

board = init_board();

def print_board(board):
    for row in board:
        print(row);

print_board(board);
