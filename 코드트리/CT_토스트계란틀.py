from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def range_l_r(board, cx, cy, nx, ny, L, R):
    return L <= abs(board[cx][cy] - board[nx][ny]) <= R


def separate(n, board, L, R):
    is_move = False
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 방문하지 않았으면
            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                groups = [(i, j)]

                while q:
                    cx, cy = q.popleft()
                    # 동서남북
                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy
                        if in_range(nx, ny, n) and not visited[nx][ny]:
                            # l <= <= r
                            if range_l_r(board, cx, cy, nx, ny, L, R):
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                groups.append((nx, ny))

                # 그룹을 구한 후.
                if len(groups) > 1:
                    sum = 0
                    is_move = True
                    # 각 그룹의 합 구하기
                    for x, y in groups:
                        sum += board[x][y]

                    # 그룹값 갱신
                    for x, y in groups:
                        board[x][y] = sum // len(groups)

    return is_move
        
def main():
    n, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    move_count = 0
    # 계란이 움직일 동안 반복.
    while True:
        is_move = separate(n, board, L, R)
        if is_move:
            move_count += 1
        else:
            break

    print(move_count)

if __name__ == "__main__":
    main()
