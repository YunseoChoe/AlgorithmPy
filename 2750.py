n = int(input())
num = []
for i in range(n):
    a = int(input())
    num.append(a)

for i in range(len(num), 0, -1):
    for j in range(i - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

for i in range(len(num)):
    print(num[i])
