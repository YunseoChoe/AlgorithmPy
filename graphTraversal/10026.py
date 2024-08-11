# 적록색약
import copy

# 입력 
n = int(input())
painting = []
for i in range(n):
    p_list = []
    p = input()
    for j in range(len(p)):
        p_list.append(p[j])
    painting.append(p_list)

# print(painting)

# visited 배열 초기화
visited = []
for i in range(n):
    v = []
    for j in range(n):
        v.append(0)
    visited.append(v)

# visited 초기화
green_red_visited = []
for i in range(n):
    v = []
    for j in range(n):
        v.append(0)
    green_red_visited.append(v)

# print(visited)

# 상하좌우 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정상 함수
def dfs(start_x, start_y):
    if visited[start_x][start_y] == 1:
        return
    visited[start_x][start_y] = 1
    # 상하좌우 비교
    for i in range(4):
        x = start_x + dx[i]
        y = start_y + dy[i] 
        # 조건: 범위 충족, 방문하지 않았고, 색상이 같으면 dfs 진행
        if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and painting[start_x][start_y] == painting[x][y]:
            dfs(x, y)

# 적록색약 함수
def green_red_dfs(start_x, start_y):
    if green_red_visited[start_x][start_y] == 1:
        return
    green_red_visited[start_x][start_y] = 1
    # 상하좌우 비교
    for i in range(4):
        x = start_x + dx[i]
        y = start_y + dy[i]
        # 조건
        if 0 <= x < n and 0 <= y < n and green_red_visited[x][y] == 0:
            # 빨간색일 때
            if painting[start_x][start_y] == 'R' and painting[x][y] == 'G':
                green_red_dfs(x, y)
            # 초록색일 때
            elif painting[start_x][start_y] == 'G' and painting[x][y] == 'R':
                green_red_dfs(x, y)
            # 둘 다 아닐 때
            elif painting[start_x][start_y] == painting[x][y]:
                green_red_dfs(x, y)

dfs_arr = []
# 정상 dfs 호출
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            dfs_arr.append((i, j))

green_red_dfs_arr = []
# 적록색약 dfs 호출
for i in range(n):
    for j in range(n):
        if green_red_visited[i][j] == 0:
            # print(f'여기에서 호출: {painting[i][j]}')
            green_red_dfs(i, j)
            green_red_dfs_arr.append((i, j))
            
print(len(dfs_arr), end = " ")
print(len(green_red_dfs_arr))
