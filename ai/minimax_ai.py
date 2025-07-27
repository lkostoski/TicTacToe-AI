from game.rules import get_winner
from game.board import is_board_full, get_available_moves

def minimax_score(board, player):
    if get_winner(board) == 'X':
        return +10
    elif get_winner(board) == 'O':
        return -10
    elif is_board_full(board):
        return 0

    available_moves = get_available_moves(board)
    scores = []
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    for move in available_moves:
        new_board = [row[:] for row in board]
        new_board[move[0]][move[1]] = player
        score = minimax_score(new_board, opponent)
        scores.append(score)
    
    if player == 'X':
        return max(scores)
    else:
        return min(scores)

def minimax_ai(board, player):
    best_pos = None
    best_score = float('-inf') if player == 'X' else float('inf')

    available_moves = get_available_moves(board)
    
    for move in available_moves:
        new_board = [row[:] for row in board]
        new_board[move[0]][move[1]] = player
        score = minimax_score(new_board, 'O' if player == 'X' else 'X')
        if player == 'X' and score > best_score:
            best_score = score
            best_pos = (move[0], move[1]) 
        elif player == 'O' and score < best_score:
            best_score = score
            best_pos = (move[0], move[1])
    
    return best_pos