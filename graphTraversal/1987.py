# 알파벳
r, c = map(int, input().split())
alphabets = []
for i in range(r):
    alphabet = []
    a = input()
    for j in range(c):
        alphabet.append(a[j])
    alphabets.append(alphabet)    

# visited 딕셔너리 초기화
visited = {}
for i in range(r):
    for j in range(c):
        visited[alphabets[i][j]] = 0    
        
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

max_path = 0

def dfs(start_x, start_y, path):
    global max_path
    # 방문했다면
    start_chr = alphabets[start_x][start_y]
    if visited[start_chr] == 1:
        return
    visited[start_chr] = 1
    max_path = max(max_path, path) # 최댓값 갱신하는 코드
    for i in range(4):
        x = start_x + dx[i]
        y = start_y + dy[i]
        # 여태껏 방문하지 않았고, 이동하려는 값이 방문하지 않았으면
        if 0 <= x < r and 0 <= y < c:
            next_chr = alphabets[x][y]
            if visited[next_chr] == 0:
                dfs(x, y, path + 1)
                visited[next_chr] = 0
        
dfs(0, 0, 1)
print(max_path)
