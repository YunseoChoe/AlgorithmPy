# 연구소2
from collections import deque
from itertools import combinations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# v = ([0,0], [1,1]]) 이런 형식
def bfs(v):
    q = deque(v)

    # visited 초기화
    visited = [[-1 for _ in range(n)] for _ in range(n)] # 0으로 초기화시키면, 제일 처음 방문한 (i, j)를 재방문할 수 있다.
    # 바이러스가 있는 곳은 0으로 초기화
    for x, y in q:
        visited[x][y] = 0

    while q:
        # 바이러스 위치부터 탐색 시작
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않았고 (바이러스가 아닌 곳도 포함), 벽이 아니라면
                if visited[nx][ny] == -1 and graph[nx][ny] != 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    cnt = -1
    # 연구소 전체가 감영되었는지 체크
    for i in range(n):
        for j in range(n):
            # 벽이 아닌데 방문하지 않았으면
            if graph[i][j] != 1 and visited[i][j] == -1:
                return -1 # 바로 종료
            # 최대 시간 찾기
            cnt = max(cnt, graph[i][j])
    return cnt
            
if __name__ == '__main__':    
    virus_list = []
    # 바이러스 조합 구하는 함수
    # def virus(count):
    #     if count == m:
    #         bfs()
    #         return
    #     for i in range(n):
    #         for j in range(n):
    #             if graph[i][j] == 2:
    #                 virus_list.append((i, j))
    #                 virus(count + 1)
    #                 virus_list.pop()

    # 입력 받기
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph_list = list(map(int, input().split()))
        graph.append(graph_list)
        
    # 바이러스가 놓일 수 있는 위치 배열
    virus_pos = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                virus_pos.append([i, j])

    ans = 0 # TODO: 초기화
    for v in combinations(virus_pos, m):
        print(v)
        # ((0,0), (1, 1), (2,2))
        # m = 2
        # v = ([0,0], [1,1])
        # v = ([0, 0], [2, 2])
        # v = ([1,1], [2, 2])

        result = bfs(v)
        if result != -1:
            ans = min(ans, result)

    print(ans) # TODO: 바이러스를 전부 퍼뜨리지 못하면 -1
                        