# 알고리즘 수업 - 알고리즘의 수행 시간 6
n = int(input())

# def MenOfPassion(A: list, n: int):
#     sum = 0
#     for i in range(1, n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 sum += A[i] * A[j] * A[k] # 코드 1
#     return sum

# 코드 1의 수행 횟수 출력 -> nc3
# solution 1. 반복문 -> 시간 초과
# cnt = 0
# for i in range(1, n - 1):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n + 1):
#             cnt += 1
# print(cnt)
# solution 2. 조합 -> 성공 
sum = int(n * (n - 1) * (n - 2) / (6))
print(sum)

# 최고차항의 차수 출력 -> O(n) = n^3
print(3)