# 구슬 탈출
import sys
from collections import deque
input = sys.stdin.readline

# 주사위 굴리기 함수
def roll(command):
        global x, y
        # print()
        # print("roll함수 실행")
        # print(f'현재 x, y값: {x, y}')
        # 0 - 윗면, 1 - 앞면, 2 - 밑면, 3 - 뒷면, 4 - 왼쪽, 5 - 오른쪽
        a = dice[0]
        b = dice[1]
        c = dice[2]
        d = dice[3]
        e = dice[4]
        f = dice[5]

        # 동
        if command == 1: 
            # print("동쪽")
            dice[0] = e
            dice[1] = b
            dice[2] = f
            dice[3] = d
            dice[4] = c
            dice[5] = a
            y += 1
        # 서
        elif command == 2:
            # print("서쪽")
            dice[0] = f
            dice[1] = b
            dice[2] = e
            dice[3] = d
            dice[4] = a
            dice[5] = c
            y -= 1
        # 남
        elif command == 4:
            # print("남쪽")
            dice[0] = d
            dice[1] = a
            dice[2] = b
            dice[3] = c
            dice[4] = e
            dice[5] = f
            x += 1
        # 북
        else:
            # print("북쪽")
            dice[0] = b
            dice[1] = c
            dice[2] = d
            dice[3] = a
            dice[4] = e
            dice[5] = f
            x -= 1

        # 굴린 후
        # 범위가 맞으면 
        if 0 <= x < n and 0 <= y < m:
            # 지도 값이 0이면, 주사위 밑면을 지도에 복사
            if graph[x][y] == 0:
                # print("지도 값이 0이라면")
                graph[x][y] = dice[2]
            # 지도 값이 0이 아니면, 주사위 밑면은 지도값으로 복사, 지도 값은 0으로
            else:
                # print("지도값이 0이 아니라면")
                dice[2] = graph[x][y]
                graph[x][y] = 0
            # print(f'지도 출력: {graph}')
            return 1
        else:
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
        # 윗면에 있는 수 출력
        # for j in range(6):
        #     print(f'주사위 전체 출력: {j}: {dice[j]}')
        # 함수의 return 값이 0일때만 윗면 값 출력
        if return_value:
            print_list.append(dice[0])
        

    for i in range(len(print_list)):
        print(print_list[i])
