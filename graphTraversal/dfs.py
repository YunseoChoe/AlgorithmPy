# 정점: 0, 1, 2, 3
adj_mat = [[0, 1, 1, 0],
           [1, 0, 0, 1],
           [1, 0, 0, 1],
           [0, 1, 1, 0]]

# adj_mat = [[0, 0, 0, 0, 0, 0],
#            [0, 0, 1, 0, 0, 1],
#            [0, 1, 0, 0, 1, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 1, 0, 0, 1],
#            [0, 1, 0, 0, 1, 0]]

visited = [0, 0, 0, 0, 0, 0] # 방문 배열
def dfs(start):
    # 방문했다면
    if visited[start]:
        return
    else:
        visited[start] = 1
        print(start, end = " ")
        for i in range(len(adj_mat[0])):
            if adj_mat[start][i] == 1 and visited[i] == 0:
                dfs(i)


print("dfs: ", end = " ")
dfs(0)
 
        
