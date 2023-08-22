n, m = input().split()
n = int(n)
m = int(m)

baguni = [0] * n

for _ in range(m):
    i, j, k = input().split()
    i = int(i)
    j = int(j)
    k = int(k)

    for l in (i - 1, j):
        baguni[l] = k

# 출력
for i in range(len(baguni)):
    print(baguni[i], end = " ")