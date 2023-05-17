from tic_tac_toe import TicTacToe

def get_human_move():
    move = input("Enter your move (1-9): ")
    return int(move) - 1

def play_human_vs_agent(agent):
    game = TicTacToe()
    game.print_board()
    while not game.winner:
        if game.current_player == "X":
            move = get_human_move()
        else:
            move = agent.get_move(game)
        if game.is_valid_move(move):
            game.make_move(move)
            game.print_board()
        else:
            print("Invalid move, please try again.")

    if game.winner == "draw":
        print("The game ended in a draw.")
    elif game.winner == "X":
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost.")
