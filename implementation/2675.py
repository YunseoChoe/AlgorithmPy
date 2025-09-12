# 문자열 반복
t = int(input())

for i in range(t):
    num = input().split() # (정수, 문자)
    n = int(num[0])
    s = list(num[-1])

    for i in range(len(s)):
        print(s[i] * n, end = "")
    print()