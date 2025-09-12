# 구슬 탈출2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 구슬 이동하는 함수
def move(x, y, dir):
    cnt = 0
    # 벽이 아니고 구멍이 아닐 때 까지
    while graph[x + dx[dir]][y + dy[dir]] != '#' and graph[x][y] != 'O':
        cnt += 1
        x += dx[dir]
        y += dy[dir]

    return x, y, cnt

def bfs(start_rx, start_ry, start_bx, start_by):
    q.append((start_rx, start_ry, start_bx, start_by, 0))
    visited.append((start_rx, start_ry, start_bx, start_by))

    while q:
        # 이동
        rx, ry, bx, by, cnt = q.popleft()
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)

            if cnt >= 10:
                print(-1)
                return

            # 파란공이 구멍에 안 들어갔을 경우
            if graph[nbx][nby] != 'O':
                # 빨간공이 구멍에 들어갔을 경우
                if graph[nrx][nry] == 'O':
                    print(cnt)
                    return
                # 빨간공과 파란공 위치가 같을 경우
                if nrx == nbx and nry == nby:
                    # 빨간색이 벽쪽일 경우
                    if rcnt < bcnt:
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dx[i]
                # 빨간공이 구멍에 안 들어간 경우
                if graph[nrx][nry] != 'O':
                    # 방문하지 않았다면
                    if (nrx, nry, nbx, nby) not in visited:
                        q.append((nrx, nry, nbx, nby, cnt + 1))
                        visited.append((nrx, nry, nbx, nby))





