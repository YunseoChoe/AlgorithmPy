# 탈출
r, c = map(int, input().split())
routes = []
for i in range(r):
    route = list(input()) 
    routes.append(route)

dx = [-1, 1, 0, 1]
dy = [0, 0, -1, 1]

def bfs(start):
    water_queue = [] # 물 
    s_queue = [] # 고슴도치
    s_queue.append(start)

    # 물 위치 queue에 넣기
    for i in range(len(routes)):
        for j in range(len(routes[0])):
            if routes[i][j] == '*':
                water_queue.append((i, j))

    while not len(s_queue) == 0:
        s_x, s_y = s_queue.pop(0) # 고슴도치 좌표
        water_x, water_y = water_queue.pop(0) # 물 좌표

        for i in range(4):
            s_x_1 = s_x + dx[i]
            s_y_1 = s_y + dy[i]

            water_x_1 = water_x + dx[i]
            water_y_1 = water_y + dy[i]

            # 물 좌표 이동
            if 0 <= water_x_1 < r and 0 <= water_y_1 < c: 
                # 만약 비어있다면 물로 채우기
                if routes[water_x_1][water_y_1] == '.':
                    routes[water_x_1][water_y_1] = '*' 
                    water_queue.append((water_x_1, water_y_1))

                # 돌을 만났을 때
                elif routes[water_x_1][water_y_1] == 'X':
                    pass

            # 고슴도치 좌표 이동
            if 0 <= s_x_1 < r and 0 <= s_y_1 < c:
                # 만약 비어있다면 고슴도치 이동
                if routes[s_x_1][s_y_1] == '.':
                    routes[s_x_1][s_y_1] = 'S'
                    routes[s_x][s_y] = '.' # 전 좌표 비우기
                    s_queue.append((s_x_1, s_y_1))

                # 돌을 만났을 때
                elif routes[s_x_1][s_y_1] == 'X':
                    pass

                # 굴을 만났을 때
                elif routes[s_x_1][s_y_1] == 'D':
                    return True
    
    return False

# 맨 처음 S의 좌표 찾기
s_x = 0
s_y = 0
for i in range(len(routes)):
    for j in range(len(routes[0])):
        if routes[i][j] == 'S':
            s_x = i
            s_y = j

return_value = bfs((s_x, s_y))
print(return_value)