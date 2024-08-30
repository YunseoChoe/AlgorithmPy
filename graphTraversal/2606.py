# 바이러스 
n = int(input()) # 컴퓨터의 수
edge = int(input()) # 간선의 개수
cnt = 0

adj_mat = []
for i in range(n):
    mat = []
    for j in range(n):
        mat.append(0)
    adj_mat.append(mat)

for i in range(edge):
    a, b = list(map(int, input().split()))
    adj_mat[a - 1][b - 1] = 1
    adj_mat[b - 1][a - 1] = 1

visited = [False] * n
def dfs(start, cnt):
    if visited[start] == True:
        return
    visited[start] = True
    for i in range(len(adj_mat[start])):
        if visited[i] == False and adj_mat[start][i] == 1:
            cnt = dfs(i, cnt + 1)
    return cnt
            
print(dfs(0, 0))
