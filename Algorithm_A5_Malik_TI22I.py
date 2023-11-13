import itertools

weights = {
    ('a', 'b'): 10,
    ('a', 'c'): 15,
    ('a', 'd'): 20,
    ('a', 'e'): 25,
    ('a', 'f'): 30,
    ('b', 'c'): 35,
    ('b', 'd'): 40,
    ('b', 'e'): 45,
    ('b', 'f'): 50,
    ('c', 'd'): 55,
    ('c', 'e'): 60,
    ('c', 'f'): 65,
    ('d', 'e'): 70,
    ('d', 'f'): 75,
    ('e', 'f'): 80,
    # Add missing edges with appropriate weights
    ('b', 'a'): 10,
    ('c', 'a'): 15,
    ('d', 'a'): 20,
    ('e', 'a'): 25,
    ('f', 'a'): 30,
    ('c', 'b'): 35,
    ('d', 'b'): 40,
    ('e', 'b'): 45,
    ('f', 'b'): 50,
    ('d', 'c'): 55,
    ('e', 'c'): 60,
    ('f', 'c'): 65,
    ('e', 'd'): 70,
    ('f', 'd'): 75,
    ('f', 'e'): 80,
}

# Calculate all paths and their total weights
def find_all_paths_and_weights(weights):
    all_paths = []
    all_weights = []

    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    for path in itertools.permutations(nodes):
        path_length = 0
        for i in range(len(path) - 1):
            edge = (path[i], path[i + 1])
            path_length += weights[edge]

        # Return to the starting point
        path_length += weights[(path[-1], path[0])]

        all_paths.append(path)
        all_weights.append(path_length)

    return all_paths, all_weights

all_paths, all_weights = find_all_paths_and_weights(weights)

# Find the shortest path
shortest_path_index = all_weights.index(min(all_weights))
shortest_path = all_paths[shortest_path_index]
shortest_distance = all_weights[shortest_path_index]

for i, (path, weight) in enumerate(zip(all_paths, all_weights)):
    print(f"Path {i+1}:", ' -> '.join(path))
    print(f"Distance {i+1}:", weight)
    print()

print("Shortest Path:", ' -> '.join(shortest_path))
print("Shortest Distance:", shortest_distance)

