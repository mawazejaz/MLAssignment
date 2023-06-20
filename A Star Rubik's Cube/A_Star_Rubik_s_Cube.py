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

    # Action functions
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

# Test the solver
initial_state = 'RRRRRRRRRGGGYYYBBBGGGYYYBBBGGGYYYBBBGGGYYYBBBOOOOOOOOOWWW'
solution = solve_cube(initial_state)
if solution is not None:
    print("Solution found! Moves:", solution)
else:
    print("No solution found.")
