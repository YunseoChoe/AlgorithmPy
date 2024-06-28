# 최대 길이 계산 함수
def calculator_max_length(matrix, n, i, j):
    # 최대 길이 계산
    # 가로 길이
    cnt_width = 1
    cnt_width_max = 1
    for k in range(n - 1):
        if matrix[i][k] == matrix[i][k + 1]:
            cnt_width += 1
            cnt_width_max = cnt_width
        else:
            cnt_width = 1

    # 세로 길이
    cnt_height = 1
    cnt_height_max = 1
    for k in range(n - 1):
        if matrix[k][j] == matrix[k + 1][j]:
            cnt_height += 1
            cnt_height_max = cnt_height
        else:
            cnt_height = 1
    return_value = max(cnt_height_max, cnt_width_max)
    return return_value

# 사탕 게임
n = int(input())

# 입력 n * n
matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

cnt = []
for i in range(n):
    for j in range(n):
        swap = False

        # 가로로 swap
        if j + 1 < n and matrix[i][j] != matrix[i][j + 1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            swap = True

            # 최대 길이 계산 (가로, 세로)
            cnt.append(calculator_max_length(matrix, n, i, j))
        
        # swap을 했으면 원위치
        if swap:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            swap = False

        # 세로로 swap
        if i + 1 < n and matrix[i][j] != matrix[i + 1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            swap = True

            # 최대 길이 계산 (가로, 세로)
            cnt.append(calculator_max_length(matrix, n, i, j))
            
        # swap을 했으면 원위치
        if swap:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            swap = False

print(max(cnt))

# # 사탕 게임
# # 최대 길이 계산 함수
# def calculator_max_length(matrix, n):
#     max_length = 1
    
#     # 가로 최대 길이
#     for i in range(n):
#         cnt = 1
#         for j in range(n):
#             if j + 1 < n and matrix[i][j] == matrix[i][j + 1]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             max_length = max(max_length, cnt)
#     # 세로 최대 길이
#     for j in range(n):
#         cnt = 1
#         for i in range(n):
#             if i + 1 < n and matrix[i][j] == matrix[i + 1][j]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             max_length = max(max_length, cnt)

#     return max_length

# n = int(input())

# # 입력 n * n
# matrix = []
# for _ in range(n):
#     row = list(input())
#     matrix.append(row)

# cnt = []
# for i in range(n):
#     for j in range(n):
#         # 가로로 swap
#         if j + 1 < n and matrix[i][j] != matrix[i][j + 1]:
#             matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
#             swap = True
            

#             # matrix의 최대 길이 계산
#             cnt.append(calculator_max_length(matrix, n))
            
#             # swap을 했으면 원위치
#             if swap:
#                 matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
#                 swap = False

#         # 세로로 swap
#         if i + 1 < n and matrix[i][j] != matrix[i + 1][j]:
#             matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
#             swap = True

#             # matrix의 최대 길이 계산
#             cnt.append(calculator_max_length(matrix, n))

#             # swap을 했으면 원위치
#             if swap:
#                 matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
#                 swap = False

# print(max(cnt))
 