from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def driver_move(i, d, n, r, c, h, w, k, dmg, board):
    """
    i번 기사를 d 방향으로 한 칸 이동시킴
    반환값: 
    """
    # 체력이 0보다 작으면 이동 불가
    if k[i] <= 0:
        return
    
    # i번째 기사 이동 가능하면, 이동
    if try_movement(i, d, n, r, c, h, w, k, dmg, board):
        r[i] += dx[d]
        c[i] += dy[d]
        k[i] -= dmg[i] # 해당 기사의 피해만큼 체력 빼주기.

def try_movement(i, d, n, r, c, h, w, k, dmg, board):
    """
    이동가능하면 True, 불가능하면 False
    """
    q = deque()
    q.append(i) # i번째 기사부터.
    visited = [False] * n
    visited[i] = True # 이동했는지 확인
    
    while not q:
        c_driver = q.poll()

        # 이동할 위치 계산
        nx = r[c_driver] + dx[d]
        ny = c[c_driver] + dy[d]
        
        # 범위 확인
        # if nr[i], nc[i]가 범위 안에 들어있지 않나?:
        if not in_range(nx, ny, n):
            return False
        
        # 함정이나 벽이 있는지 확인
        for i in range(nx, nx + h[c_driver] + 1):
            for j in range(ny, ny + h[c_driver] + 1):
                # 함정이 있으면 대미지 +1
                if board[nx][ny] == 2:
                    dmg[c_driver] += 1
                # 벽이 있으면 이동 불가
                if board[nx][ny] == 1:
                    return False
        
        # 다른 기사랑 충돌이 났는지 확인
        for next_driver in range(n):
            # 방문했거나, 체력이 0이하면 continue
            if visited[next_driver] or k[next_driver] <= 0:
                continue
            # 이동하려고 하는 곳에 다른 기사가 있다면
            if nx <= r[next_driver] < nx + h[c_driver] and ny <= c[next_driver] < ny + w[c_driver]:
                visited[next_driver] = True
                q.append(next_driver) # 해당 기사도 연쇄 이동해야 함.
            
def damage(i, r, c, h, w, k, board, total_damage):
    """
    i번 기사가 이동 후 밀려나거나 함정 위에 있을 때 피해 계산
    """
    # 대미지 계산
    damage_cnt = 0
    # 기사 영역에 있는 함정의 개수만큼 피해를 입음
    for x in range(r[i], r[i] + h[i]):
        for y in range(c[i], c[i] + w[i]):
            if board[x][y] == 2:
                damage_cnt += 1
    
    # 대미지가 있다면
    if damage_cnt > 0:
        # 체력이 부족하다면
        if k[i] <= damage_cnt:
            k[i] = 0
            for x in range(r[i], r[i] + h[i]):
                for y in range(c[i], c[i] + w[i]):
                    board[x][y] = 0 # 체스판에서 제거해야 함.
        # 체력이 부족하지 않다면 체력 감소
        else:
            k[i] -= damage_cnt

        total_damage += damage_cnt # 총 입은 대미지 합산

    return total_damage
    
def main():
    l, n, q = map(int, input().split())
    # 체스판 입력
    board = [list(map(int, input().split())) for _ in range(l)]

    # 기사 정보 입력 (초기 위치(r, c), h x w, 체력)
    r, c, h, w, k = [], [], [], [], []
    for _ in range(n):
        ri, ci, hi, wi, ki = map(int, input().split())
        r.append(ri)
        c.append(ci)
        h.append(hi)
        w.append(wi)
        k.append(ki)

    # 명령 입력
    commands = [tuple(map(int, input().split())) for _ in range(q)]

    dmg = [0] * n
    total_damage = 0

    # 명령 처리
    for cmd in commands:
        i, d = cmd # i번째 기사, d방향
        # 기사 이동
        driver_move(i - 1, d, n, r, c, h, w, k, dmg, board)

        # 이동 후 피해 계산
        for idx in range(n):
            total_damage = damage(idx, r, c, h, w, k, board, total_damage)
    
    print(total_damage) # 생존한 기사들이 총 받은 대미지의 합

if __name__ == "__main__":
    main()
