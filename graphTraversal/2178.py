# 미로 탐색
n, m = list(map(int, input().split()))
miro = []

for i in range(n):
    num = list(input())
    for j in range(len(num)):
        num[j] = int(num[j])
    miro.append(num)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []
def bfs(start_x, start_y):
    queue.append((start_x, start_y))
 
    while len(queue) != 0:
        start_x, start_y = queue.pop(0)
        for i in range(4):
            x = start_x + dx[i]
            y = start_y + dy[i]

            if 0 <= x < n and 0 <= y < m and miro[x][y] == 1:
                miro[x][y] = miro[start_x][start_y] + 1
                queue.append((x, y))

    return miro[n - 1][m - 1]
    
print(bfs(0, 0))
