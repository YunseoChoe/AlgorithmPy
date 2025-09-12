# 효율적인 해킹 (인접 행렬)
n, m = input().split()
n = int(n)
m = int(m)

# 인접 행렬 초기화
adj_mat = []
for i in range(n):
    mat = []
    for j in range(n):
        mat.append(0)
    adj_mat.append(mat)

# print(adj_mat)

start_vertex = 100000 # dfs 시작 정점
for _ in range(m):
    vertexs = input().split(' ') # 공백 기준으로 입력
    vertexs[0] = int(vertexs[0])
    vertexs[1] = int(vertexs[1])

    for i in range(2):
        if start_vertex > vertexs[i]:
            start_vertex = vertexs[i]
    
    print(f'start_vertex: {start_vertex}')
    
    start = vertexs[1] - 1
    end = vertexs[0] - 1

    # print(end, start)

    adj_mat[start][end] = 1 # 방향 추가

print(adj_mat) # 확인용 출력

# 방문 배열 초기화
visited = [False] * n
# dict 초기화
dict = {}
for i in range(n):
    dict[i] = 0

print(dict)

def dfs(start):
    print(f'start: {start}')
    # 방문했으면
    if visited[start] == True:
        return
    # 방문하지 않았으면    
    visited[start] = True
    
    # 인접하고, 방문하지 않았다면 dfs 진행
    for i in range(len(adj_mat[0])):
        if adj_mat[start][i] == 1 and visited[i] == False:
            # print("dfs")
            dict[start] += 1 
            dfs(i)
            dict[start] += 1

print(f'첫 시작 정점: {start_vertex + 1}')
dfs(start_vertex + 1)
print(dict)
