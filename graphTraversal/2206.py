# 벽 부수고 이동하기
from collections import deque

n, m = map(int, input().split())

mat = []
for i in range(n):
    mat_list = list(map(int, input()))
    mat.append(mat_list)

visited = []
for i in range(n):
    visited_list = []
    for j in range(m):
        list = [0, 0]
        visited_list.append(list)
    visited.append(visited_list)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, breaks = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y][breaks])
            return
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < m:
                # 벽을 처음 부신 경우
                if mat[new_x][new_y] == 1 and breaks == 0:
                    visited[new_x][new_y][1] = visited[x][y][0] + 1
                    q.append((new_x, new_y, 1))
                # 벽이 아니고 방문하지 않은 경우
                elif mat[new_x][new_y] == 0 and visited[new_x][new_y][breaks] == 0:
                    q.append((new_x, new_y, breaks))
                    visited[new_x][new_y][breaks] = visited[x][y][breaks] + 1
    # 도달하지 못했을 경우
    return -1

if bfs():
    print(-1)
