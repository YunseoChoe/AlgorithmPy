# 안전 영역
import sys
sys.setrecursionlimit(10**6)

graph = []
maxNum = 0 # graph에서의 최고 높이

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start_x, start_y, height):
    if visited[start_x][start_y]:
        return 
    visited[start_x][start_y] = True
    # 상하좌우 보면서 방문하지 않았고, height보다 크면 dfs
    for i in range(4):
        new_x = start_x + dx[i]
        new_y = start_y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and visited[new_x][new_y] == False and graph[new_x][new_y] > height:
            dfs(new_x, new_y, height)
        
if __name__ == '__main__':
    result = 0
    n = int(input())
    # enter graph information
    for i in range(n):        
        graph_list = list(map(int, input().split(' ')))
        graph.append(graph_list)

    # maxNum 구하기
    for i in range(n):
        for j in range(n):
            maxNum = max(maxNum, graph[i][j])
    
    # 높이 별로 안전 영역 구하기
    for height in range(0, maxNum):
        area = 0 # 높이마다 안전 영역이 달라짐
        # 방문 배열 초기화
        visited = []
        for i in range(n):
            visited_list = [False] * n
            visited.append(visited_list)
        for i in range(n):
            for j in range(n):
                # 높이보다 크고 방문하지 않았으면 dfs
                if graph[i][j] > height and visited[i][j] == False:
                    dfs(i, j, height) 
                    area += 1
        # print(f'높이{height}에서 area: {area}')
        result = max(result, area)

    print(result)
