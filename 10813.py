n, m = input().split()
n = int(n)
m = int(m)

# 바구니 정렬
baguni = [0] * n
for i in range(len(baguni)):
    baguni[i] = i + 1

# 공 바꾸기
for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    a -= 1
    b -= 1
    
    # swap
    baguni[a], baguni[b] = baguni[b], baguni[a]

# 출력
for i in range(len(baguni)):
    print(baguni[i], end = " ")