# 유기농 배추 복습
# 배추가 심어져 있는 영역을 구하는 문제이니, 깊이 우선 탐색(dfs)로 풀면 될 것 같음.
# dfs 함수
def dfs(start_x, start_y):
    print(f'start: {start_x}행 {start_y}열')
    global cnt
    if visited[start_x][start_y] == True:
        return
    for i in range(start_x + 1, n):
        for j in range(start_y + 1, m):
            if visited[i][j] == False and adj_mat[i][j] == 1:
                cnt += 1
                print(f'i: {i}, j: {j}')
                dfs(i, j)


t = int(input()) # 테스트의 개수
for i in range(t):
    m, n, k = list(map(int, input().split())) # 가로, 세로, 배추 개수

    adj_mat = []
    visited = []
    for j in range(n):
        mat = [0] * m
        v = [False] * m
        adj_mat.append(mat)
        visited.append(v)
       
    for j in range(k):
        x, y = list(map(int, input().split()))
        adj_mat[y][x] = 1

    cnt = 0
    dfs(0, 0)
    print(cnt)    


# m = 5
# n = 3
# cnt = 0
# adj_mat = [[1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
# visited = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# def dfs(start_x, start_y):
#     if visited[start_x][start_y]:
#         return
#     visited[start_x][start_y] = 1
#     for i in range(start_x, n):
#         for j in range(start_y, m):
#             if visited[i][j] == 0 and adj_mat[i][j] == 1:
#                 dfs(i, j)

# cnt = 0
# for i in range(len(adj_mat)):
#     for j in range(len(adj_mat[0])):
#         if adj_mat[i][j] == 1 and visited[i][j] == 0:
#             print(f'{i}행 {j}열')
#             cnt += 1
#             dfs(i, j)

# print(cnt)
