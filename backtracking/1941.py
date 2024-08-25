# 소문난 칠공주
stu = []  # 전체 학생을 담는 배열
for i in range(5):
    per = input()
    stu.append(list(per))

# 상하좌우로 연결되어 있는지
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start, arr, visited):
    global cnt
    x = start // 5
    y = start % 5
    
    if visited[start] == 0:
        visited[start] = 1
        cnt += 1
        for j in range(4):
            new_x = x + dx[j]
            new_y = y + dy[j]
            if 0 <= new_x < 5 and 0 <= new_y < 5:
                new_i = new_x * 5 + new_y
                if visited[new_i] == 0 and new_i in arr:
                    dfs(new_i, arr, visited)

# 이다솜파가 4명 이상 있는지
def check_cnt(arr):
    s_cnt = 0
    for i in arr:
        if stu[i // 5][i % 5] == 'S':
            s_cnt += 1
    return s_cnt >= 4

def func(start, arr):
    global all_cnt
    global cnt
    if len(arr) == 7:
        visited = [0] * 25  # 방문 배열 초기화
        cnt = 0  # 연결된 학생 수 초기화
        dfs(arr[0], arr, visited)
        if cnt == 7 and check_cnt(arr):
            all_cnt += 1
        return

    for i in range(start, 25):
        if i not in arr:
            arr.append(i)
            func(i + 1, arr)
            arr.pop()

arr = []
all_cnt = 0
func(0, arr)
print(all_cnt)
