# 촌수계산
n = int(input())
adj_mat = []
for i in range(n + 1):
    mat = []
    for j in range(n + 1):
        mat.append(0)
    adj_mat.append(mat)

a, b = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = list(map(int, input().split()))
    adj_mat[x][y] = 1
    adj_mat[y][x] = 1

visited = [0] * (n + 1)

def dfs(start, count):
    global flag
    if visited[start] == 1:
        return
    if start == b:
        flag = True
        print(count)
        exit()
    visited[start] = 1
    for i in range(len(adj_mat)):
        if adj_mat[start][i] == 1 and visited[i] == 0:
            dfs(i, count + 1)

flag = False
dfs(a, 0)

if flag == False:
    print(-1)
