# 수 정렬하기 2
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

# Bubble Sort -> 시간 초과
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         if num[j] > num[j + 1]:
#             # swap
#             tmp = num[j]
#             num[j] = num[j + 1]
#             num[j + 1] = tmp

# Merge Sort

# 출력
for i in range(len(num)):
    print(num[i])