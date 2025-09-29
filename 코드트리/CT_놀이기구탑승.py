import sys
input = sys.stdin.readline

DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n

# 놀이기구 탑승 (자리 배정)
def board(map_, stu, like, n, like_dict):
    best = (-1, -1)
    max_like = -1
    max_empty = -1

    for i in range(n):
        for j in range(n):
            # 이미 앉아 있으면 패스
            if map_[i][j] != 0: 
                continue

            like_cnt = 0
            empty_cnt = 0
            # 동서남북
            for dx, dy in DIR:
                nx, ny = i + dx, j + dy
                if in_range(nx, ny, n):
                    if map_[nx][ny] in like:
                        like_cnt += 1
                    if map_[nx][ny] == 0:
                        empty_cnt += 1

            # 우선순위 비교
            if (like_cnt > max_like or
               (like_cnt == max_like and empty_cnt > max_empty) or
               (like_cnt == max_like and empty_cnt == max_empty and i < best[0]) or
               (like_cnt == max_like and empty_cnt == max_empty and i == best[0] and j < best[1])):
                best = (i, j)
                max_like = like_cnt
                max_empty = empty_cnt

    # 학생 앉히기
    r, c = best
    map_[r][c] = stu
    like_dict[stu] = like # 좋아하는 학생 저장

# 학생 점수 구하기
def get_student_score(map_, i, j, n, like_dict):
    stu = map_[i][j]
    like = like_dict[stu]
    cnt = 0
    # 동서남북
    for dx, dy in DIR:
        nx, ny = i + dx, j + dy
        if in_range(nx, ny, n) and map_[nx][ny] in like:
            cnt += 1

    if cnt == 0:
        return 0
    return 10 ** (cnt - 1)

def main():
    n = int(input())
    map_ = [[0] * n for _ in range(n)]
    like_dict = {}
    order = []
    
    for i in range(n):
        for j in range(n):
            data = list(map(int, input().split()))
            stu = data[0]
            like = data[1:]
            order.append((stu, like))

    # 학생 순서대로 앉히기
    for stu, like in order:
        board(map_, stu, like, n, like_dict)

    # 점수 계산
    total_score = 0
    for i in range(n):
        for j in range(n):
            total_score += get_student_score(map_, i, j, n, like_dict)

    print(total_score)

if __name__ == "__main__":
    main()
