# 바구니 뒤집기
# 입력받기 1
n, m = input().split()
n = int(n)
m = int(m)

# 바구니 생성  
num = []
for i in range(1, n + 1):
    num.append(i)

# 입력받기 2
for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    temp = num[a - 1:b]
    temp.reverse()
    print(temp)
    num = temp + num[b:]
    print(num)

print(f'{num}')

# num = [1, 2, 3, 4, 5]
# temp = num[0:3]
# temp.reverse()
# print(temp)














