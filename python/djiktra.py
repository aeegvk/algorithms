import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
# Sample usage
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 4},
    'E': {'D': 4}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {distances}")
