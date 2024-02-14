def dfs(g, v, visited):
    visited[v] = True
    print(chr(ord('A')+v), end=' ')
    for i in range(len(g)):
        if g[v][i] == True and not visited[i]:
            dfs(g, i, visited)

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

visited = [False] * len(graph)
dfs(graph, 0, visited)