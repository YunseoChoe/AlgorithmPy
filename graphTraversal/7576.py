# 토마토
from collections import deque

m, n = input().split()
m = int(m)
n = int(n)
tomatos = []
for i in range(n):
    num = map(int, input().split())
    num = list(num)
    tomatos.append(num)

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

def bfs():
    global tomatos
    # queue = []
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 1:
                queue.append((i, j))
                
    while not len(queue) == 0:
        x, y = queue.popleft()
        for i in range(4):
            x_1 = x + dx[i]
            y_1 = y + dy[i]

            if 0 <= x_1 < n and 0 <= y_1 < m and tomatos[x_1][y_1] == 0:
                tomatos[x_1][y_1] = tomatos[x][y] + 1
                queue.append((x_1, y_1))

bfs()

is_zero = False
max = -1
# tomatos에 0이 1개라도 있으면 -1
for i in range(len(tomatos)):
    for j in range(len(tomatos[0])):
        if max < tomatos[i][j]:
            max = tomatos[i][j]
        if tomatos[i][j] == 0:
            is_zero = True

if is_zero:
    print(-1)
else:
    print(max - 1)
