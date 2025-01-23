# 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    q = deque()
    visited[start_x][start_y][0] = 1 # 시작점은 1부터
    q.append((start_x, start_y, 0)) # 벽을 부수지 않고 시작
    
    while q:
        cur_x, cur_y, breaks = q.popleft()
        # 목적지에 도착했다면
        if cur_x + 1 == n and cur_y + 1 == m:
            print(visited[cur_x][cur_y][breaks])
            return
        
        # 동서남북
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이면
                if graph[nx][ny] == "1" and breaks < k and visited[nx][ny][breaks + 1] == 0:
                    # 이미 벽을 k - 1번 이하로 부셨다면 (벽을 한 번도 안 부신 것도 포함)
                    visited[nx][ny][breaks + 1] = visited[cur_x][cur_y][breaks] + 1
                    q.append((nx, ny, breaks + 1))
                        
                # 벽이 아니면
                elif graph[nx][ny] == "0" and visited[nx][ny][breaks] == 0:
                    visited[nx][ny][breaks] = visited[cur_x][cur_y][breaks] + 1
                    q.append((nx, ny, breaks)) 

    # 도달하지 못했다면
    print(-1)
    return 

if __name__ == '__main__':
    # 입력 받기
    n, m, k = map(int, input().strip().split())
    graph = []
    for i in range(n):
        graph_list = input().strip()
        graph.append(graph_list)

    # visited 초기화
    visited = []
    for i in range(n):
        visited_mat = []
        for j in range(m):
            visited_list = [0] * (k + 1) # k + 1번으로 
            visited_mat.append(visited_list)
        visited.append(visited_mat)

    # (0, 0)부터 bfs 시작
    bfs(0, 0)
