# 숨바꼭질 4
n, k = list(map(int, input().split()))

dist = [0] * 100001 # 거리를 저장하는 배열
path = {} # 지나온 위치를 저장하는 딕셔너리 (key값은 해당 위치와 value값은 지나온 위치들)

def print_path():
    root = [] 
    now = k
    # 이전 위치로 이동하면서 경로 저장
    while now != n:
        root.append(now)
        now = path[now]
        if now == n:
            root.append(n)
    # 경로가 없을 경우
    if len(root) == 0:
        print(k)
    else:
        # 역순으로 출력
        root.reverse()    
        for value in root:
            print(value, end = " ")
    
def bfs(start):
    global return_path
    queue = []
    dist[start] = 0
    path[start] = start                                                                            
    queue.append(start)

    while len(queue) != 0:
        x = queue.pop(0)
        if x == k:
            # 출력 (path, 함수)
            print(dist[k])
            print_path()
            break # queue의 모든 요소를 끝까지 보지 않아도 됨.

        for x_1 in [x - 1, x + 1, x * 2]:
            # 시작 위치라면
            if x_1 == start:
                pass
            else:
                # 범위 확인
                if 0 <= x_1 <= 100000 and dist[x_1] == 0:
                    dist[x_1] = dist[x] + 1
                    queue.append(x_1)

                    # 이전 위치 저장
                    path[x_1] = x
                        
bfs(n)
