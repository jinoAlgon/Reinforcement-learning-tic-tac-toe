class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.winner = None

    def print_board(self):
        print("-------------")
        print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|")
        print("-------------")
        print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|")
        print("-------------")
        print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|")
        print("-------------")

    def is_valid_move(self, move):
        if self.board[move] == " ":
            return True
        return False

    def make_move(self, move):
        self.board[move] = self.current_player
        self.check_winner()
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for positions in win_positions:
            if self.board[positions[0]] == self.board[positions[1]] == self.board[positions[2]] != " ":
                self.winner = self.board[positions[0]]
                return

        if " " not in self.board:
            self.winner = "draw"
