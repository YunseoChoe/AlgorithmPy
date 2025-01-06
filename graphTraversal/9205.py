# 맥주 마시면서 걸어가기
def bfs(start_x, start_y):
    q = []
    q.append((start_x, start_y))
    while q:
        x, y = q.pop() # x, y는 현재 위치
        # 페스티벌에 도달할 수 있으면
        if abs(x - x_festival) + abs(y - y_festival) <= 1000:
            print("happy")
            return
        # 페스티벌에 도달할 수 없으면
        for i in range(n): 
            # 방문하지 않았고, 현재 위치에서 1000m보다 가까이 있으면 편의점 들리기
            if visited[i] == False:
                x_conv, y_conv  = convinience_store[i] 
                if abs(x - x_conv) + abs(y - y_conv) <= 1000: 
                    visited[i] = True
                    q.append((x_conv, y_conv)) # 위치로 이동
    # happy가 출력되지 않았다면
    print("sad")

if __name__ == '__main__':
    t = int(input()) # 테스트 케이스의 개수
    for _ in range(t):
        n = int(input()) # 편의점의 개수
        # enter graph input
        x_home, y_home = map(int, input().split()) # 상근이 집 좌표
        convinience_store = [] # 편의점 
        for i in range(n):
            x_conv, y_conv = map(int, input().split()) # 편의점 좌표
            convinience_store.append((x_conv, y_conv))
        x_festival, y_festival = map(int, input().split()) # 페스티벌 좌표

        # 편의점 방문 배열 초기화
        visited = [False] * n
        
        # bfs 호출
        bfs(x_home, y_home) # 상근이 집부터 시작
