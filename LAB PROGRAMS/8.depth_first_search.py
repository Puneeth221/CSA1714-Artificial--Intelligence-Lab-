# Depth First Search (DFS)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
visited_set = set()

def dfs(node):
    if node not in visited_set:
        visited_set.add(node)
        visited.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)

# Start DFS from node A
dfs('A')

print("DFS Traversal:")
print(" -> ".join(visited))