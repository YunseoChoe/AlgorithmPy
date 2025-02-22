# 구슬탈출
from collections import deque

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 구슬 움직이는 함수 
def move(x, y, dir):
    nx, ny = x, y
    cnt = 0  
    
    # 벽이 아니고, 구멍이 아닐 때까지 이동
    while graph[nx + dx[dir]][ny + dy[dir]] != '#' and graph[nx][ny] != 'O':
        nx += dx[dir]
        ny += dy[dir]
        cnt += 1

    return nx, ny, cnt

def bfs(start_red_x, start_red_y, start_blue_x, start_blue_y):
    q = deque()
    q.append((start_red_x, start_red_y, start_blue_x, start_blue_y, 0))

    while q:
        red_x, red_y, blue_x, blue_y, count = q.popleft()
        # 10번 이상되면 종료
        if count > 10:
            return 0

        # 구슬 이동
        for i in range(4):
            # 새로운 x, 새로운 y, 벽과의 거리
            rnx, rny, rcnt = move(red_x, red_y, i) 
            bnx, bny, bcnt = move(blue_x, blue_y, i)

            # 파란공이 구멍에 들어갔을 경우
            if graph[bnx][bny] == 'O':
                return 0

            # 파란공이 구멍에 안 들어갔을 경우
            if graph[bnx][bny] != 'O':
                # 빨간공이 구멍에 들어갔을 경우
                if graph[rnx][rny] == 'O':
                    return 1
                # 빨간공과 파란공 위치가 같을 경우
                if rnx == bnx and rny == bny:
                    # 동
                    if dir == 0:
                        if rcnt < bcnt:
                            bny -= 1
                        else:
                            rny -= 1
                    # 서
                    elif dir == 1:
                        if rcnt < bcnt:
                            bny += 1
                        else:
                            rny += 1
                    # 남
                    elif dir == 2:
                        if rcnt < bcnt:
                            bnx -= 1
                        else:
                            rnx -= 1
                    # 북
                    else:
                        if rcnt < bcnt:
                            bnx += 1
                        else:
                            rnx += 1
  
                # 만약 방문하지 않았다면 
                if (rnx, rny, bnx, bny) not in visited:
                    # 방문처리
                    visited.append((rnx, rny, bnx, bny))      
                    # Q에 넣기
                    q.append((rnx, rny, bnx, bny, count + 1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph_list = list(input())
        graph.append(graph_list)

    # 방문배열 초기화 
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
    print(bfs(start_red_x, start_red_y, start_blue_x, start_blue_y))
