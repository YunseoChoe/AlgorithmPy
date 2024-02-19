# 알고리즘 수업 - 알고리즘의 수행 시간 3

n = int(input())

# def MenOfPassion(A :list, n: int):
#     sum = 0
#     for i in range(1, n):
#         for j in range(1, n):
#             sum = sum + A[i] * A[j] # 코드 1
#     return sum

# 코드 1의 수행 횟수 출력 -> n^2에 비례
print(n ** 2)
# 최고 차항 차수 출력 -> O(n) = n^2
print(2)