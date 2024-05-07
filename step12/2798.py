# 블랙잭
n, m = map(int, input().split())

num = []
user_input = input()
num.extend(map(int, user_input.split()))

# 오름차순 정렬
num.sort()

max = -1
for i in range(len(num) - 1, -1, -1):
    for j in range(len(num) - 2, -1, -1):
        for k in range(len(num) - 3, -1, -1):
            sum = num[i] + num[j] + num[k]
            if sum <= m and num[i] != num[j] and num[i] != num[k] and num[j] != num[k]:
                if max < sum:
                    max = sum

print(max)