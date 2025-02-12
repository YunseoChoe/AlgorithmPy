# 주사위 굴리기
import sys
from collections import deque
input = sys.stdin.readline

# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 굴리기 함수
def roll(command):
        global x, y
        # 0 - 윗면, 1 - 앞면, 2 - 밑면, 3 - 뒷면, 4 - 왼쪽, 5 - 오른쪽
        a = dice[0]
        b = dice[1]
        c = dice[2]
        d = dice[3]
        e = dice[4]
        f = dice[5]

        # 동
        if command == 1: 
            dice[0] = e
            dice[1] = b
            dice[2] = f
            dice[3] = d
            dice[4] = c
            dice[5] = a
        # 서
        elif command == 2:
            dice[0] = f
            dice[1] = b
            dice[2] = e
            dice[3] = d
            dice[4] = a
            dice[5] = c
        # 남
        elif command == 4:
            dice[0] = d
            dice[1] = a
            dice[2] = b
            dice[3] = c
            dice[4] = e
            dice[5] = f
        # 북
        else:
            dice[0] = b
            dice[1] = c
            dice[2] = d
            dice[3] = a
            dice[4] = e
            dice[5] = f

        # 이동
        x = x + dx[command - 1]
        y = y + dy[command - 1]

        # 범위가 맞으면
        if 0 <= x < n and 0 <= y < m:
            # 지도 값이 0이면
            if graph[x][y] == 0:
                graph[x][y] = dice[2]
            # 지도 값이 0이 아니면
            else:
                dice[2] = graph[x][y]
                graph[x][y] = 0
            return 1

        # 범위가 맞지 않으면 
        # 원상복구
        x = x - dx[command - 1]
        y = y - dy[command - 1]
        return 0


if __name__ == '__main__':
    graph = [] # 지도
    print_list = []
    # 입력받기 
    n, m, x, y, k = map(int, input().strip().split(' '))
    for _ in range(n):
        graph_list = list(map(int, input().split(' ')))
        graph.append(graph_list)
    commands = list(map(int, input().split(' ')))
    
    dice = [0, 0, 0, 0, 0, 0] # 초기 주사위값은 모두 0
    
    # command 수만큼 주사위 굴리기
    for i in range(len(commands)):
        command = commands[i]
        return_value = roll(command)
        # return값이 1일 때만 출력
        if return_value:
            print_list.append(dice[0])

    for i in range(len(print_list)):
        print(print_list[i])
