import random
from game.rules import is_valid_move
from game.board import get_available_moves

def random_ai(board, player=None):
    x = random.randrange(3)
    y = random.randrange(3) 
    if not is_valid_move(board, (x,y)):
        return random_ai(board)
    
    return (x,y)

def random_ai2(board, player=None):
    return random.choice(get_available_moves(board))