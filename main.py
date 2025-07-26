import random

def init_board():
    board = [ ['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_'] ]
    return board

def print_board(board):
    for row in board:
        print(row)

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

def get_move(board):
    x = int(input("Enter row: "))
    y = int(input("Enter column: "))

    if not is_valid_move(board, (x,y)):
        return get_move(board)
    
    return (x,y)

def make_move(board, position, player):
    x = position[0] - 1
    y = position[1] - 1
    board[x][y] = player
    return board

def player_turn(turn):
    if turn:
        return 'X'
    else: 
        return 'O'

def get_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    
    return '_'

# AI

def random_ai(board):
    x = random.randrange(3) + 1
    y = random.randrange(3) + 1
    if not is_valid_move(board, (x,y)):
        return random_ai(board)
    
    return (x,y)

def random_ai2(board):
    list_available = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                list_available.append((x+1,y+1))
    return random.choice(list_available)

def play():
    turn = True
    board = init_board()
    print_board(board)
    print()
    count = 0
    is_winner = '_'

    while is_winner == '_':
        board = make_move(board, random_ai2(board), player_turn(turn))
        count += 1
        turn = not turn
        print_board(board)
        print()
        if count >= 5:
            is_winner = get_winner(board)
        
        if count == 9:
            break
    
    if not is_winner == '_':
        print(f"The winner is {is_winner}")
    else:
        print ("The match has ended in a draw!")

play()