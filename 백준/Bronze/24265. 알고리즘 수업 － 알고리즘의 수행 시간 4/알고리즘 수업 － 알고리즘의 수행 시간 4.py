# 알고리즘 수업 - 알고리즘의 수행 시간 4

n = int(input())

# def MenOfPassion(A :list, n: int):
#     sum = 0
#     for i in range(1, n - 1):
#         for j in range(i + 1, n):
#             sum = sum + A[i] * A[j] # 코드 1
#     return sum

# 코드 1의 수행 횟수 출력 -> 
sum = 0
for i in range(n - 1, 0, -1):
    sum += i
print(sum)
# 최고차항의 차수 출력 -> O(n) = n^2
print(2)