# N-Queen
import sys

n = int(sys.stdin.readline())
chess = [0 for _ in range(n)]
cnt = 0

# 가로, 세로, 대각선이 모두 0인지 확인하는 함수
def no_issue(row):
    for i in range(row):
        if chess[row] == chess[i] or abs(i - row) == abs(chess[i] - chess[row]):
            return False
    return True

cnt = 0
def nqueen(row): # 행
    global cnt
    if row == n: # 행을 다 봤으면
        cnt += 1
        return
    
    for col in range(n): # 열
        chess[row] = col
        if no_issue(row): # 가로, 세로, 대각선이 모두 0이면 놓을 수 있음
            nqueen(row + 1)

nqueen(0)
print(cnt)
