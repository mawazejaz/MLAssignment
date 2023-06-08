import random
from collections import deque

class RubiksCube:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def is_solved(self):
        for face in self.state.values():
            if len(set(face)) != 1:
                return False
        return True

    def get_neighbors(self):
        neighbors = []
        for move in moves:
            new_state = self.state.copy()
            for face, indices in move.items():
                new_state[face] = [new_state[face][i] for i in indices]
            neighbors.append(RubiksCube(new_state, parent=self))
        return neighbors

    def heuristic(self):
        # Calculate the heuristic value for the cube state
        # You can use any heuristic function of your choice
        pass

    def __hash__(self):
        return hash(str(self.state))

    def __eq__(self, other):
        return self.state == other.state

def solve_rubiks_cube(cube):
    open_set = deque([cube])
    closed_set = set()
    g_scores = {cube: 0}
    f_scores = {cube: cube.heuristic()}

    while open_set:
        current_cube = min(open_set, key=lambda c: f_scores[c])
        if current_cube.is_solved():
            return reconstruct_path(current_cube)

        open_set.remove(current_cube)
        closed_set.add(current_cube)

        for neighbor in current_cube.get_neighbors():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current_cube] + 1
            if neighbor not in open_set or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + neighbor.heuristic()
                neighbor.parent = current_cube  # Update the parent attribute
                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None

def reconstruct_path(cube):
    # Reconstruct the path from the solved cube to the initial cube
    path = []
    while cube is not None:
        path.append(cube)
        cube = cube.parent
    return path[::-1]

def autoplay_rubiks_cube(initial_state):
    cube = RubiksCube(initial_state)
    path = solve_rubiks_cube(cube)
    if path is None:
        print("No solution found.")
    else:
        print("Solution found in", len(path) - 1, "moves.")
        for i, cube in enumerate(path):
            print("Move", i, ":")
            print(cube.state)

# Define the possible moves for each face
moves = [
    {"U": [2, 5, 8, 1, 4, 7, 0, 3, 6], "B": [6, 7, 8, 0, 1, 2, 15, 12, 9], "R": [0, 1, 2, 3, 4, 5, 6, 7, 8], "D": [0, 3, 6, 1, 4, 7, 2, 5, 8], "F": [0, 1, 2, 3, 4, 5, 6, 7, 8], "L": [0, 1, 2, 3, 4, 5, 6, 7, 8]},
    {"U": [0, 3, 6, 1, 4, 7, 2, 5, 8], "B": [0, 1, 2, 9, 10, 11, 6, 3, 0], "R": [0, 1, 2, 3, 4, 5, 6, 7, 8], "D": [2, 5, 8, 1, 4, 7, 0, 3, 6], "F": [2, 5, 8, 1, 4, 7, 0, 3, 6], "L": [2, 5, 8, 1, 4, 7, 0, 3, 6]},
    {"U": [6, 3, 0, 7, 4, 1, 8, 5, 2], "B": [8, 7, 6, 11, 10, 9, 2, 5, 8], "R": [0, 1, 2, 3, 4, 5, 6, 7, 8], "D": [8, 5, 2, 7, 4, 1, 6, 3, 0], "F": [8, 7, 6, 11, 10, 9, 2, 5, 8], "L": [8, 7, 6, 11, 10, 9, 2, 5, 8]},
    {"U": [8, 5, 2, 7, 4, 1, 6, 3, 0], "B": [8, 5, 2, 1, 4, 7, 14, 13, 12], "R": [0, 1, 2, 3, 4, 5, 6, 7, 8], "D": [6, 3, 0, 7, 4, 1, 8, 5, 2], "F": [6, 3, 0, 7, 4, 1, 8, 5, 2], "L": [6, 3, 0, 7, 4, 1, 8, 5, 2]}
]

# Define the initial state of the Rubik's Cube
initial_state = {
    "U": ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
    "B": ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
    "R": ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
    "D": ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
    "F": ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
    "L": ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
}
initial_state1 = {
    "U": ["O", "R", "G", "Y", "Y", "B", "B", "W", "B"],
    "B": ["G", "G", "B", "Y", "W", "W", "W", "R", "O"],
    "R": ["B", "R", "W", "B", "G", "O", "O", "W", "G"],
    "D": ["Y", "R", "O", "Y", "O", "O", "W", "Y", "O"],
    "F": ["B", "R", "Y", "R", "O", "B", "Y", "B", "G"],
    "L": ["R", "G", "R", "G", "R", "Y", "G", "Y", "W"]
}


initial_state2 ={
    "U": ["R", "G", "Y", "B", "G", "R", "Y", "O", "W"],
    "B": ["B", "G", "G", "W", "B", "W", "B", "R", "O"],
    "R": ["R", "G", "O", "R", "Y", "G", "B", "Y", "W"],
    "D": ["W", "O", "Y", "Y", "O", "O", "Y", "B", "W"],
    "F": ["R", "G", "W", "Y", "O", "B", "R", "R", "B"],
    "L": ["O", "B", "G", "O", "W", "R", "Y", "Y", "B"]
}

initial_state3 ={
    "U": ["R", "R", "Y", "G", "B", "W", "Y", "R", "W"],
    "B": ["G", "Y", "B", "O", "W", "R", "W", "O", "R"],
    "R": ["O", "G", "B", "G", "W", "Y", "O", "B", "Y"],
    "D": ["O", "G", "W", "O", "O", "R", "Y", "W", "O"],
    "F": ["G", "R", "O", "R", "Y", "B", "B", "Y", "R"],
    "L": ["W", "G", "R", "B", "R", "O", "G", "Y", "B"]
}

initial_state4 ={
    "U": ["Y", "B", "R", "R", "W", "B", "G", "Y", "Y"],
    "B": ["O", "R", "O", "B", "O", "R", "W", "R", "G"],
    "R": ["O", "G", "O", "R", "B", "W", "W", "O", "G"],
    "D": ["W", "Y", "G", "B", "Y", "O", "O", "O", "O"],
    "F": ["B", "W", "B", "G", "Y", "G", "W", "R", "R"],
    "L": ["G", "Y", "W", "G", "G", "B", "Y", "Y", "R"]
}

initial_state5 ={
    "U": ["B", "G", "B", "O", "Y", "G", "R", "O", "O"],
    "B": ["G", "R", "G", "G", "Y", "W", "B", "B", "Y"],
    "R": ["Y", "B", "B", "G", "R", "O", "O", "R", "W"],
    "D": ["Y", "W", "Y", "O", "Y", "O", "W", "B", "G"],
    "F": ["R", "G", "R", "W", "W", "B", "G", "Y", "R"],
    "L": ["B", "O", "W", "O", "R", "Y", "W", "W", "R"]
}


def generate_random_initial_state():
    colors = ["R", "G", "B", "Y", "W", "O"]  # List of possible colors for the cube
    initial_state = {}

    for face in ["U", "B", "R", "D", "F", "L"]:  # Iterate over each face of the cube
        # Generate a random color for each position on the face
        random_colors = [random.choice(colors) for _ in range(9)]
        initial_state[face] = random_colors

    return initial_state

import random

import random

import random

def shuffle_initial_state(initial_state, moves=20):
    shuffled_state = initial_state.copy()

    for _ in range(moves):
        random_move = random.choice(moves)
        for face, indices in random_move.items():
            shuffled_state[face] = [shuffled_state[face][i] for i in indices]

    return shuffled_state





print(initial_state)

shuffle_initial_state(initial_state,1)
autoplay_rubiks_cube(initial_state)
