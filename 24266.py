# 알고리즘 수업 - 알고리즘의 수행 시간 5
n = int(input())

# def MenOfpassino(A: list, n: int):
#     sum = 0
#     for i in range(1, n):
#         for j in range(1, n):
#             for k in range(1, n):
#                 sum = sum + A[i] * A[j] * A[k] # 코드 1
#     return sum

# 코드 1의 수행 횟수 -> n^3
print(n ** 3)

# 최고차항의 차수 -> O(n) = n^3
print(3)