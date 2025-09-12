# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    q = deque()
    visited[start_x][start_y][0] = 1 # 시작점 경로는 1
    q.append((start_x, start_y))

    while q:
        new_x, new_y = q.popleft()
        # 목적지에 도달했다면
        if new_x + 1 == n and new_y + 1 == m:
            print(max(visited[new_x][new_y][0], visited[new_x][new_y][1]))
            return
        
        # 동서남북
        for i in range(4):
            nx = new_x + dx[i]
            ny = new_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 0이라면
                if graph[nx][ny] == "0":
                    # 벽을 1번 부셨다면
                    if visited[new_x][new_y][1] > 0 and visited[nx][ny][1] == 0: 
                        visited[nx][ny][1] = visited[new_x][new_y][1] + 1
                        q.append((nx, ny))
                    # 벽을 부수지 않았다면
                    elif visited[new_x][new_y][1] == 0 and visited[nx][ny][0] == 0:
                        visited[nx][ny][0] = visited[new_x][new_y][0] + 1
                        q.append((nx, ny))
                
                # 1이고, 방문하지 않았다면
                if graph[nx][ny] == "1" and visited[nx][ny][0] == 0 and visited[nx][ny][1] == 0:
                    # 벽을 부수고 오지 않았다면
                    if visited[new_x][new_y][1] == 0:
                        visited[nx][ny][1] = visited[new_x][new_y][0] + 1
                        q.append((nx, ny))

    # 목적지에 도달하지 못했다면 -1 출력
    print(-1)
    return

if __name__ == '__main__':
    # 입력 받기
    n, m = map(int, input().strip().split(' '))
    graph = []
    for i in range(n):
        graph_list = input().strip()
        graph.append(graph_list)
    
    # visited 초기화 
    visited = []
    for i in range(n):
        visited_mat = []
        for j in range(m):
            visited_list = [0, 0]
            visited_mat.append(visited_list)
        visited.append(visited_mat)

    # (0, 0)부터 bfs 시작
    bfs(0, 0)
