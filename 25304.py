# 영수증
x = int(input()) # 구매한 총 금액
n = int(input()) # 구매한 물건의 종류의 수
sum = 0
for i in range(n):
    a, b = input().split() # 물건의 가격과 개수
    a = int(a)
    b = int(b)
    sum = sum + a * b

if x == sum:
    print("Yes")
else:
    print("No")