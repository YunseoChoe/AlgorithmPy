# # 로봇 청소기
# import sys
# from collections import deque
# input = sys.stdin.readline

# # 동서남북
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# if __name__ == '__main__':
#     # 입력받기
#     n, m = map(int, input().split())
#     r, c, d = map(int, input().split()) # 로봇청소기 시작 위치, 방향
#     graph = []
#     for i in range(n):
#         graph_list = list(map(int, input().split()))
#         graph.append(graph_list)

#     clean_count = 0

#     i = r # 시작 x위치
#     j = c # 시작 y위치

#     print(f'i: {i}')
#     print(f'j: {j}')
#     print(f'd: {d}')

#     # 후진할 수 없을 때까지 작동
#     # is_all_clean_up = True
#     while True:
#         # 1. 현재 칸이 청소되지 않은 경우
#         print(f'i, j: {i}, {j}')
#         if graph[i][j] == 0:
#             print("청소함")
#             clean_count += 1
#             graph[i][j] = 2 # 청소했으면 2로 체크
        
#         # 동서남북 보기
#         is_clean = False
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < m:
#                 print(f'nx: {nx}')
#                 print(f'ny: {ny}')
#                 print(f'graph[nx][ny]: {graph[nx][ny]}')
#                 if graph[nx][ny] == 0:
#                     is_clean = True # 청소되지 않은 빈 칸이 있음

#         # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
#         if is_clean == False:
#             # 후진할 수 있다면 후진하고, 후진할 수 없다면 멈춤
#             # 동
#             if d == 1:
#                 if j - 1 >= 0:
#                     # 만약 벽이면 종료
#                     if graph[i][j - 1] == 1:
#                         break
#                     # 벽이 아니면 후진
#                     else:
#                         j -= 1
                    
#             # 서
#             elif d == 3:
#                 if j + 1 < m:
#                     # 만약 벽이면 종료
#                     if graph[i][j + 1] == 1:
#                         break
#                     # 벽이 아니면 후진
#                     else:
#                         j += 1

#             # 남
#             elif d == 2:
#                 if i - 1 >= 0:
#                     # 만약 벽이면 종료
#                     if graph[i - 1][j] == 1:
#                         break
#                     # 벽이 아니면 후진
#                     else:
#                         i -= 1

#             # 북
#             elif d == 0:
#                 if i + 1 < n:
#                     if graph[i + 1][j] == 1:
#                         break
#                     else:
#                         i += 1
                    
            

#         # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#         if is_clean:
#             # 1. 반시계 회전
#             # 동 -> 남
#             if d == 1:
#                 d = 2
#             # 서 -> 북
#             elif d == 3:
#                 d = 0
#             # 남 -> 동
#             elif d == 2:
#                 d = 1
#             # 북 -> 서
#             elif d == 0:
#                 d = 3

#             # 2. 앞 칸이 청소되지 않았다면 한 칸 전진
#             # 동
#             if d == 1:
#                 if j + 1 < m:
#                     if graph[i][j + 1] == 0:
#                         j += 1
#             # 서
#             elif d == 3:
#                 if j - 1 >= 0:
#                     if graph[i][j - 1] == 0:
#                         j -= 1
#             # 남
#             elif d == 2:
#                 if i + 1 < n:
#                     if graph[i + 1][j] == 0:
#                         i += 1
#             # 북
#             elif d == 0:
#                 if i - 1 >= 0:
#                     if graph[i - 1][j] == 0:
#                         i -= 1

#     print(clean_count)
#     print(graph)



# 로봇 청소기
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    # 입력받기
    n, m = map(int, input().split())
    r, c, d = map(int, input().split()) # 로봇청소기 시작 위치, 방향
    graph = []
    for i in range(n):
        graph_list = list(map(int, input().split()))
        graph.append(graph_list)

    clean_count = 0

    i = r # 시작 x위치
    j = c # 시작 y위치

    # 후진할 수 없을 때까지 작동
    # is_all_clean_up = True
    while True:
        # 1. 현재 칸이 청소되지 않은 경우
        if graph[i][j] == 0:
            clean_count += 1
            graph[i][j] = 2 # 청소했으면 2로 체크
        
        # 동서남북 보기
        is_clean = False
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    is_clean = True # 청소되지 않은 빈 칸이 있음

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if is_clean == False:
            # 후진할 수 있다면 후진하고, 후진할 수 없다면 멈춤
            # 동
            if d == 1:
                if j - 1 >= 0:
                    # 만약 벽이면 종료
                    if graph[i][j - 1] == 1:
                        break
                    # 벽이 아니면 후진
                    else:
                        j -= 1
                    
            # 서
            elif d == 3:
                if j + 1 < m:
                    # 만약 벽이면 종료
                    if graph[i][j + 1] == 1:
                        break
                    # 벽이 아니면 후진
                    else:
                        j += 1

            # 남
            elif d == 2:
                if i - 1 >= 0:
                    # 만약 벽이면 종료
                    if graph[i - 1][j] == 1:
                        break
                    # 벽이 아니면 후진
                    else:
                        i -= 1

            # 북
            elif d == 0:
                if i + 1 < n:
                    if graph[i + 1][j] == 1:
                        break
                    else:
                        i += 1
                    
            

        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if is_clean:
            # 1. 반시계 회전
            # 동 -> 북
            if d == 1:
                d = 0
            # 서 -> 남
            elif d == 3:
                d = 2
            # 남 -> 동
            elif d == 2:
                d = 1
            # 북 -> 서
            elif d == 0:
                d = 3

            # 2. 앞 칸이 청소되지 않았다면 한 칸 전진
            # 동
            if d == 1:
                if j + 1 < m:
                    if graph[i][j + 1] == 0:
                        j += 1
            # 서
            elif d == 3:
                if j - 1 >= 0:
                    if graph[i][j - 1] == 0:
                        j -= 1
            # 남
            elif d == 2:
                if i + 1 < n:
                    if graph[i + 1][j] == 0:
                        i += 1
            # 북
            elif d == 0:
                if i - 1 >= 0:
                    if graph[i - 1][j] == 0:
                        i -= 1

    print(clean_count)

