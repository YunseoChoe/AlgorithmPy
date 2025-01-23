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
    q = deque()
    q.append((x, y, z))
    while q:
        # print(f'q 내용: {q}')
        new_x, new_y, new_z = q.popleft()
        # 목적지에 도착했으면 종료
        if new_x == dest_x and new_y == dest_y and new_z == dest_z:
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
                # 방문하지 않았고, 비어있는 칸 또는 목적지라면 이동
                if visited[nz][nx][ny] == 0 and (graph[nz][nx][ny] == "." or graph[nz][nx][ny] == "E"):
                    q.append((nx, ny, nz))
                    # 방문 배열에 경로를 누적
                    visited[nz][nx][ny] = visited[new_z][new_x][new_y] + 1
                
    print_list.append("Trapped!")
           
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
            line = input()
        

        # 시작점, 목적지 찾기
        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if graph[i][j][k] == "S":
                        start_z, start_x, start_y = i, j, k
                    elif graph[i][j][k] == "E":
                        dest_z, dest_x, dest_y = i, j, k

        # bfs호출
        bfs(start_x, start_y, start_z, dest_x, dest_y, dest_z)

    # 최종 출력
    for i in range(len(print_list)):
        print(print_list[i])
