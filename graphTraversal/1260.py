# DFS와 BFS
n, m, v = input().split()
n = int(n)
m = int(m)
v = int(v)

adj_mat = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    edge = map(int, input().split())
    edge = list(edge)
    adj_mat[edge[0]][edge[1]] = 1
    adj_mat[edge[1]][edge[0]] = 1

visited_dfs = [0] * (n + 1)
def dfs(start):
    if visited_dfs[start] == 1:
        return
    else:
        visited_dfs[start] = 1
        print(start, end = " ")
        for i in range(len(adj_mat[0])):
            if visited_dfs[i] == 0 and adj_mat[start][i] == 1:
                dfs(i)

visited_bfs = [0] * (n + 1)
def bfs(start):
    queue = []
    visited_bfs[start] = 1
    queue.append(start)

    while not len(queue) == 0:
        vertex = queue.pop(0)
        print(vertex, end = " ")
        for i in range(len(adj_mat[0])):
            if adj_mat[vertex][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)