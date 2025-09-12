board = [[1, 2, 3],
         [4, 5 ,6],
         [7, 8, 9]]

# 90도 시계 방향 회전 (3x3)
def rotate90Clockwise(board):
    rotated_board = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rotated_board[j][2 - i] = board[i][j]
    return rotated_board
            
# 90도 반시계 방향 회전 (3x3)
def rotate90CounterClockwise(board):
    rotated_board = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rotated_board[2 - j][i] = board[i][j]
    return rotated_board

def main():
    print(f'시계방향 90도 회전 결과: {rotate90Clockwise(board)}')
    print(f'반시계방향 90도 회전 결과: {rotate90CounterClockwise(board)}')

if __name__ == "__main__":
    main()
