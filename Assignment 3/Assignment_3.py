import random
import math

# Genetic Algorithm parameters
POPULATION_SIZE = 100
CITIES = [(2, 3), (5, 8), (1, 6), (7, 2), (9, 5), (4, 1)]  # Coordinates of cities
city_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
GENERATIONS = 50
MUTATION_RATE = 0.01

print("##########################################################")
# Print the list of cities with names and coordinates
for i, city in enumerate(CITIES):
    city_name = city_names[i]
    print(f"City {city_name}: {city[0]}, {city[1]}")
print("##########################################################")

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_route_distance(route):
    """Calculate the total distance of a route"""
    total_distance = 0
    for i in range(len(route)):
        current_city = route[i]
        next_city = route[(i + 1) % len(route)]
        total_distance += calculate_distance(current_city, next_city)
    return total_distance

def generate_individual():
    """Generate a random individual (route)"""
    individual = CITIES[:]
    random.shuffle(individual)
    return individual

def evaluate_fitness(individual):
    """Evaluate the fitness of an individual (route)"""
    distance = calculate_route_distance(individual)
    return 1 / distance  # Fitness is inversely proportional to the distance

def crossover(parent1, parent2):
    """Perform ordered crossover between two parents"""
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child1 = [-1] * len(parent1)
    child2 = [-1] * len(parent1)

    # Copy the selected portion from parents to children
    child1[start:end] = parent1[start:end]
    child2[start:end] = parent2[start:end]

    # Fill in the remaining cities in the order of the other parent
    for i in range(len(parent2)):
        index = (end + i) % len(parent2)
        city = parent2[index]
        if city not in child1:
            child1[child1.index(-1)] = city
        if city not in child2:
            child2[child2.index(-1)] = city

    return child1, child2

def mutate(individual):
    """Swap two randomly selected cities in an individual"""
    mutated_individual = individual[:]
    index1 = random.randint(0, len(mutated_individual) - 1)
    index2 = random.randint(0, len(mutated_individual) - 1)
    mutated_individual[index1], mutated_individual[index2] = mutated_individual[index2], mutated_individual[index1]
    return mutated_individual

# Initialize the population
population = [generate_individual() for _ in range(POPULATION_SIZE)]

# Main loop
for generation in range(GENERATIONS):
    # Evaluate fitness for each individual
    fitness_scores = [evaluate_fitness(individual) for individual in population]

    # Select parents for crossover
    selected_parents = random.choices(population, weights=fitness_scores, k=2*POPULATION_SIZE)

    # Perform crossover and mutation to create offspring
    offspring = []
    for i in range(0, 2*POPULATION_SIZE, 2):
        parent1 = selected_parents[i]
        parent2 = selected_parents[i+1]
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutate(child1))
        offspring.append(mutate(child2))

    # Replace the population with the offspring
    population = offspring

    # Print the best individual in the current generation
    best_individual = max(population, key=evaluate_fitness)
    best_distance = calculate_route_distance(best_individual)
    print(f"Generation {generation+1}: Best distance = {best_distance}")
print("##########################################################")
# Print the overall best individual
best_individual = max(population, key=evaluate_fitness)
best_distance = calculate_route_distance(best_individual)
print(f"\nBest route:")
for i, city in enumerate(best_individual):
    city_name = city_names[CITIES.index(city)]
    print(f"City {city_name}: {city[0]}, {city[1]}")
print("##########################################################")
print(f"Best distance: {best_distance}")
print("##########################################################")
