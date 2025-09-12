graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3, 4],
    3: [0, 2],
    4: [2],
    5: [1]
}
cnt = 0
visited = [0] * len(graph) # node 6개 고정

print(visited)

def dfs(start, path):
    global cnt
    visited[start] = 1
    if path == 3:
        cnt += 1
        return
    for i in range(len(graph[start])):
        next = graph[start][i]
        if visited[next] == 0:
            dfs(next, path + 1)
            visited[next] = 0

dfs(0, 1)
print(cnt)
