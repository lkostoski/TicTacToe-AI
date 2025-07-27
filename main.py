import sys
import random
import time

from game.board import init_board, print_board, make_move
from game.rules import get_winner, player_turn
from players.human import human_player
from ai.random_ai import random_ai, random_ai2
from ai.strategic_ai import finds_winning_moves_ai, finds_winning_and_losing_moves_ai
from ai.minimax_ai import minimax_ai

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
            board = make_move(board, human_player(board, current_player), current_player)
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
        return human_player(board, player)
    elif ai_name == 'minimax':
        return minimax_ai(board, player)
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
        if current_player == 'X':
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
        if is_winner == 'X': return 1
        else: return 2
    else:
        print ("The match has ended in a draw!")
        return 0

def repeated_play(x_ai_name, y_ai_name):
    start_time = time.time()

    count = 0
    draws = 0
    x = 0
    y = 0
    while count < 10:
        winner = play_with_ais(x_ai_name, y_ai_name)
        if winner == 0: draws += 1
        elif winner == 1: x += 1
        elif winner == 2: y += 1
        count += 1
    
    end_time = time.time()
    duration = end_time - start_time
    # 100000 = 3.50s Unoptimized

    print (f"{x_ai_name} won {x} times.")
    print (f"{y_ai_name} won {y} times.")
    print (f"{draws} draws.")
    print()
    print (f"{x_ai_name} won {(x/count)*100} %")
    print (f"{y_ai_name} won {(y/count)*100} %")
    print (f"They drew {(draws/count)*100} %")
    print()
    print(f"Execution time: {duration:.2f} seconds")
    print(f"Games per second: {count/duration:.1f}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x_ai = sys.argv[1]
        o_ai = sys.argv[2]
        repeated_play(x_ai, o_ai)
    else:
        print("Starting default game: random_ai2 vs finds_winning_and_losing_moves_ai")
        play_with_ais('minimax', 'human')