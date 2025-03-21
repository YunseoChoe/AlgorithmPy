from collections import deque

def solution(land): 
    answer = 0
    n = len(land)
    m = len(land[0])
    oil = [0] * m
    visited = []
    
    for i in range(n):
        visited_list = [0] * m
        visited.append(visited_list)
        
    # 동서남북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 석유 덩어리 크기 세는 함수
    def bfs(x, y):
        oil_set = {y}
        count = 1
        q = deque()
        q.append((x, y))
        visited[x][y] = 1
        while q:
            cur_x, cur_y = q.popleft()
            # 동서남북
            for i in range(4):
                new_x, new_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    # 방문하지 않았고 석유라면
                    if visited[new_x][new_y] == 0 and land[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        visited[new_x][new_y] = 1
                        count += 1
                        oil_set.add(new_y)
        for col in oil_set:
            oil[col] += count
                    
    for i in range(n):
        for j in range(m):
            # 방문하지 않은 석유라면 덩어리 개수 세기 
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                
    answer = max(oil)
    return answer
