import heapq


def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    shortest_paths = {node: float("inf") for node in graph}
    shortest_paths[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return shortest_paths


graph = {
    "A": {"B": 3},
    "B": {"A": 3, "C": 1, "D": 5},
    "C": {"B": 1, "D": 2, "E": 7},
    "D": {"B": 5, "E": 2},
    "E": {"C": 7, "D": 2},
}

start_vertex = "A"
shortest_distance = dijkstra(graph, start_vertex)

for vertex, distance in shortest_distance.items():
    print(f"The shortest path from {start_vertex} to {vertex}: {distance}")
