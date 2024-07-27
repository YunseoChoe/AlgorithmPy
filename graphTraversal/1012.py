# 유기농 배추
# dfs 함수
def dfs(start_x, start_y):
    visited[start_x][start_y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    print(f"기존 x,y 좌표: {start_x, start_y}")
    for i in range(4):
        x = start_x + dy[i]
        y = start_y + dx[i]
        print(f'x, y 좌표: {x, y}')
    print()

    if 0 <= x < n and 0 <= y < m and mat[x][y] == 1 and visited[x][y] == 0:
        print("!!")
        dfs(x, y)

# 코드 시작
t = int(input())
return_values = []

for _ in range(t):
    m, n, k = map(int, input().split())
    mat = []

    # visited 초기화
    visited = []
    for i in range(n):
        v = []
        for j in range(m):
            v.append(0)
        visited.append(v)

    # mat 초기화
    for i in range(n):
        mat_row = []
        for j in range(m):
            mat_row.append(0)
        mat.append(mat_row)
            
    # 배추 자리 표시
    for _ in range(k):
        x, y = map(int, input().split())
        mat[y][x] = 1

    print(mat)

    # 함수 호출
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)


