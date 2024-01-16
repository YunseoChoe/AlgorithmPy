# 공 넣기
# 입력 받기
n, m = input().split()
n = int(n)
m = int(m)

# 바구니 초기화
bucket = []
for i in range(n):
    bucket.append(0)

# 공 넣기
for _ in range(m):
    num = input().split()
    for l in range(len(num)):
        num[l] = int(num[l])
    i = num[0]
    j = num[1]
    k = num[2]
    for s in range(i - 1, j):
        bucket[s] = k

# 출력하기
for i in range(len(bucket)):
    print(bucket[i], end = " ")