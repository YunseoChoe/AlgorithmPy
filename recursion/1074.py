# Z
import sys
input = sys.stdin.readline
n, r, c = list(map(int, input().split()))
ans = 0

def z(x, y, n):
    global ans
    if x == r and y == c:
        print(ans)
        exit(0)
    
    if not (x <= r < x + n and y <= c < y + n):
        ans += n * n
        return
    
    half = n // 2
    z(x, y, half)
    z(x, y + half, half)
    z(x + half, y, half)
    z(x + half, y + half, half) 

z(0, 0, 2**n)
