# 감시
import sys
import copy
input = sys.stdin.readline

n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

# cctv 정보 저장
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append((i, j, graph[i][j]))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# number 1: dir에 차례대로 동, 서, 남, 복
# number 2: dir에 차례대로 (동서), (남북)
# number 3: dir에 차례대로 (동남), (남서), (서북), (북동)
# number 4: dir에 차례대로 (동남서), (남서북), (서북동), (북동남)
# number 5: dir에 1번 돌기 

# 0 -> 동
# 1 -> 남
# 2 -> 서
# 3 -> 북
direction = {
    1: [[0], [1], [2], [3]], # len(arr) = 4
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# cctv가 감시할 수 있는 영역 표시
def view(dir, graph, x, y): # dir은 방향 정보 배열 (ex. dir = [0] or dir = [[0, 2], [1, 3]], ...)
    # dir에 맞는 모든 방향을 봐야하므로 반복문 사용
    for i in dir:
        nx = x + dx[i]
        ny = y + dy[i]
        # 벽이 아니고 끝이 아니고, cctv가 아니라면 
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
            graph[nx][ny] = '#'
            nx += dx[i]
            ny += dy[i]

# 이전 상태로 되돌리는 함수
# def back(dir, graph, x, y):
#     for i in dir:
#         nx = x + dx[i]
#         ny = y + dy[i]
#         while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
#             graph[nx][ny] = 0
#             nx += dx[i]
#             ny += dy[i]

# 사각지대 세기 
answer = 10000000000000 # 초기화
def count_zero(graph):
    global answer # 전역 변수 설정
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                cnt += 1
    answer = min(cnt, answer)
    
# cctv의 모든 조합 탐색
def dfs(count):
    global graph
    # 모든 cctv를 탐색했으면
    if count == len(cctv): # cctv = [x, y, cctv number]
        # 사각지대 개수 세기
        count_zero(graph) # answer값 update
        return
    
    new_graph = copy.deepcopy(graph) # 기존 graph 저장해놓기      
    x, y, number = cctv[count] # number은 cctv의 방향 정보를 담고있는 번호
    # 내가 지금 살펴보려는 cctv를 get해서, 해당 cctv의 모든 방향을 살펴봐야한다.
    for dir in direction[number]:
        # 영역 표시
        view(dir, graph, x, y)
        dfs(count + 1)
        # view 이전 상태로 graph 원상복귀 시키기
        # back(dir, graph, x, y)
        graph = copy.deepcopy(new_graph)  # 저장해놨던 기존 graph로 원상복구

dfs(0)
print(answer)
