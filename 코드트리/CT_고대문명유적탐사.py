# 고대 문명 유적 탐사
from collections import deque
import copy

# 3x3 행렬 회전
def rot3x3(board, sr, sc, deg):
    sub_mat = [[0, 0, 0] for _ in range(3)]
    # 3x3 자를 부분
    for i in range(3):
        for j in range(3):
            sub_mat[i][j] = board[sr + i][sc + j]

    return_board = copy.deepcopy(board)

    # 90도 회전 함수 (180, 270도 회전 시에도 쓰임)
    def rot90(mat):
        """3x3 행렬을 시계방향으로 90도 회전 후 회전된 행렬 반환"""
        L = 3
        res = [[0] * L for _ in range(L)]
        for i in range(L):
            for j in range(L):
                res[j][L - 1 - i] = mat[i][j]
        return res

    if deg == 90:
        tmp = rot90(sub_mat)
    elif deg == 180:
        tmp = rot90(rot90(sub_mat))
    else:
        tmp = rot90(rot90(rot90(sub_mat)))

    # 다시 5x5로 합치기
    for i in range(3):
        for j in range(3):
            return_board[sr + i][sc + j] = tmp[i][j]

    return return_board


def find_groups(board):
    """보드에서 같은 숫자 (>0)로 연결된 그룹 중 크기가 >= 3 인 것들을 탐색 (bfs)"""
    visited = [[False] * 5 for _ in range(5)]
    groups = []

    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(x, y):
        target = board[x][y]
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        group = [(x, y)]
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and board[nx][ny] == target:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    group.append((nx, ny))
        return group

    for i in range(5):
        for j in range(5):
            if board[i][j] > 0 and not visited[i][j]:
                group = bfs(i, j)
                if len(group) >= 3:
                    groups.append(group)

    return groups


def calculated_gain(board_after_rotation):
    """회전 직 후, 점수를 계산 (보드 변경 x)"""
    tmp = copy.deepcopy(board_after_rotation)
    groups = find_groups(tmp)
    return sum(len(g) for g in groups)


def choose_rotation(board):
    """모든 3x3 부분에 대해서 회전 후 가장 최적의 회전 결과를 반환"""
    best = None
    for sr in range(0, 3):
        for sc in range(0, 3):
            for deg in (90, 180, 270):
                new_board = rot3x3(board, sr, sc, deg)
                cnt = calculated_gain(new_board)
                info = (-cnt, deg, sc, sr)  # 우선순위
                if best is None or info < best[0]:
                    best = (info, new_board)

    info, new_board = best
    return -info[0], new_board


def erase(board, groups):
    """groups = [(1, 2), (3, 4)]가 있을 때 board에서 해당 좌표들 0으로 만들기"""
    for group in groups:
        for i, j in group:
            board[i][j] = 0


def fill(board, wall_candidate):
    """열 오름차순, 행 내림차순"""
    empty_cells = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                empty_cells.append([i, j])

    # 우선순위 기준 정렬
    for i in range(len(empty_cells)):
        for j in range(i + 1, len(empty_cells)):
            r1, c1 = empty_cells[i]
            r2, c2 = empty_cells[j]
            if c1 > c2 or (c1 == c2 and r1 < r2):
                empty_cells[i], empty_cells[j] = empty_cells[j], empty_cells[i]

    idx = 0
    for r, c in empty_cells:
        if idx < len(wall_candidate):
            board[r][c] = wall_candidate[idx]
            idx += 1
        else:
            break

    return board


def process_gain_chain(board, wall_candidate):
    """find_group -> 제거 -> 벽 채우기 (연쇄)"""
    total = 0
    while True:
        groups = find_groups(board)
        if not groups:
            break
        else:
            erase(board, groups)
            total += sum(len(g) for g in groups)
            fill(board, wall_candidate)
    return total


def main():
    k, m = map(int, input().split())
    board = []
    for _ in range(5):
        row = list(map(int, input().split()))
        board.append(row)

    wall_candidate = list(map(int, input().split()))

    for _ in range(k):
        cnt, rotated = choose_rotation(board)
        if cnt == 0:
            break
        else:
            board = rotated
            gain_cnt = process_gain_chain(board, wall_candidate)
            print(gain_cnt)


if __name__ == "__main__":
    main()
