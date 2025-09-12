# 빙산
# 1. dfs -> bfs
# 2. python3 -> pypy3
# 3. input 수정

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

graph = []

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0의 개수 반환 함수
def melt(i, j):
    zero_cnt = 0 # 0의 개수
    # 상하좌우 보면서 0의 개수를 대입
    for k in range(4):
        new_x = i + dx[k]
        new_y = j + dy[k]
        if 0 <= new_x < n and 0 <= new_y < m:
            if graph[new_x][new_y] == 0:
                zero_cnt += 1
    return zero_cnt

# def dfs(i, j):
#     if visited[i][j]:
#         return
#     visited[i][j] = True                                                        
#     # 상하좌우보면서 방문하지 않았고, 0보다 크면 dfs 진행
#     for k in range(4):
#         new_x = i + dx[k]
#         new_y = j + dy[k]
#         if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] == False and graph[new_x][new_y] > 0:
#             dfs(new_x, new_y)  

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        # 동서남북
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] == False and graph[new_x][new_y] > 0:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

if __name__ == '__main__':
    n, m = map(int, input().split()) # 행, 렬
    # enter graph input
    for i in range(n):      
        graph_list = list(map(int, input().strip().split(' ')))
        graph.append(graph_list)
    
    year = 0
    while True:
        year += 1
        # 방문 배열 초기화
        visited = []
        for _ in range(n):
            visited_list = [False] * m
            visited.append(visited_list)

        # 인접한 바다 행렬 만드는 작업 (around_sea)
        around_sea = []
        for _ in range(n):
            around_sea_list = [0] * m
            around_sea.append(around_sea_list)
        
        is_zero = True # 모두 녹았을 경우를 확인하는 변수
        for i in range(n):
            for j in range(m):
                # 0보다 크면
                if graph[i][j] > 0:
                    is_zero = False
                    around_sea[i][j] = melt(i, j)
                
        # 녹이기
        for i in range(n):
            for j in range(m):
                if graph[i][j] > around_sea[i][j]:
                    graph[i][j] -= around_sea[i][j]
                else:
                    graph[i][j] = 0

        # 분리 여부
        count = 0
        for i in range(n):
            for j in range(m):
                # 방문하지 않았고, 0보다 크면 bfs
                if graph[i][j] > 0 and visited[i][j] == False:
                    bfs(i, j)
                    count += 1

        # 분리되는 영역이 2개가 될 때까지 반복
        if count >= 2:
            print(year)
            break  

        # 빙산이 모두 녹았는데 분리되지 않았을 경우 (언젠간 다 녹아서 0이 되지 않나..?)
        if is_zero:
            print(0)
            break
