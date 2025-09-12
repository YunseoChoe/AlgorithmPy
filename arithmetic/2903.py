# 중앙 이동 알고리즘
# 1. 그냥 풀기
# n = int(input())    # 1 <= n <= 15
# area = 1
# sum = 4
# for i in range(n):
#     print(f'i: {i}')
#     print(f'sum: {sum}')
#     print(f'area * 4: {area * 4}')
#     print(f'i * area: {i * area}')
#     if n == 1:
#         print("if")
#         sum += (area * 4) + (area * 4 // 4) # 변 + 중앙 - 겹침(없음)
#     else:
#         print("else")
#         sum += (area * 4) + (area * 4 // 4) # 변 + 중앙
#         if i >= 1:
#             sum -= (area * 4)               # 겹치는 거 빼기 (4, 24, ...)
#     area = area * 4
#     print()
# print(f'최종 sum: {sum}')

# 2. 2차원 배열로 풀기 -> O(n) = n^2 -> 메모리 낭비가 큼
# n = int(input())    # 1 <= n <= 15
# matrix = []
# num = 2
# # for _ in range(n):
# #     num = (num * 2) - 1
# #     row_list = []
# #     for i in range(num):
# #         row_list.append(1)
# # 2차원 행렬 만들기
# # for i in range(len(row_list)):
# #     matrix.append(row_list)
# # while문 사용
# all_cnt = 0
# while all_cnt != n:
#     num = (num * 2) - 1
#     row_list = []
#     cnt = 0
#     while cnt != num:
#         row_list.append(1)
#         cnt += 1
#     all_cnt += 1
# # 2차원 행렬 만들기
# all_cnt = 0
# while all_cnt != len(row_list):
#     matrix.append(row_list)
#     all_cnt += 1
# # 점 개수 출력
# cnt = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         cnt += 1
# print(cnt)

# 3. 제곱
n = int(input())    # 1 <= n <= 15
matrix = []
num = 2

for _ in range(n):
    num = (num * 2) - 1

print(num ** 2)