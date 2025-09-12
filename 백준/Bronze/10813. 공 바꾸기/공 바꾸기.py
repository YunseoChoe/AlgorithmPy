# 공 바꾸기
# 입력받기
n, m = input().split()
n = int(n)
m = int(m)

# 바구니
bucket = []
for i in range(1, n + 1):
    bucket.append(i)

# 공 바꾸기
for i in range(m):
    num = input().split()
    # 정수화
    for j in range(len(num)):
        num[j] = int(num[j])
    a = num[0]
    b = num[1]
    # swap
    temp = bucket[a - 1]
    bucket[a - 1] = bucket[b - 1]
    bucket[b - 1] = temp

# 출력하기
for i in range(len(bucket)):
    print(bucket[i], end = " ")