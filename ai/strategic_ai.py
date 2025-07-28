import random
from game.rules import get_winner
from game.board import get_available_moves

def will_move_win(board, position, player):
    x = position[0]
    y = position[1]
    temp_board = [row[:] for row in board]
    temp_board[x][y] = player
    return get_winner(temp_board) != '_'


def finds_winning_moves_ai(board, player):
    available_moves = get_available_moves(board)

    for move in available_moves:
        if will_move_win(board, move, player):
                    return move
        
    return random.choice(available_moves)

def finds_winning_and_losing_moves_ai(board, player):
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    available_moves = get_available_moves(board)

    for move in available_moves:
        if will_move_win(board, move, player):
            return move
    
    for move in available_moves:
        if will_move_win(board, move, opponent):
            return move

    return random.choice(available_moves)