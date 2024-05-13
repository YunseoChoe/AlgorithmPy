# 알고리즘 수업 - 점근적 표기 1
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0
g = n0

if f <= g * c and a1 <= c: # 기울기 비교했을 때
    print(1)
else:
    print(0)