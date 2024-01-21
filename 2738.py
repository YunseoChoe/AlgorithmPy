# 행렬 덧셈
# 입력
n, m = input().split()
n = int(n) # 행
m = int(m) # 열

# 2개의 행렬 입력
matrix1 = []
for i in range(n):
    row_list = input().split()
    # 정수화
    for j in range(m):
        row_list[j] = int(row_list[j])
    matrix1.append(row_list)

matrix2 = []
for i in range(n):
    row_list = input().split()
    # 정수화
    for j in range(m):
        row_list[j] = int(row_list[j])
    matrix2.append(row_list)

# 전체 행렬 초기화
matrix = []
for i in range(n):
    row_list = []
    for j in range(m):
        row_list.append(0)
    matrix.append(row_list)

# 행렬 덧셈
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix1[i][j] + matrix2[i][j]

# 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = " ")
    print()