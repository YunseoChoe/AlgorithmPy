# 뱀
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] 
    

    q = deque()
    n = int(input()) # 보드의 크기
    k = int(input()) # 사과의 개수

    # 보드 초기화
    graph = [] 
    for _ in range(n):
        graph_list = [0] * n
        graph.append(graph_list)
    
    # 사과 입력받기
    for _ in range(k):
        apple_x, apple_y = map(int, input().split())
        graph[apple_x - 1][apple_y - 1] = 1 # 사과는 1


    # 뱀의 방향 횟수 입력받기
    snake_ways = {}
    l = int(input())
    for _ in range(l):
        second, way = input().split()
        snake_ways[second] = way

    total_second = 0 # 처음 시작은 0초 부터
    d = 0 # 뱀은 동쪽을 보고 시작
    nx = 0
    ny = 0
    q.append((nx, ny)) # 뱀의 첫 위치 넣기

    while True:
        total_second += 1

        # 방향 전환
        if str(total_second - 1) in snake_ways:
            way = snake_ways[str(total_second - 1)]
            if way == 'L':
                d = (d + 3) % 4
            elif way == 'D':
                d = (d + 1) % 4


        # 이동할 좌표 구하기 (d에 따라서)
        nx = nx + dx[d]
        ny = ny + dy[d]

        # 종료 조건
        # 벽이거나 자기 자신이면 종료
        if not (0 <= nx < n) or not (0 <= ny < n) or (nx, ny) in q:
            print(total_second)
            break

        # 사과가 있다면 (머리는 이동, 꼬리는 이동 x)
        if graph[nx][ny] == 1:
            # 현재 칸 사과 없애기
            graph[nx][ny] = 0
            # 뱀의 머리만 이동
            q.append((nx, ny))
            
        # 사과가 없다면 
        else:
            # 머리 이동
            q.append((nx, ny))
            # 꼬리 이동
            q.popleft()
