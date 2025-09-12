# 알고리즘 수업 - 점근적 표기 1
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

n = n0
f = a1 * n + a0
g = n

if n >= n0 and f <= c * g and a1 <= c:
    print(1)
else:
    print(0)