# 적록색약
import copy

n = int(input())
painting = []
for i in range(n):
    p_list = []
    p = input()
    for j in range(len(p)):
        p_list.append(p[j])
    painting.append(p_list)

print(painting)

# [['R', 'R', 'R'], 
#  ['R', 'R', 'R'],
#  ['R', 'R', 'R']]

# visited 배열 (n^2로 초기화)
visited = {}
for i in range(n):
    for j in range(n):
        visited[painting[i][j]] = 0

print(visited)

dfs_arr = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# dfs 함수
def dfs(start_x, start_y):
    # print(start_x, start_y)
    if visited[painting[start_x][start_y]] == 1:
        print("if")
        return
    else:
        print("else")
        # print(f'painting[start_x][start_y]: {painting[start_x][start_y]}')
        global dfs_arr
        # if (start_x, start_y) != (0, 0):
        dfs_arr.append((start_x, start_y))
        visited[painting[start_x][start_y]] = 1
    
        for i in range(4):
                    x = start_x + dx[i]
                    y = start_y + dy[i]
                    print(x, y)
                    # 범위
                    if (0 <= x <= len(painting[0]) - 1 and 0 <= y <= (len(painting) - 1)) and (painting[x][y] != painting[start_x][start_y]) and visited[painting[x][y]] != 1:
                        print("dfs ")
                        print(painting[start_x][start_y], end = " ")
                        print(painting[x][y])
                        print(visited)
                        dfs(x, y)
                    
                
dfs(0, 0)
print(dfs_arr)
print(len(dfs_arr))
