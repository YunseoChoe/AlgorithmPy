EXIT_DIRS = [(), (), (), ()] # 북, 동, 남, 서
def change_exit_direction():
    """
    출구의 방향을 바꿈
    """
    pass

def jungnyung_move(board, nr, nc, d, gid, rr, c):
    """
    정녕 이동 함수
    최대한 정녕을 남으로 이동시킴
    반환: 정령의 최종적 행
    """
    q = deque([gid])
    vis = {gid}

    while q:
        cgid = q.popleft()
        # 모든 golem에 대한 정보를 이미 가지고 있어야 함
        # gid -> (cr, cc, d)
        cr, cc, cd = golem_info[cgid]

        exr, exc = cr + EXIT_DIRS[cd], cc + EXIT_DIRS[cd]

        for dr, dc in DIRS:
            next_dr, next_dc = exr + dr, exc + dc
            if 범위 안에 있는지 체크:
                continue
            next_id = board[next_dr][next_dc]
            if next_id != 0 and next_id != cgid and next_id not in vis:
                vis.add(next_id)
                q.append(next_id)

def place_golem(board, id, r, c):
    board[r][c - 1] = id
    board[r][c] = id

def in_range(board, gid, parts, r, c):
    # 각각의 part들 돌면서, 얘네가 board 범위 안에 있는지 && 해당 part가 다른 골렘이 있는지 확인해야한다.
    pass

def golem_move(c_start, d_start, gid, board, r, c):
    """ 
        더 이상 움직이지 못할 때까지 반복
        우선 순위
        1. 남쪽 이동
        2. 남쪽으로 이동할 수 없으면(초록색 칸들이 비어있지 않으면) 서쪽 이동하면서 내려옴
        + 이동하면서 출구는 반시계방향으로 이동
        3. 남, 서쪽으로 이동할 수 없으면 동쪽 이동하면서 내려감
        + 이동하면서 출구는 반시계방향으로 이동
        가장 남쪽에 도달해 더이상 이동할 수 없으면 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동 가능. 
        단 현재 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동 가능
        최종적으로 정령을 최대한 남쪽으로 이동시킨 후 이동을 완전히 종료 -> 이때의 위치가 정령의 최종 위치

        최종 남쪽에 도착한 골렘의 몸 일부가 숲을 벗어난 상태라면, 해당 골렘을 포함한 숲에 위치한 모든 골렘들을 삭제 후 다시 탐색 시작.
        
        반환: 골렘의 최종 센터 행, 열, 출구 방향
    """
    cr, cc = 1, c_start - 1 # center
    d = d_start

    ## drop
    while True:
        move = False
        # 남쪽으로 이동
        golem_part = [(cr + 1, cc - 1), (cr + 2, cc), (cr + 1, cc + 1)]
        if in_range(board, gid, golem_part, r, c):
            cr += 1
            move = True
        else:
            # 서쪽으로 이동 + 아래
            golem_part = [(cr - 1, cc - 1), (cr, cc - 2), (cr + 1, cc - 2), (cr + 1, cc - 1), (cr + 2, cc - 1)]
            if in_range(board, gid, golem_part, r, c):
                cr += 1
                cc -= 1
                d = (d - 1) % 4
                move = True
            # 동쪽으로 이동 + 아래
            else:
                golem_part = []
                if in_range():
                    cr
                    cc
                    d
                    move

        if not move:
            break

    return cr, cc, d

def main():
    row_sum = 0 # 정녕들의 누적 합
    
    r, c, k = map(int, input().split(" ")) # 행, 렬, 정녕 수
    rr = r + 3 # + 3 !!! 
    board = [[0] * c for _ in range(rr)]
    
    gid = 1
    
    golem_info = {}
    # k번 반복
    for _ in range(k):

        c_start, d_start = map(int, input().split(" ")) # 골렘이 출발하는 열, 골렘의 출구 방향 정보

        # 탐색 시작
        nr, nc, d = golem_move(c_start, d_start, gid, board, rr, c)

        # 최종 이동 후, 골렘이 숲에 걸쳐있다면 nr - 1 >= 3
        if nr < 4:
            board = [[0] * c for _ in range(rr)] # 모든 골렘 삭제 후 다음 골렘 시작
            gid = 1
            continue

        place_golem(board, gid, nr, nc)
        row_sum += jungnyung_move(board, nr, nc, d, gid, rr, c) # 다른 골렘으로 이동
        gid += 1

    print(row_sum)
