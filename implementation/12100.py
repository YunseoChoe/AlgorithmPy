# 2048 (Easy)
import sys, copy
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 이동하는 함수
def move(board, dir):
    new_board = copy.deepcopy(board)
    # 동
    if dir == 0:
        for i in range(n): # 행마다 이동시키기
            edge = n - 1
            for j in range(n - 2, -1, -1):
                if new_board[i][j] != 0:
                    tmp = new_board[i][j]
                    # edge가 비어 있으면
                    if new_board[i][edge] == 0:
                        new_board[i][edge] = tmp
                        new_board[i][j] = 0
                    # edge가 tmp랑 같은 숫자일 때
                    elif new_board[i][edge] == tmp:
                        new_board[i][edge] += tmp
                        new_board[i][j] = 0
                        edge -= 1
                    # edge가 tmp랑 다른 숫자일 때
                    else:
                        edge -= 1
                        new_board[i][edge] = tmp
    # 서
    elif dir == 1:
        for i in range(n):
            edge = 0
            for j in range(1, n):
                if new_board[i][j] != 0:
                    tmp = new_board[i][j]
                    if new_board[i][edge] == 0:
                        new_board[i][edge] = tmp
                        new_board[i][j] = 0
                    elif new_board[i][edge] == tmp:
                        new_board[i][edge] += tmp
                        new_board[i][j] = 0
                        edge += 1
                    else:
                        edge += 1
                        new_board[i][edge] = tmp 

    # 남
    elif dir == 2:
        for i in range(n):
            edge = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = new_board[i][j]
                    if new_board[i][edge] == 0:
                        new_board[i][edge] = tmp
                        new_board[i][j] = 0
                    elif new_board[i][edge] == tmp:
                        new_board[i][edge] += tmp
                        new_board[i][j] = 0
                        edge  -= 1
                    else:
                        edge -= 1
                        new_board[i][edge] = tmp  
    # 북
    else:
        for i in range(n):
            edge = 0
            for j in range(1, n):
                if new_board[i][j] != 0:
                    tmp = new_board[i][j]
                    if new_board[i][edge] == 0:
                        new_board[i][edge] = tmp
                        new_board[i][j] = 0
                    elif new_board[i][edge] == tmp:
                        new_board[i][edge] += tmp
                        new_board[i][j] = 0
                        edge += 1
                    else:
                        edge += 1
                        new_board[i][edge] = tmp
    return new_board

def bfs(start_board, cnt):
    q = deque()
    q.append((start_board, 0))
    max_value = 1
    
    while q:
        cur_board, cnt = q.popleft()
        
        # 종료 조건
        if cnt == 5:
            # 최댓값 갱신
            for i in range(n):
                for j in range(n):
                    max_value = max(max_value, board[i][j])

        # 동서남북 이동
        for i in range(4):
            new_board = move(board, i)
            # board의 변화가 있는 경우에만 q에 넣기..?
            if cur_board != new_board:
                q.append((new_board, cnt + 1))

    return max_value

if __name__ == '__main__':
    board = []
    n = int(input())
    for i in range(n):
        board.append(list(map(int, input().split())))

    # 처음 cnt는 0부터 시작
    print(bfs(board, 0))
