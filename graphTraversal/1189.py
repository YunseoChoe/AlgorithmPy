# 컴백홈

dx = 
dy = 

def dfs(start_x, start_y, dist):
    if start_x == 0 and start_y == r and dist == k:
        result += 1
    else:
        visited[start_x][start_y] = True
        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and adj_mat[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, dist + 1)
            