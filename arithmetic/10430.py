# 나머지
# 입력받기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# 출력하기
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)