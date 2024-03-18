def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nDFS Traversal starting from vertex 'A':")
dfs(graph, 'A')
