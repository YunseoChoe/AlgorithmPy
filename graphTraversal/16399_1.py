# 벽 부수고 이동하기 3
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0, 1)) 
    visited[0][0][0] = 1
    
    while q:
        cur_x, cur_y, breaks, dist = q.popleft()
        # 도착했다면 경로 출력 후 종료
        if cur_x == (n - 1) and cur_y == (m - 1):
            print(visited[cur_x][cur_y][breaks]) 
            return

        # 동서남북
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닐 때
                if visited[nx][ny][breaks] == 0 and graph[nx][ny] == 0:
                    q.append((nx, ny, breaks, dist + 1))
                    visited[nx][ny][breaks] = dist + 1
                    
                # 벽일 때 
                if graph[nx][ny] == 1:
                    # 밤이면 제자리 이동
                    if dist % 2 == 0:
                        q.append((cur_x, cur_y, breaks, dist + 1))
                    # 낮이면 그냥 이동
                    elif dist % 2 == 1 and breaks < k and visited[nx][ny][breaks + 1] == 0:
                        q.append((nx, ny, breaks + 1, dist + 1))
                        visited[nx][ny][breaks + 1] = dist + 1
    # 도달하지 못했을 경우
    print(-1)
    return
                            
if __name__ == '__main__':
    # 입력 받기
    n, m, k = map(int, input().strip().split())
    graph = []
    for i in range(n):
        graph_list = list(map(int, input().strip()))
        graph.append(graph_list)

    # visited 초기화
    visited = []
    for i in range(n):
        visited_mat = []
        for j in range(m):
            visited_list = [0] * (k + 1) # k + 1번으로 (k번까지 부실 수 있으니까)
            visited_mat.append(visited_list)
        visited.append(visited_mat)

    # (0, 0)부터 bfs 시작
    bfs() # 거리는 1부터 시작