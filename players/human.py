from game.rules import is_valid_move

def human_player(board, player):
    print(f"Player {player}'s turn:")
    x = int(input("Enter row: ")) - 1
    y = int(input("Enter column: ")) - 1

    if not is_valid_move(board, (x,y)):
        print("Enter row (1-3): ")
        return human_player(board)
    
    return (x,y)