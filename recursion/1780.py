# 종이의 개수
"""
구역:
1 2 3
4 5 6
7 8 9
"""
n = int(input())
cnt_0 = 0
cnt_1 = 0
cnt_1_1 = 0 # -1
board = []

for i in range(n):
    color = list(map(int, input().split()))
    board.append(color)

def func(x, y, n):
    global cnt_1, cnt_0, cnt_1_1
    color = board[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색상이 같지 않다면
            if color != board[i][j]:
                # 1구역
                func(x, y, n // 3)
                # 2구역
                func(x, y + n // 3, n // 3)
                # 3구역
                func(x, y + 2 * n // 3, n // 3)
                # 4구역
                func(x + n // 3, y, n // 3)
                # 5구역
                func(x + n // 3, y + n // 3, n // 3)
                # 6구역
                func(x + n // 3, y + 2 * n // 3, n // 3)
                # 7구역
                func(x + 2 * n // 3, y, n // 3)
                # 8구역
                func(x + 2 * n // 3, y + n // 3, n // 3)
                # 9구역
                func(x + 2 * n // 3, y + 2 * n // 3, n // 3)
                return
                
    # 색상이 같다면 cnt + 1
    if color == 0:
        cnt_0 += 1
    elif color == 1:
        cnt_1 += 1
    else:
        cnt_1_1 += 1

    return
            
func(0, 0, n)
print(cnt_1_1)
print(cnt_0)
print(cnt_1)
