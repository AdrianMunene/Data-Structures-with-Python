def bellman_ford(graph, start):
    # Step 1: Initialize distance and parent dictionaries
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    distance[start] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    parent[neighbor] = node

    # Step 3: Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distance, parent

# Example usage:
graph = {
    'A': {'B': -1, 'C': -2},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start = 'A'
distances, parents = bellman_ford(graph, start)

# Print the results
# for node in graph:
#     print(f"Shortest distance from {start_node} to {node}: {distances[node]}")
#     path = []
#     current = node
#     while current is not None:
#         path.insert(0, current)
#         current = parents[current]
#     print(f"Shortest path: {' -> '.join(path)}\n")
