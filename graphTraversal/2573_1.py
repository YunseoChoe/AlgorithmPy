import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0의 개수 반환 함수 (주변 바다의 개수를 반환)
def melt(i, j):
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
            around_sea[i][j] += 1

# BFS로 빙산 덩어리의 개수를 세기
def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            new_x, new_y = x + dx[k], y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and graph[new_x][new_y] > 0:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

if __name__ == '__main__':
    n, m = map(int, input().split())  # 행, 열
    graph = [list(map(int, input().split())) for _ in range(n)]
    around_sea = [[0] * m for _ in range(n)]
    year = 0
    while True:
        year += 1
        visited = [[False] * m for _ in range(n)]
        is_zero = True  # 모두 녹았을 경우를 확인하는 변수
        
        # 1. `melt` 계산을 한 번에 끝냄
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0:
                    is_zero = False
                    melt(i, j)
        if is_zero:
            print(0)
            break
            
        # 2. 얼음 녹이기
        for i in range(n):
            for j in range(m):
                if graph[i][j] > around_sea[i][j]:
                    graph[i][j] -= around_sea[i][j]
                else:
                    graph[i][j] = 0
                around_sea[i][j] = 0

        # 3. 빙산이 분리되었는지 확인 (BFS로 연결된 영역 세기)
        count = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    bfs(i, j)
                    count += 1

        # 4. 분리되는 영역이 2개 이상이면 종료
        if count >= 2:
            print(year)
            break