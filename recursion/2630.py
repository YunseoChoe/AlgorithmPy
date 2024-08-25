# 색종이 만들기
n = int(input())
board = []
white_cnt = 0
blue_cnt = 0

for i in range(n):
    color = list(map(int, input().split()))
    board.append(color)

def func(x, y, n):
    global white_cnt, blue_cnt
    color = board[x][y]
    
    # 색상 검사
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                # 모든 색상이 같지 않다면
                func(x, y, n // 2)                      # 1사분면
                func(x, y + n // 2, n // 2)             # 2사분면
                func(x + n // 2, y, n // 2)             # 3사분면
                func(x + n // 2, y + n // 2, n // 2)    # 4사분면
                return()

    # 모든 색상이 같다면
    # 흰색이라면
    if color == 0:
        white_cnt += 1
    # 검은색이라면
    else:
        blue_cnt += 1

func(0, 0, n)
print(white_cnt)
print(blue_cnt)
