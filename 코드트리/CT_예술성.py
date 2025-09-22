# 예술성
def get_contact_cnt(g1, g2, board, n):
    """
    g1(int), g2(int) 그룹끼리 맞닿아 있는 변의 수 구하기
    """
    contact_cnt = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(n):
            # g1, g2에 속한 칸만 확인
            if board[i][j] != g1 and board[i][j] != g2:
                continue
            # 동서남북
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
    해당 group(int)에 속한 칸의 수를 반환
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

def divide_group(nums, start, path, result):
    if len(path) == 2:
        result.append(tuple(path))
        return
    
    for i in range(start, len(nums)):
        divide_group(nums, i + 1, path + [nums[i]], result)

def get_unique_numbers(board):
    unique_nums = set()
    for row in board:
        unique_nums.update(row)  # 각 행의 숫자를 바로 set에 추가
    return sorted(unique_nums)
    
def calculate_art_score(board, n):
    """
    예술 점수(조화로움의 합) 계산
    (a 그룹에 속한 칸의 수 + b 그룹에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수 (항상 1임)
    반환: 계산된 총 예술 점수

    """
    total_score = 0
    # 그룹 나누기 (g1, g2) -> 조합 (백트래킹)

    # 2차원 board에서 중복 제거된 숫자만 뽑기
    unique_nums = get_unique_numbers(board)

    # 그룹 나누기
    indexs = []
    divide_group(unique_nums, 0, [], indexs)

    print(f'그룹핑된 그룹 출력: {indexs}') # indexs = [(1, 2), (1, 3), (2, 3)]

    # 그룹 별로 total_score 구하기
    for index in indexs:
        group_a = index[0]
        group_b = index[1]

        # a그룹에 속한 칸의 수
        group_a_score = get_all_cnt_by_group(group_a, board, n)
        # b그룹에 속한 칸의 수
        group_b_score = get_all_cnt_by_group(group_b, board, n)
        # 맞닿아 있는 변의 수 구하기
        contact_socre = get_contact_cnt(group_a, group_b, board, n)   
        
        total_score += (group_a_score + group_b_score) * group_a * group_b * contact_socre

    return total_score

def rotate(board, n):
    """
    정중앙을 기준으로 두 선을 그어 만들어지는 십자 모양과 그 외 부분 회전
    """
    # 정중앙 위치 구하기
    center = n // 2
    rotated_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 센터 영역이면
            if i == center or j == center:
                # 시계 방향 90도 회전
                rotated_board[j][n - 1 - i] = board[i][j]
            # 나머지 영역이면
            else:
                # 반시계 방향 90도 회전
                rotated_board[n - 1 - j][i] = board[i][j]
    
    return rotated_board

def main():
    board = []
    n = int(input())
    for _ in range(n):
        # 색깔 정보 입력 (1 ~ 10)
        input_list = list(map(int, input().split(" ")))
        board.append(input_list)

    # 초기 예술 점수 구하기
    early_score = calculate_art_score(board, n)

    # 1회전 예술 점수 구하기
    board = rotate(board, n)
    first_rotation_score = calculate_art_score(board, n)

    # 2회전 예술 점수 구하기
    board = rotate(board, n)
    second_rotation_score = calculate_art_score(board, n)

    # 3회전 예술 점수 구하기
    board = rotate(board, n)
    third_rotation_score = calculate_art_score(board, n)
    
    print(early_score + first_rotation_score + second_rotation_score + third_rotation_score)

if __name__ == "__main__":
    main()
