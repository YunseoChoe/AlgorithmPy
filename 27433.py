def fac(n):
    if n == 0 or n == 1: # 재귀 종료시키는 부분
        return 1
    else:
        return n * fac(n  - 1)

n = int(input())

print(fac(n))