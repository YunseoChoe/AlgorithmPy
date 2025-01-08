# 상범빌딩
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북상하
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

print_list = [] # 출력 배열

def bfs(x, y, z, dest_x, dest_y, dest_z):
    print(f'목적지 좌표: {dest_z}층 {dest_x}행 {dest_y}열')
    q = deque()
    q.append((z, x, y))
    while q:
        new_z, new_x, new_y = q.popleft()
        print(new_z, new_x, new_y)
        # 목적지에 도착했으면 종료
        if new_x == dest_x and new_y == dest_y and new_z == dest_z:
            print("목적지 도착!")
            print_list.append()
            p = f'Escaped in {visited[dest_z][dest_x][dest_y]} minute(s).'
            print_list.append(p)
            return
        # 동서남북상하 
        for i in range(6):
            nx = new_x + dx[i]
            ny = new_y + dy[i]
            nz = new_z + dz[i]
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                # print(f"현재 보고있는 좌표값: {nz}층 {nx}행 {ny}열")
                # 방문하지 않았고, 비어있는 칸이면 이동
                if visited[nz][nx][ny] == 0 and graph[nz][nx][ny] == ".":
                    q.append((nz, nx, ny))
                    # 방문 배열에 경로를 누적
                    visited[nz][nx][ny] = visited[new_z][new_x][new_y] + 1
                    print(f'visited 출력: {visited}')
    w = "Trapped!"
    print_list.append(w)
           
if __name__ == '__main__':
    while True:
        l, r, c = map(int, input().split())
        # while문 종료 조건
        if l == 0 and r == 0 and c == 0:
            break

        # visited 배열 초기화
        visited = []
        for _ in range(l):
            visited_mat = []
            for _ in range(r):
                visited_list = [0] * c
                visited_mat.append(visited_list)
            visited.append(visited_mat)

        # graph 입력
        graph = []
        for _ in range(l):
            graph_mat = []
            for _ in range(r):
                graph_list = input().strip()
                graph_mat.append(graph_list)
            graph.append(graph_mat)
        print(f'graph 출력: {graph}')

        # 시작점, 목적지 찾기
        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if graph[i][j][k] == "S":
                        start_z = i
                        start_x = j
                        start_y = k
                    elif graph[i][j][k] == "E":
                        dest_z = i
                        dest_x = j
                        dest_y = k

        # bfs호출
        bfs(start_z, start_x, start_y, dest_x, dest_y, dest_z)

        # 최종 출력
        for i in range(len(print_list)):
            print(print_list[i])

