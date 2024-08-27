# N-Queen
n = int(input())
cnt = 0

# chess 초기화
chess = []
for i in range(n):
    col = []
    for j in range(n):
        col.append(0)
    chess.append(col)

# 가로, 세로, 대각선이 모두 0인지 확인하는 함수
def no_issue(row, col):
    real_row = row
    real_col = col

    # 가로, 세로
    for i in range(n):
        if chess[row][i] == 1:
            return False
        elif chess[i][col] == 1:
            return False

    # 왼쪽 대각선 /
    while 0 <= row < n and 0 <= col < n: # 위쪽
        if chess[row][col] == 1:
            return False
        row -= 1
        col += 1

    # 원상 복귀
    row = real_row
    col = real_col

    while 0 <= row < n and 0 <= col < n: # 아래쪽
        if chess[row][col] == 1:
            return False
        row += 1
        col -= 1

    # 원상 복귀
    row = real_row
    col = real_col

    # 오른쪽 대각선 \
    while 0 <= row < n and 0 <= col < n: # 위쪽
        if chess[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # 원상 복귀
    row = real_row
    col = real_col

    while 0 <= row < n and 0 <= col < n: # 아래쪽
        if chess[row][col] == 1:
            return False
        row += 1
        col += 1

    return True

cnt = 0
def nqueen(row): # 행
    global cnt
    if row == n: # 행을 다 봤으면
        cnt += 1
        return
    
    for col in range(n): # 열
        if no_issue(row, col): # 가로, 세로, 대각선이 모두 0이면 놓을 수 있음
            chess[row][col] = 1
            nqueen(row + 1)
            chess[row][col] = 0 # 백트래킹

nqueen(0)
print(cnt)
