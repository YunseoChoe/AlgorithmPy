# 뱀
if __name__ == '__main__':
    # 동서남북 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n = int(input()) # 보드의 크기
    k = int(input()) # 사과의 개수
    # 보드 초기화
    graph = [] 
    for _ in range(n):
        graph_list = [0] * n
        graph.append(graph_list)

    print(graph)
    
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

    print(snake_ways)

    total_second = 1
    head_x = 0 # 뱀은 (0, 0)에서 시작하고 오른쪽(1)을 바라보고 있음
    head_y = 0
    tail_x = 0
    tail_y = 0
    d = 1 

    while True:
        total_second += 1
        # 종료조건
        if graph[head_x][head_y] == 2 or head_x < 0 or head_y < 0:
            print("게임 종료")  
            break

        # 방향 전환
        for s in snake_ways.keys(): 
            # 만약 해당 초가 됐다면
            if int(s) == total_second:
                # 방향이 L이라면 왼쪽으로 90도 회전
                if snake_ways[s] == 'L':
                    pass
                # 방향이 D라면 오른쪽으로 90도 회전
                elif snake_ways[s] == 'D':
                    pass


        # 사과가 있다면 (머리는 이동, 꼬리는 이동 x)
        if graph[nx][ny] == 1:
            graph[head_x][head_y] == 0 # 현재 칸에 사과 없애기
            # 뱀의 머리만 이동
            head_x = nx 
            head_y = ny
            
        # 사과가 없다면 (머리와 꼬리 모두 이동, 크기는 변하지 않음)
        else:
            tail_x = ??
            tail_y = ??
            head_x = nx
            head_y = ny
            

        



        

                
                


