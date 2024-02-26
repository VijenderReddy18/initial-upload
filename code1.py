import heapq

def dijkstra(graph, start, end):
    shortest_paths = {start: (None, 0)}
    queue = [(0, start, [])]
    while queue:
        (cost, current, path) = heapq.heappop(queue)
        if current == end:
            return cost, path
        for neighbor, edge_cost in graph[current]:
            old_cost = shortest_paths.get(neighbor, (None, float('inf')))[1]
            new_cost = cost + edge_cost
            if new_cost < old_cost:
                shortest_paths[neighbor] = (current, new_cost)
                heapq.heappush(queue, (new_cost, neighbor, path + [current]))
    return None

def get_best_route(graph, start, end):
    best_route = None
    min_time = float('inf')
    for route in graph[start]:
        (next_node, edge_time) = route
        (cost, path) = dijkstra(graph, next_node, end)
        if cost is not None:
            total_time = edge_time + cost
            if total_time < min_time:
                min_time = total_time
                best_route = path + [next_node]
    return min_time, best_route

# Example usage:
graph = {
    'A': [('B', 10), ('C', 5)],
    'B': [('D', 20), ('E', 10)],
    'C': [('D', 15), ('F', 10)],
    'D': [('G', 5)],
    'E': [('F', 5)],
    'F': [('G', 10)]
}

start = 'A'
end = 'G'

min_time, best_route = get_best_route(graph, start, end)

print(f"The best route to take is: {best_route}")
print(f"The total time taken is: {min_time}")