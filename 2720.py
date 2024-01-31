# 세탁소 사장 동혁
t = int(input())

for i in range(t):
    c = int(input()) # 거스름돈 (단위: 센트, 1달러 == 100센트)
    print(c // 25, end = " ")
    c = c - (25 * (c // 25))
    print(c // 10, end = " ")
    c = c - (10 * (c // 10))
    print(c // 5, end = " ")
    c = c - (5 * (c // 5))
    print(c // 1, end = " ")
    c = c - (1 * (c // 1))