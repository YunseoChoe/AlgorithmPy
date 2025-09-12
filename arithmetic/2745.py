# 진법 변환
n, b = input().split() # b진법 수 n
b = int(b)

# n을 10진법으로 변환 (int함수 이용)
print(int(n, b))