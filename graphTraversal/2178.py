# 미로 탐색
n, m = input().split()
n = int(n)
m = int(m)

miro = []
for i in range(n):
    num = list(input())
    for j in range(len(num)):
        num[j] = int(num[j])
    miro.append(num)

dx = [-1, 1, 0, 0] # 상하좌우 좌표
dy = [0, 0, -1, 1]

def bfs(start): # 시작 좌표
    queue = []
    queue.append(start) 

    while not len(queue) == 0:
        x, y = queue.pop(0)
        for i in range(4):
            x_1 = x + dx[i]
            y_1 = y + dy[i]
         
            if 0 <= x_1 < n and 0 <= y_1 < m and miro[x_1][y_1] == 1: 
                # if dx[i] == -1 and dy[i] == 0:
                #     print("상")
                # elif dx[i] == 1 and dy[i] == 0:
                #     print("하")
                # elif dx[i] == 0 and dy[i] == -1:
                #     print("좌")
                # elif dx[i] == 0 and dy[i] == 1:
                #     print("우")
                
                miro[x_1][y_1] = miro[x][y] + 1
                queue.append((x_1, y_1))
    
    return miro[n - 1][m - 1]

return_value = bfs((0,0))
print(return_value)