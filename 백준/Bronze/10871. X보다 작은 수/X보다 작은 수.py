# x보다 작은 수
n, x = input().split()
n = int(n)
x = int(x)

num = input().split()
for i in range(n):
    num[i] = int(num[i]) # 1 <= num[i] <= 10,000

# x보다 작은 수 찾기
small = []
for i in range(n):
    if num[i] < x:
        small.append(num[i])

# 출력
for i in range(len(small)):
    print(small[i], end = " ")