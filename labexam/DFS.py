
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)



graph = {
    'S': ['A', 'B' , 'C'],
    'A': ['E'],
    'B': ['E', 'D'],
    'C': ['D'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

print("\nDFS Traversal starting from vertex 'S':")
dfs(graph, 'S')