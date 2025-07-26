import sys
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

def get_move(board, player):
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

def random_ai(board, player):
    x = random.randrange(3) + 1
    y = random.randrange(3) + 1
    if not is_valid_move(board, (x,y)):
        return random_ai(board)
    
    return (x,y)

def random_ai2(board, player):
    list_available = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                list_available.append((x+1,y+1))
    return random.choice(list_available)

def will_move_win(board, position, player):
    x = position[0] - 1
    y = position[1] - 1
    temp_board = [row[:] for row in board]
    temp_board[x][y] = player
    if get_winner(temp_board) == '_':
        return False
    else:
        return True


def finds_winning_moves_ai(board, player):
    list_available = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                list_available.append((x+1,y+1))
                if will_move_win(board, (x+1, y+1), player):
                    return (x+1, y+1)
    return random.choice(list_available)

def finds_winning_and_losing_moves_ai(board, player):
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    list_available = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                list_available.append((x+1,y+1))
                if will_move_win(board, (x+1, y+1), player):
                    return (x+1, y+1)
    
    for x in range(3):
        for y in range(3):
            if board[x][y] == '_':
                if will_move_win(board, (x+1, y+1), opponent):
                    return (x+1, y+1)

    return random.choice(list_available)

def play_vs_ai():
    turn = random.choice([True, False])
    board = init_board()
    print_board(board)
    print()
    count = 0
    is_winner = '_'

    while is_winner == '_' and count < 9:
        current_player = player_turn(turn)
        if current_player == 'O':
            board = make_move(board, finds_winning_and_losing_moves_ai(board, current_player), current_player)
        else:
            board = make_move(board, get_move(board, current_player), current_player)
        count += 1
        turn = not turn
        print_board(board)
        print()
        if count >= 5:
            is_winner = get_winner(board)
    
    if not is_winner == '_':
        print(f"The winner is {is_winner}")
    else:
        print ("The match has ended in a draw!")

def select_ai(ai_name, board, player):
    if ai_name == 'random_ai':
        return random_ai(board, player)
    elif ai_name == 'random_ai2':
        return random_ai2(board, player)
    elif ai_name == 'finds_winning_moves_ai':
        return finds_winning_moves_ai(board, player)
    elif ai_name == 'finds_winning_and_losing_moves_ai':
        return finds_winning_and_losing_moves_ai(board, player)
    elif ai_name == 'human':
        return make_move(board, player)
    else:
        print(f"Unknown AI: {ai_name}")
        return random_ai2(board, player)
    
def play_with_ais(x_ai_name, y_ai_name):
    turn = random.choice([True, False])
    board = init_board()
    print_board(board)
    print()
    count = 0
    is_winner = '_'

    while is_winner == '_' and count < 9:
        current_player = player_turn(turn)
        if current_player == 'O':
            board = make_move(board, select_ai(x_ai_name, board, current_player), current_player)
        else:
            board = make_move(board, select_ai(y_ai_name, board, current_player), current_player)
        count += 1
        turn = not turn
        print_board(board)
        print()
        if count >= 5:
            is_winner = get_winner(board)
    
    if not is_winner == '_':
        print(f"The winner is {is_winner}")
        if is_winner == 'O': return 1
        else: return 2
    else:
        print ("The match has ended in a draw!")
        return 0

def repeated_play(x_ai_name, y_ai_name):
    count = 0
    draws = 0
    x = 0
    y = 0
    while count < 10000:
        winner = play_with_ais(x_ai_name, y_ai_name)
        if winner == 0: draws += 1
        elif winner == 1: x += 1
        elif winner == 2: y += 1
        count += 1
    print (f"{x_ai_name} won {x} times.")
    print (f"{y_ai_name} won {y} times.")
    print (f"{draws} draws.")
    print()
    print (f"{x_ai_name} won {(x/count)*100} %")
    print (f"{y_ai_name} won {(y/count)*100} %")
    print (f"They drew {(draws/count)*100} %")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x_ai = sys.argv[1]
        o_ai = sys.argv[2]
        repeated_play(x_ai, o_ai)
    else:
        print("Starting default game: random_ai2 vs finds_winning_and_losing_moves_ai")
        play_with_ais('random_ai2', 'finds_winning_and_losing_moves_ai')