# 2048 (Easy) - dfs
import copy
def dfs(cnt, board):
    global max_value 
    # 최댓값 갱신
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                max_value = max(max_value, board[i][j])
        return

    # 동서남북 이동   
    # 원본 저장
    copy_board = copy.deepcopy(board)
    for i in range(4):
        new_board = move(board, i)
        dfs(cnt + 1, new_board)
        # 이전 상태 되돌리기
        board = copy.deepcopy(copy_board)

print(max_value)

    