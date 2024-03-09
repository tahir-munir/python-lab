def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print("visited ", visited)
            print("graph: ", graph[vertex])
            i=0
            for neighbor in graph[vertex]:
                i += 1
                print( i)
                print("neibor: ", neighbor)
                if neighbor not in visited:
                    queue.append(neighbor)

            
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("BFS Traversal starting from vertex 'A':")
bfs(graph, 'A')