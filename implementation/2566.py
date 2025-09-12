# 최댓값
# 입력받기
matrix = []  # 전체 행렬
# 문자열로 저장
for i in range(9):
    matrix.append(input().split())

# 정수화
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = int(matrix[i][j])

# 최댓값 찾기
max = -1
max_i = 0
max_j = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if max < matrix[i][j]:
            max = matrix[i][j]
            max_i = i + 1
            max_j = j + 1

# 출력하기
print(max)
print(max_i, end = " ")
print(max_j)