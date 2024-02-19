# 수 정렬하기
n = int(input())
num = []
for i in range(n):
    n = int(input())
    num.append(n)

num.sort()

for i in range(len(num)):
    print(num[i])