# 토마토
m, n, h = input().split()
m = int(m) # 가로 칸
n = int(n) # 세로 칸
h = int(h) # 상자의 수

# 그래프 초기화
graph = []
for i in range(h):
    graph_list = []
    for j in range(n):
        list = []
        for k in range(m):
            list.append(0)
        graph_list.append(list)
    graph.append(graph_list)

print(graph)

# 방문 배열 초기화
visited = []
for i in range(h):
    visited_list = []
    for j in range(n):
        list = [False] * m
        visited_list.append(list)
    visited.append(visited_list)

print(visited)

# 입력 받기
for i in range(h):
    for j in range(n):
        num = input().split(' ')
        # 정수화
        for k in range(m):
            num[k] = int(num[k])
        graph[i][j][k] = 
            
print(graph)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(graph):
    queue = []
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = 1
    while queue:
        x, y, z = queue.pop()
        for i in range(6):
            next_x = dx[i] + x
            next_y = dy[i] + y
            next_z = dz[i] + z
            if 0 <= next_x < m and 0 <= next_y < n and 0 <= next_z < h:
                if visited[next_x][next_y][next_z] == 0 and graph[next_x][next_y][next_z] == 0:
                    queue.append((next_x, next_y, next_z))
                    graph[next_x][next_y][next_z] += 1
                    visited[next_x][next_y][next_z] = 1

bfs(graph)

is_done = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                is_done = 0

print(is_done)
