# 다리 만들기
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

bfs_list = []

# 라벨링하는 bfs
def label_bfs(start_x, start_y):
    q = deque()
    visited[start_x][start_y] = 1
    q.append((start_x, start_y))
    graph[start_x][start_y] = label
    
    # q가 빌 때까지 반복
    while q:
        cur_x, cur_y = q.popleft() 
        # 만약 동서남북이 1이면 라벨링 후 q에 넣기
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                graph[next_x][next_y] = label
                visited[next_x][next_y] = 1
                q.append((next_x, next_y))

# 최단거리 찾는 bfs
def bfs(label):
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == label:
                q.append((i, j))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                # 다른 대륙 발견하면 바로 종료
                if graph[next_x][next_y] != 0 and graph[next_x][next_y] != label:
                    return visited[cur_x][cur_y]
                # 방문하지 않았고, 바다면 이동하기
                elif visited[next_x][next_y] == 0 and graph[next_x][next_y] == 0:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
    return 1000

if __name__ == '__main__':
    # 입력 받기
    n = int(input())
    graph = []
    for i in range(n):
        graph_list = list(map(int, input().strip().split(' ')))
        graph.append(graph_list)

    # visited 초기화
    visited = []
    for i in range(n):
        visited_list = [0] * n
        visited.append(visited_list)

    # 라벨링하기 (2부터)
    label = 2
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                label_bfs(i, j)
                label += 1

    # visited 초기화
    visited = []
    for i in range(n):
        visited_list = [0] * n
        visited.append(visited_list)

    # 최단거리 찾기
    min_result = 1000
    for i in range(2, label):
        min_result = min(bfs(i), min_result)
        # visited 초기화
        visited = []
        for i in range(n):
            visited_list = [0] * n
            visited.append(visited_list)

    print(min_result)
