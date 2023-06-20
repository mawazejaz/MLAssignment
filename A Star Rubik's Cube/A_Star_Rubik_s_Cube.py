from queue import PriorityQueue

class CubeNode:
    def __init__(self, cube, g_cost, h_cost, parent=None, action=None):
        self.cube = cube
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
        self.action = action
    
    def __lt__(self, other):
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

def apply_action(state, action):
    if action == 'U':
        state = state[9:] + state[:9]
    elif action == 'D':
        state = state[18:] + state[:18]
    elif action == 'L':
        state = state[:9] + state[27:36] + state[9:27] + state[36:]
    elif action == 'R':
        state = state[:27] + state[36:45] + state[27:36] + state[45:]
    elif action == 'F':
        state = state[:18] + state[27:30] + state[18:21] + state[30:33] + state[21:24] + state[33:]
    elif action == 'B':
        state = state[:24] + state[33:36] + state[24:27] + state[36:39] + state[27:30] + state[39:]
    return state

def get_actions():
    return ['U', 'D', 'L', 'R', 'F', 'B']

def print_cube(cube):
    print(cube[:9])
    print(cube[9:18])
    print(cube[18:27])
    print(cube[27:36])
    print(cube[36:45])
    print(cube[45:])

def solve_cube(cube):
    # Define the goal state
    goal_state = 'RRRRRRRRRGGGYYYBBBGGGYYYBBBGGGYYYBBBGGGYYYBBBOOOOOOOOOWWW'

    # Heuristic function (Manhattan distance)
    def heuristic(state):
        dist = 0
        for i in range(len(state)):
            if state[i] != goal_state[i]:
                dist += 1
        return dist

    # A* algorithm
    start_node = CubeNode(cube, 0, heuristic(cube))
    open_set = PriorityQueue()
    open_set.put(start_node)
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()
        current_state = current_node.cube

        if current_state == goal_state:
            # Goal state reached, construct solution path
            solution_path = []
            while current_node.parent is not None:
                solution_path.insert(0, current_node.action)
                current_node = current_node.parent
            return solution_path

        closed_set.add(current_state)

        for action in get_actions():
            new_state = apply_action(current_state, action)
            if new_state not in closed_set:
                g_cost = current_node.g_cost + 1
                h_cost = heuristic(new_state)
                new_node = CubeNode(new_state, g_cost, h_cost, current_node, action)
                open_set.put(new_node)

    # No solution found
    return None

# Main game loop
def play_game():
    initial_state = 'RRRRRRRRRGGGYYYBBBGGGYYYBBBGGGYYYBBBGGGYYYBBBOOOOOOOOOWWW'
    current_state = initial_state
    moves = []
    print("Welcome to Rubik's Cube Solver!")
    print("Enter 'Q' to quit the game.")
    print("Enter 'S' to solve the cube.")
    while True:
        print("\nCurrent Cube State:")
        print_cube(current_state)
        print("Moves:", moves)
        print("Enter an action (U, D, L, R, F, B) or command:")
        user_input = input().upper()

        if user_input == 'Q':
            print("Exiting the game.")
            break
        elif user_input == 'S':
            print("Solving the cube...")
            solution = solve_cube(current_state)
            if solution is not None:
                print("Solution found! Moves:", solution)
                moves.extend(solution)
                current_state = initial_state
            else:
                print("No solution found.")
        elif user_input in get_actions():
            current_state = apply_action(current_state, user_input)
            moves.append(user_input)
        else:
            print("Invalid input. Please enter a valid action or command.")

# Start the game
play_game()
