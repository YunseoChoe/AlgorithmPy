# 벽 부수고 이동하기 3
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y, 0)) # x, y, breaks (벽을 부수지 않고 시작)
    visited[start_x][start_y][0] = 1 # 시작점부터 경로는 1
    day = True # 낮부터 시작

    while q:
        cur_x, cur_y, breaks = q.popleft()
        print(f'현재 보고있는 cur_x, cur_y: {cur_x}, {cur_y}')
        
        # 도착했다면 경로 출력 후 종료
        if cur_x == (n - 1) and cur_y == (m - 1):
            print("도착!")
            print(visited[cur_x][cur_y][breaks]) 
            return

        # 동서남북
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                print(f'nx, ny: {nx}, {ny}')
                # 벽이 아닐 때 (day 상관 x)
                if visited[nx][ny][breaks] == 0 and graph[nx][ny] == 0:
                    print("벽이 아님")
                    q.append((nx, ny, breaks))
                    visited[nx][ny][breaks] = visited[cur_x][cur_y][breaks] + 1
                    print(f'방문배열: {visited}')
                    # 밤, 낮 변경
                    if day == False:
                        day = True
                    else:
                        day = False

                # 벽일 때 (day가 True일 때만 이동)
                if graph[nx][ny] == 1:
                    print("벽임")
                    # 밤이면 제자리 이동
                    if day == False:
                        print("밤")
                        q.append((cur_x, cur_y, breaks))
                        visited[cur_x][cur_y][breaks] = visited[cur_x][cur_y][breaks] + 1
                        print(f'방문배열: {visited}')
                        # 낮으로 변경
                        day = True
                    
                    # 낮이면 그냥 이동
                    else:
                        print("낮")
                        # 벽을 (k - 1)번 이하로 부셨다면 그냥 이동 (0번도 포함)
                        if breaks < k and visited[nx][ny][breaks + 1] == 0:
                            print("벽을 k - 1번 이하로 부심")
                            q.append((nx, ny, breaks + 1))
                            visited[nx][ny][breaks + 1] = visited[cur_x][cur_y][breaks] + 1
                            print(f'방문배열: {visited}')
                            # 밤으로 변경
                            day = False

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
    bfs(0, 0)
    print(visited)





