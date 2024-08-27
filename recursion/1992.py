# 쿼드트리
n = int(input())
board = []
cnt_0 = 0
cnt_1 = 0

for i in range(n):
    color = list(input())
    # 정수화
    for j in range(len(color)):
        color[j] = int(color[j])
    board.append(color)

def func(x, y, n):
    global cnt_0, cnt_1
    color = board[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                new_n = n // 2
                # 1구역
                print("(", end = "")
                func(x, y, new_n)
                # print(")")
                # 2구역
                # print("(")
                func(x, y + new_n, new_n)
                # print(")")
                # 3구역
                # print("(")
                func(x + new_n, y, new_n)
                # print(")")
                # 4구역
                # print("(")
                func(x + new_n, y + new_n, new_n)
                print(")", end = "")
                return
    
    
    print(color, end = "")

func(0, 0, n)
