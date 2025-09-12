x = int(input()) # 총 금액 x
n = int(input()) # 구매한 물건의 종류의 수 n
sum = 0 # 총계
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    sum = sum + a * b
if x == sum:
    print("Yes")
else:
    print("No")