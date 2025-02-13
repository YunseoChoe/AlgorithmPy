# 구슬탈출
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def move():
    pass

q = deque()
# 구슬 탈출
while not q.empty():
    red_x, red_y, blue_x, blue_y, count = q.popleft()
    if count > 10:
        break
    for i in range(4):
        red_nx, red_ny, _ = move(red_x, red_y, dx[i], dy[i])
        blue_nx, blue_ny, _ = move(blue_x, blue_y, dx[i], dy[i])
        # 구멍인지 확인
        if graph[blue_nx][blue_ny] != 'O':
            if graph[red_nx][red_ny] == 'O':
                return ok
            # ...
            # TODO: red랑 blue가 같은 위치에 있지 않도록 조정
            
            # 빨간색이 구멍에 들어가지 않았을 경우
            q.append((red_nx, red_ny, blue_nx, blue_ny, count + 1))

