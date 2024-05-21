def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.append(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    

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

print("BFS Traversal starting from vertex 'S':")
bfs(graph, 'S')
