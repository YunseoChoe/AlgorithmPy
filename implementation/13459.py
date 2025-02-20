# 구슬탈출
from collections import deque

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 구슬 움직이는 함수 
def move(x, y, dx, dy):
    is_hall = False
    # 동
    if dx == 0 and dy == 1:
        wall_distance = (m - 1) - y
        while True:
            # 만약 벽이 아니면 이동
            if graph[x][y + 1] == '#':
                break
            # 만약 구멍이면
            elif graph[x][y + 1] == 'O':
                is_hall = True
                y += 1
                break
            y += 1 # 이동
            
    # 서
    elif dx == 0 and dy == (-1):
        wall_distance = y
        while True:
            if graph[x][y - 1] == '#':
                break
            elif graph[x][y - 1] == 'O':
                is_hall = True
                y -= 1
                break
            y -= 1
    # 남
    elif dx == 1 and dy == 0:
        wall_distance = (n - 1) - x
        while True:
            if graph[x + 1][y] == '#':
                break
            elif graph[x + 1][y] == 'O':
                is_hall = True
                x += 1
                break
            x += 1
    # 북
    elif dx == (-1) and dy == 0:
        wall_distance = x
        while True:
            if graph[x - 1][y] == '#':
                break
            elif graph[x - 1][y] == 'O':
                is_hall = True
                x -= 1
                break
            x -= 1

    return x, y, wall_distance, is_hall

def bfs(start_red_x, start_red_y, start_blue_x, start_blue_y):
    q = deque()
    q.append((start_red_x, start_red_y, start_blue_x, start_blue_y, 0))

    while q:
        red_x, red_y, blue_x, blue_y, count = q.popleft()
        # 10번 이상되면 종료
        if count > 10:
            break

        # 구슬 이동
        for i in range(4):
            # 새로운 x, 새로운 y, 벽과의 거리
            red_nx, red_ny, red_distance, red_is_hall = move(red_x, red_y, dx[i], dy[i]) 
            blue_nx, blue_ny, blue_distance, blue_is_hall = move(blue_x, blue_y, dx[i], dy[i])

            # 파란색이 구멍에 들어갔을 경우 종료
            if blue_is_hall:
                print(0)
                break 

            # 빨간색이 구멍에 들어갔을 경우
            if red_is_hall:
                print(1)
                break

            # 빨간색이 구멍에 들어가지 않았을 경우 
            else:
                # 만약 red랑 blue가 같은 위치에 있다면 이동 금지
                if red_nx == blue_nx and red_ny == blue_ny:
                    # 빨간공이 더 벽과 가깝다면
                    if red_distance < blue_distance:
                        # 동
                        if dx[i] == 0 and dy[i] == 1:
                            blue_ny -= 1
                        # 서
                        elif dx[i] == 0 and dy[i] == -1:
                            blue_ny += 1
                        # 남
                        elif dx[i] == 1 and dy[i] == 0:
                            blue_nx -= 1
                        # 북
                        else:
                            blue_nx += 1
                    # 파란공이 더 벽과 가깝다면
                    else:
                        # 동
                        if dx[i] == 0 and dy[i] == 1:
                            red_ny -= 1
                        # 서
                        elif dx[i] == 0 and dy[i] == -1:
                            red_ny += 1
                        # 남
                        elif dx[i] == 1 and dy[i] == 0:
                            red_nx -= 1
                        # 북
                        else:
                            red_nx += 1
                q.append((red_nx, red_ny, blue_nx, blue_ny, count + 1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph_list = list(input())
        graph.append(graph_list)

    visited = [] 

    # 시작 red, blue 위치 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'B':
                start_blue_x = i
                start_blue_y = j
            elif graph[i][j] == 'R':
                start_red_x = i
                start_red_y = j


    bfs(start_red_x, start_red_y, start_blue_x, start_blue_y)
