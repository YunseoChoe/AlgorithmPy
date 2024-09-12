# 촌수계산
n = int(input())
adj_mat = []
flag = False
for i in range(n + 1):
    mat = []
    for j in range(n + 1):
        mat.append(0)
    adj_mat.append(mat)

visited = [False] * (n + 1)

a, b = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = list(map(int, input().split()))
    adj_mat[x][y] = 1
    adj_mat[y][x] = 1

def dfs(start, count):
    global flag 
    if visited[start]:
        return
    if start == b:
        flag = True
        print(count)
        exit(0)
    visited[start] = True
    for i in range(n + 1):
        if visited[i] == False and adj_mat[start][i] == 1:
            dfs(i, count + 1)
    
dfs(a, 0)
if not flag:
    print(-1)
