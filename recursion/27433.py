# 팩토리얼 2
def fac(n):
    if n == 0: 
        return 1
    else:
        return n * fac(n  - 1)

n = int(input())

print(fac(n))