# DFS와 BFS 복습
n, m, v = list(map(int, input().split())) # 정점, 간선, 시작 정점
adj_mat = []
dfs_path = [] # dfs 경로 저장 배열
bfs_path = [] # bfs 경로 저장 배열

visited_dfs = [False] * n
visited_bfs = [False] * n

for i in range(n):
    mat = [0] * n
    adj_mat.append(mat)

for i in range(m):
    a, b = list(map(int, input().split()))
    adj_mat[a - 1][b - 1] = 1
    adj_mat[b - 1][a - 1] = 1


def dfs(start, dfs_path):
    # global dfs_path
    if visited_dfs[start]:
        return
    
    dfs_path.append(start + 1)
    visited_dfs[start] = True
    for i in range(len(adj_mat[start])):
        if visited_dfs[i] == False and adj_mat[start][i] == 1:
            dfs(i)

queue = []
def bfs(start, bfs_path):
    # global bfs_path
    visited_bfs[start] = True
    queue.append(start)

    while len(queue) != 0:
        vertex = queue.pop(0)
        bfs_path.append(vertex)
        for i in range(len(adj_mat[vertex])):
            if visited_bfs[i] == False and adj_mat[vertex][i] == 1:
                queue.append(i)
                visited_bfs[i] = True

dfs(v - 1, dfs_path)
bfs(v - 1, bfs_path)
for i in dfs_path:
    print(i, end = " ")
print()
    
for i in bfs_path:
    print(i + 1, end = " ")
