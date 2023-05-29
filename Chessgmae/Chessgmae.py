
class Chessboard:
    def __init__(self):
        self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self.current_player = 'white'
        self.move_history = []

    def print_board(self):
        print("  a b c d e f g h")
        for i in range(len(self.board)):
            print(8 - i, end=' ')
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print(8 - i)
        print("  a b c d e f g h")

    def get_coordinates(self, position):
        file = ord(position[0]) - ord('a')
        rank = 8 - int(position[1])
        return rank, file

    def make_move(self, from_pos, to_pos):
        from_rank, from_file = self.get_coordinates(from_pos)
        to_rank, to_file = self.get_coordinates(to_pos)

        piece = self.board[from_rank][from_file]
        self.board[from_rank][from_file] = ' '
        self.board[to_rank][to_file] = piece

        self.move_history.append((from_pos, to_pos))
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def play(self):
        while True:
            self.print_board()
            print(f"It's {self.current_player}'s turn.")
            from_pos = input("Enter the position of the piece you want to move (e.g., e2): ")
            to_pos = input("Enter the destination position (e.g., e4): ")
            self.make_move(from_pos, to_pos)

            play_again = input("Do you want to make another move? (y/n): ")
            if play_again.lower() != 'y':
                break

        print("Game over.")
        print("Move history:")
        for move in self.move_history:
            print(move[0], '->', move[1])


# Create a new chessboard and start playing
chessboard = Chessboard()
chessboard.play()
