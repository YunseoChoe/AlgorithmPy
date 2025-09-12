# 세 막대
a, b, c = map(int, input().split())

# 삼각형 조건 만족하는지
# 제일 긴 변 찾기
max = a
side1 = b
side2 = c
if max < b:
    max = b
    side1 = a
    side2 = c
if max < c:
    max = c
    side1 = a
    side2 = b
if max < side1 + side2:
    sum = max + side1 + side2
else:
    max = side1 + side2 - 1
    sum = max + side1 + side2

print(sum)