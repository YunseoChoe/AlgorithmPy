# 로봇 청소기
import sys
from collections import deque
input = sys.stdin.readline

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    # 입력받기
    n, m = map(int, input().split())
    r, c, d = map(int, input().split()) # 로봇청소기 시작 위치, 방향
    graph = []
    for i in range(n):
        graph_list = list(map(int, input().split()))
        graph.append(graph_list)

    clean_count = 0

    i = r # 시작 x위치
    j = c # 시작 y위치

    # 후진할 수 없을 때까지 작동
    while True:
        # 1. 현재 칸이 청소되지 않은 경우
        if graph[i][j] == 0:
            clean_count += 1
            graph[i][j] = 2 # 청소했으면 2로 체크
        
        # 동서남북 보기
        is_clean = False
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    is_clean = True # 청소되지 않은 빈 칸이 있음

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if is_clean == False:
            index = (d + 2) % 4
            nx = i + dx[index]
            ny = j + dy[index]

            # 범위가 맞고 만약 벽이 아니라면 후진
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                i = nx
                j = ny
            # 벽이라면 종료
            else:
                break
                 
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if is_clean:
            # 1. 반시계 회전
            d = (d + 3) % 4
            nx = i + dx[d]
            ny = j + dy[d]
            
            # 2. 앞 칸이 청소되지 않았다면 한 칸 전진
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                i = nx
                j = ny
            
    print(clean_count)
