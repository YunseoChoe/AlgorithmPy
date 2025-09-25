from collections import deque

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def rotate(board, n):
    """
    예술 점수 문제 회전 함수
    중앙 십자가는 반시계 방향 90도 회전
    나머지 4개 정사각형 구역은 시계 방향 90도 회전
    """
    new_board = [[0] * n for _ in range(n)]
    center = n // 2

    # 십자가 모양이면 반시계 방향 회전
    # 열 -> 행
    for i in range(n):
        new_board[center][i] = board[i][center]
    # 행 -> 열 (거꾸로)
    for i in range(n):
        new_board[i][center] = board[center][n - 1 - i]

    # 4개의 정사각형 시계 방향 회전
    def rotate_square(sx, sy, center):
        for i in range(center):
            for j in range(center):
                new_board[sx + j][sy + center - 1 - i] = board[sx + i][sy + j]

    # 좌상
    rotate_square(0, 0, center)
    # 우상
    rotate_square(0, center + 1, center)
    # 좌하
    rotate_square(center + 1, 0, center)
    # 우하
    rotate_square(center + 1, center + 1, center)

    return new_board

def divide_group(board, n):
    """
    bfs를 통해서 그룹을 나눔
    반환값: 그룹핑된 board(grouping_board), 해당 그룹의 원래 값(original_value: dict()), 해당 그룹의 크기(group_size: dict())
    """
    grouping_board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    original_value = dict()
    group_size = dict()

    gid = 0 # 그룹 아이디는 1번부터 이므로 0부터.
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):
            # 방문하지 않았으면
            if not visited[i][j]:
                gid += 1 # 새로운 그룹을 발견하면 gid +1.
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                grouping_board[i][j] = gid
                
                val = board[i][j]
                size = 1

                while queue:
                    cx, cy = queue.popleft()
                    # 동서남북
                    for dx, dy in dirs:
                        nx, ny = cx + dx, cy + dy
                        # 범위, 방문하지 않았으면
                        if in_range(nx, ny, n) and not visited[nx][ny]:
                            # val과 같은 값이라면
                            if board[nx][ny] == val:
                                visited[nx][ny] = True
                                grouping_board[nx][ny] = gid
                                queue.append((nx, ny))
                                size += 1
                                

                # 그룹 정보 기록
                original_value[gid] = val
                group_size[gid] = size

    return grouping_board, original_value, group_size

def backtrack(group_ids):
    """"
    백트래킹을 사용하여 2개씩 그룹 조합 생성하기
    반환값: 2개의 그룹이 묶인 배열
    """
    result = []
    n = len(group_ids)

    def dfs(start, path):
        if len(path) == 2:
            result.append(tuple(path))
            return
        for i in range(start, n):
            dfs(i + 1, path + [group_ids[i]])

    dfs(0, [])

    return result

def get_contact_cnt(a, b, grouping_board, n):
    """
    두 그룹 a, b가 맞닿아 있는 변의 수 계산
    """
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if grouping_board[i][j] == a: # 한 개의 그룹만 확인.
                # 동서남북
                for dx, dy in dirs:
                    nx, ny = i + dx, j + dy
                    # 범위 안에 있고 board[nx][ny] 값이 b그룹이라면
                    if in_range(nx, ny, n) and grouping_board[nx][ny] == b:
                        cnt += 1

    return cnt

def calculate_art_score(grouping_board, original_value, group_size, a, b, n):
    """
    예술 점수 계산
    """
    # 그룹 a에 속한 칸의 수
    cnt_a = group_size[a]
    # 그룹 b에 속한 칸의 수
    cnt_b = group_size[b]
    # 그룹 a를 이루고 있는 숫자 값
    val_a = original_value[a]
    # 그룹 b를 이루고 있는 숫자 값
    val_b = original_value[b]
    # 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    border_cnt = get_contact_cnt(a, b, grouping_board, n)

    return (cnt_a + cnt_b) * val_a * val_b * border_cnt

def main():
    total_score = 0
    board = []
    n = int(input())
    for _ in range(n):
        input_list = list(map(int, input().split()))
        board.append(input_list)

    # 초기 상태 + 3번 회전
    for _ in range(4):
        # 그룹 나누기 (회전하면 새로운 그룹이 생기니 회전할 때마다 그룹을 나눠야 함.)
        grouping_board, original_value, group_size = divide_group(board, n)
        group_ids = list(group_size.keys())

        # 조합 생성
        combi = backtrack(group_ids)

        # 점수 계산
        for a, b in combi:
            total_score += calculate_art_score(grouping_board, original_value, group_size, a, b, n)

        # 회전
        board = rotate(board, n)

    print(total_score)

if __name__ == "__main__":
    main()
