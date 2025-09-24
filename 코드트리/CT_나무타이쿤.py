import copy
DIRS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)] # 1, 2, 3, 4, 5, 6, 7, 8

def in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def move_supplement(d, p, supplements, n):
    """
    dir: 이동 방향, cnt: 이동 횟수
    특수 영양제를 이동시킴
    격자 바깥으로 나가면 반대편으로 돌아옴
    반환값: 이동된 supplements
    """
    new_supplements = []
    for i in range(len(supplements)):
        cx, cy = supplements[i]
        # 이동
        nx = (cx + DIRS[d][0] * p) % n
        ny = (cy + DIRS[d][1] * p) % n

        new_supplements.append((nx, ny))
    
    return new_supplements


def growup(moved_supplements, board, n):
    """
    이동된 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
    + 대각선으로 인접한 높이 1이상의 리브로수의 개수만큼 높이 증가
    반환값: grow_board
    """
    grow_board = copy.deepcopy(board)
    diagonal_dirs = [DIRS[1], DIRS[3], DIRS[5], DIRS[7]] # 대각선 방향만 뽑음.

    # 높이 1 증가
    for i in range(len(moved_supplements)):
        grow_board[moved_supplements[i][0]][moved_supplements[i][1]] += 1

    # 대각선으로 인접한 높이 1이상의 리브로수의 개수만큼 증가
    for i in range(len(moved_supplements)):
        cnt = 0
        cx = moved_supplements[i][0]
        cy = moved_supplements[i][1]
        # 대각선
        for j in range(4):
            nx = cx + diagonal_dirs[j][0]
            ny = cy + diagonal_dirs[j][1]
            # 대각선의 값의 인덱스 범위가 맞지 않거나, 높이가 1보다 작으면 (높이 1증가 후, 증가시켜야하므로 grow_board[][]로 접근해야 함.)
            if not in_range(nx, ny, n) or grow_board[nx][ny] < 1:
                continue
            
            cnt += 1

        grow_board[cx][cy] += cnt

    return grow_board

def put(moved_supplements, board, n):
    """
    해당 특수 영양제를 맞은 땅을 제외하고 높이가 2이상인 리브로수를 높이 2만큼 날라냄 
    + 해당 땅 위에 특수 영양제를 올려줌
    반환: cut_board, 재배치된 특수 영양제 위치
    """
    replaced_supplements = []
    cut_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):  
            # moved_supplements에 해당하는 곳이면 제외
            if (i, j) in moved_supplements:
                continue
            if board[i][j] >= 2:
                cut_board[i][j] -= 2
                # 해당 땅 위에 특수 영양제 올려줌
                replaced_supplements.append((i, j))

    return cut_board, replaced_supplements

def main():
    n, m = map(int, input().split()) # 격자 크기, 리브로수를 키우는 총 년 수

    board = []
    supplements = [(n - 2, 0), (n - 1, 0), (n - 2, 1), (n - 1, 1)] # 초기 특수 영양제 위치 (2x2)
    
    for _ in range(n):
        board_list = list(map(int, input().split()))
        board.append(board_list)

    for _ in range(m): # 총 m년마다 반복
        d, p = map(int, input().split()) # 이동 방향, 이동 칸 수
        
        # 특수 영양제 이동
        supplements = move_supplement(d - 1, p, supplements, n) # d가 아닌 d - 1로

        # 리브로수의 성장
        board = growup(supplements, board, n) # board 재정의

        # 특수 영양제 투입
        board, supplements = put(supplements, board, n)

    # 남아있는 리브로수의 총 높이의 합
    total_height = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                total_height += board[i][j]

    print(total_height)

if __name__ == "__main__":
    main()
