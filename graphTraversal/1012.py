# 유기농 배추
dfs_arr = []

# visited 초기화
# visited = []
# for i in range(50):
#     v = []
#     for j in range(50):
#         v.append(0)
#     visited.append(v)

# def dfs(start, m, n):
#     start_x, start_y = start
#     visited[start_x][start_y] = 1
#     dfs_arr.append((start_x, start_y))
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for i in range(4):
#         x = start_x + dx[i]
#         y = start_y + dy[i]

#         if 0 <= x < m and 0 <= y < n and mat[x][y] == 1 and visited[x][y] == 0:
#             dfs((x, y), m, n)

#     return len(dfs_arr)

# 코드 시작
t = int(input())
return_values = []

for _ in range(t):
    m, n, k = input().split()
    m = int(m)
    n = int(n)
    k = int(k)
    mat = []

    # mat 초기화
    for i in range(n):
        mat_row = []
        for j in range(m):
            mat_row.append(0)
        mat.append(mat_row)
            
    # 좌표 입력받기
    for _ in range(k):
        x, y = map(int, input().split())
        mat[y][x] = 1

    print(mat)
#     # 함수 호출
#     return_value = dfs((0, 0), m, n)
#     print(f'return_value: {return_value}')
#     return_values.append(return_value)

# return_value = dfs((0, 0), m, n)
# print(return_values)