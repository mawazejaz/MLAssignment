
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tsp_branch_and_bound(graph, start_node):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start_node]
    visited[start_node] = True
    min_cost = math.inf
    best_path = []

    def backtrack(curr_node, curr_cost, depth):
        nonlocal min_cost, best_path

        if depth == num_nodes - 1:
            final_cost = curr_cost + graph[curr_node][start_node]
            if final_cost < min_cost:
                min_cost = final_cost
                best_path = path[:]
            return

        for next_node in range(num_nodes):
            if not visited[next_node]:
                path.append(next_node)
                visited[next_node] = True
                backtrack(next_node, curr_cost + graph[curr_node][next_node], depth + 1)
                path.pop()
                visited[next_node] = False

    backtrack(start_node, 0, 0)
    best_path.append(start_node)
    return min_cost, best_path

# Example usage
# Define the graph as a 2D list where graph[i][j] represents the distance between nodes i and j
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 20, 0]
]
start_node = 0

min_cost, best_path = tsp_branch_and_bound(graph, start_node)

print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
