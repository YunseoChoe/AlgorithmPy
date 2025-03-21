# 쿼드트리
n = int(input())
board = []

for i in range(n):
    color = list(input())
    # 정수화
    for j in range(len(color)):
        color[j] = int(color[j])
    board.append(color)

def func(x, y, n):
    color = board[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                # 1구역
                print("(", end = "")
                func(x, y, n // 2)
                # 2구역
                func(x, y + n // 2, n // 2)
                # 3구역
                func(x + n // 2, y, n // 2)
                # 4구역
                func(x + n // 2, y + n // 2, n // 2)
                print(")", end = "")
                return # return을 해야 중복 카운팅을 막을 수 있음.
    
    # return되지 않은 경우 (즉 색깔이 모두 같을 때만 도달함.)
    print(color, end = "")

func(0, 0, n)
