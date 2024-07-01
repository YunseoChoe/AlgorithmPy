# 바이러스
n = int(input())
e = int(input())

dfs_arr = []
adj_mat = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(e):
    edge = map(int, input().split())
    edge = list(edge)
    adj_mat[edge[0]][edge[1]] = 1
    adj_mat[edge[1]][edge[0]] = 1

visited = [0] * (n + 1)
def dfs(start):
    if visited[start] == 1:
        return
    else:
        visited[start] = 1
        # print(start, end = " ")
        dfs_arr.append(start)
        for i in range(len(adj_mat[0])):
            if visited[i] == 0 and adj_mat[start][i] == 1:
                dfs(i)

dfs(1)
print(len(dfs_arr))