def get_contact_cnt(g1, g2, board, n):
    """
    g1, g2 그룹끼리 맞닿아 있는 변의 수 구하기
    """
    contact_cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            # g1, g2에 속한 칸만 확인
            if board[i][j] != g1 and board[i][j] != g2:
                continue
            
            for k in range(4):
                nr = i + dx[k]
                nc = j + dy[k]

                if not in_range(nr, nc, n):
                    continue

                if board[i][j] == g1:
                    if board[nr][nc] == g2:
                        contact_cnt += 1
                elif board[i][j] == g2:
                    if board[nr][nc] == g1:
                        contact_cnt += 1

    return contact_cnt // 2  # 중복 제거

def get_all_cnt_by_group(group, board, n):
    """
    해당 group에 속한 칸의 수를 반환
    """
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == group:
                cnt += 1
    return cnt

def in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def make_group(start, path, result, n):
    """
    백트래킹을 사용해서 2개의 그룹 조합 생성
    """
    if len(path) == 2:
        result.append(tuple(path))
        return
    
    for i in range(start, n):
        make_group(i + 1, )
    


def calculate_art_score(board):
    """
    예술 점수(조화로움의 합) 계산
    (a 그룹에 속한 칸의 수 + b 그룹에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수 (항상 1임)
    반환: 계산된 총 예술 점수

    """
    total_score = 0
    # 그룹 나누기 (g1, g2) -> 조합 (백트래킹)
    
    indexs = []
    make_group(0, [], indexs) # indexs = [(1, 2), (1, 3), (2, 3)]

    # 그룹 별로 total_score 구하기
    for index in indexs:
        group_a = index[0]
        group_b = index[1]

        # 1. a그룹에 속한 칸의 수
        total_score += get_all_cnt_by_group(group_a)
    
        # 2. b그룹에 속한 칸의 수
        total_score += get_all_cnt_by_group(group_b)

        # 3. a그룹을 이루고 있는 숫자 값
        total_score += group_a

        # 4. b그룹을 이루고 있는 숫자 값
        total_score += group_b
        
        # 5. 맞닿아 있는 변의 수 구하기
        total_score += get_contact_cnt(group_a, group_b, board)    
    return total_score

def rot90(group, board, clockwise=True):
    """
    시계/반시계 방향으로 90도 회전 (True: 시계방향, False: 반시계방향)
    반환값: 회전된 board
    """
    rotated_board = []

    return rotated_board


def rotate(board, n):
    """
    정중앙을 기준으로 두 선을 그어 만들어지는 십자 모양과 그 외 부분으로 나뉘어 진행됨
    """
    # 십자 모양으로 나누기
    # 정중앙 위치 구하기
    center_r, center_c = n // 2, n // 2 # n은 무조건 홀수

    cross_group = []
    not_cross_group = []
    for row in range(n):
        for col in range(n):
            # 십자 모양이면
            if row == center_r or col == center_c:
                cross_group.append(board[row][col])
            # 십자 모양이 아니면
            else:
                not_cross_group.append(board[row][col])

    # 십자 모양 반시계 방향 90도 회전
    board = rot90(cross_group, board, False)
    # 십자 모양을 제외한 나머지 시계 방향 90도 회전
    board = rot90(not_cross_group, board, True)
    return board

def main():
    board = []
    n = int(input())
    for _ in range(n):
        # 색깔 정보 입력 (1 ~ 10)
        list = list(map(int, input().split(" ")))
        board.append(list)

    # 초기 예술 점수 구하기
    early_score = calculate_art_score(board)
    
    # 1회전 예술 점수 구하기
    board = rotate(board, n)
    first_rotation_score = calculate_art_score(board)

    # 2회전 예술 점수 구하기
    board = rotate(board, n)
    second_rotation_score = calculate_art_score(board)

    # 3회전 예술 점수 구하기
    board = rotate(board, n)
    third_rotation_score = calculate_art_score(board)
    
    print(early_score + first_rotation_score + second_rotation_score + third_rotation_score)

if __name__ == "__main__":
    main()
