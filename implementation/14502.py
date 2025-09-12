# 연구소
# 1. 벽 3개를 세울 수 있는 모든 경우의 수
# 2. 각각의 경우에 virus를 퍼뜨리기
# 3. 안전 영역 -> 최댓값 구하기
import sys, copy
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_area = 0
# virus 퍼뜨리는 함수 (bfs)
def virus(board, safe_area_count):
    global max_area
    temp_board = copy.deepcopy(board) # board값 복사
    
    q = deque()
    # 바이러스 좌표 q에 넣기
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()

        # 동서남북
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 빈 칸이면
                if temp_board[nx][ny] == 0:
                    temp_board[nx][ny] = 2
                    q.append((nx, ny))

    # 안전 영역 세기
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 0:
                safe_area_count += 1
    # 최댓값 갱신
    if max_area < safe_area_count:
        max_area = safe_area_count

# (중복없이) 벽 세우는 함수 -> 완전 탐색
def createWall(count):
    # 벽이 이미 3개라면
    if count == 3:
        virus(board, 0) # 바이러스 퍼뜨리기
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                createWall(count + 1)
                board[i][j] = 0 # 백트래킹

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board_list = list(map(int, input().strip().split()))
        board.append(board_list)

    # 벽 세우기
    createWall(0)

    # 최대 안전 영역 출력
    print(max_area)
