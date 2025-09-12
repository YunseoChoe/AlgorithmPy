# 최소, 최대
n = int(input())

num = input().split()
for i in range(n):
    num[i] = int(num[i])

# 최솟값, 최댓값 찾기
max = num[0]
min = num[0]
for i in range(n):
    if max < num[i]:
        max = num[i]
    if min > num[i]:
        min = num[i]

print(f'{min} {max}')