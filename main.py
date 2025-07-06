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

def get_move():
    x = int(input("Enter row: "))
    if x < 0 or x > 4:
        print("Row number should be between 1 and 3")
        return get_move();
    y = int(input("Enter column: "))
    if y < 0 or y > 4:
        print("Column number should be between 1 and 3")
        return get_move();
    print(x,y)
    return (x,y)

get_move()