def is_valid_move(board, position):
    x = position[0]
    y = position[1]

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

def get_winner2(board, last_move_pos):
    row = last_move_pos[0]
    col = last_move_pos[1]
    player = board[row][col]

    if all(board[row][y] == player for y in range(3)):
        return player
    
    if all(board[x][col] == player for x in range(3)):
        return player
    
    if row == col and all(board[i][i] == player for i in range(3)):
        return player
    
    if row + col == 2 and all (board[i][2-i] == player for i in range(3)):
        return player
    
    return '_'

def player_turn(turn):
    if turn:
        return 'X'
    else: 
        return 'O'