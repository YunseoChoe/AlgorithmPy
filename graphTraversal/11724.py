# 연결 요소의 개수
n, m = list(map(int, input().split())) # 정점, 간선 개수

adj_mat = [[0] * (n) for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    adj_mat[u - 1][v - 1] = 1
    adj_mat[v - 1][u - 1] = 1

visited = set()

def dfs(start):
    # global visited 
    if start in visited:
        return
    else:
        visited.add(start)
        for i in range(len(adj_mat[0])):
            if i not in visited and adj_mat[start][i] == 1:
                dfs(i)

cnt = 0
for i in range(n):
    if i not in visited:
        # print(f'vertex: {i}')
        dfs(i)
        cnt += 1

print(cnt)  