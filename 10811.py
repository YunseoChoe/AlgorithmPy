# 바구니 뒤집기
n, m = input().split()
n = int(n)
m = int(m)

bucket = []
for i in range(1, n + 1):
    bucket.append(i)

for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)

    # 부분 나누기
    part = bucket[a - 1: b]
    # 부분 뒤집기
    part.reverse()
    # 합치기
    bucket = bucket[:a - 1] + part + bucket[b:]
    # print(bucket)

# list -> 하나씩 출력
for i in range(len(bucket)):
    print(bucket[i], end = " ")