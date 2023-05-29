import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_position = (0, 0)
        self.wumpus_position = self.generate_random_position()
        self.gold_position = self.generate_random_position()
        self.pit_positions = [self.generate_random_position() for _ in range(size)]
        self.is_game_over = False

    def generate_random_position(self):
        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        return row, col

    def is_valid_position(self, position):
        row, col = position
        return 0 <= row < self.size and 0 <= col < self.size

    def get_adjacent_positions(self, position):
        row, col = position
        adjacent_positions = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1),  # Right
        ]
        return [pos for pos in adjacent_positions if self.is_valid_position(pos)]

    def move_agent(self, position):
        if self.is_valid_position(position):
            self.agent_position = position

    def get_percept(self):
        row, col = self.agent_position
        percept = {}

        if self.agent_position == self.wumpus_position:
            percept['stench'] = True

        for pit_position in self.pit_positions:
            if self.agent_position == pit_position:
                percept['breeze'] = True

        if self.agent_position == self.gold_position:
            percept['glitter'] = True

        return percept

    def draw_board(self):
        print("Wumpus World Board:")
        print("-------------------")
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) == self.agent_position:
                    print('A', end=' ')
                elif (row, col) == self.wumpus_position:
                    print('W', end=' ')
                elif (row, col) == self.gold_position:
                    print('G', end=' ')
                elif (row, col) in self.pit_positions:
                    print('P', end=' ')
                else:
                    print('_', end=' ')
            print()
        print("-------------------")

    def play(self):
        print("Welcome to Wumpus World!")
        print("Goal: Find the gold without getting eaten by the Wumpus or falling into a pit.")

        while not self.is_game_over:
            self.draw_board()
            percept = self.get_percept()
            print("\nPercept:", percept)

            action = input("Enter your action (m for move, g for grab): ").lower()

            if action == 'm':
                direction = input("Enter the direction to move (u for up, d for down, l for left, r for right): ").lower()
                if direction == 'u':
                    self.move_agent((self.agent_position[0] - 1, self.agent_position[1]))
                elif direction == 'd':
                    self.move_agent((self.agent_position[0] + 1, self.agent_position[1]))
                elif direction == 'l':
                    self.move_agent((self.agent_position[0], self.agent_position[1] - 1))
                elif direction == 'r':
                    self.move_agent((self.agent_position[0], self.agent_position[1] + 1))
                else:
                    print("Invalid direction!")

            elif action == 'g':
                if 'glitter' in percept:
                    if self.agent_position == self.gold_position:
                        print("\nCongratulations! You have found the gold and won the game.")
                    else:
                        print("\nSorry, the gold is not at your current location.")

            else:
                print("Invalid action!")

            print("\nAgent Position:", self.agent_position)

            if self.agent_position == self.wumpus_position or self.agent_position in self.pit_positions:
                print("Oops! You got eaten by the Wumpus or fell into a pit.")
                self.is_game_over = True

            print()

        print("\nGame over.")

# Create a new Wumpus World game and start playing
wumpus_world = WumpusWorld()
wumpus_world.play()
