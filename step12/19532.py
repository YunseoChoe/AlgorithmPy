# 수학은 비대면강의입니다
a, b, c, d, e, f = map(int, input().split()) 

# 방법 1: for문 사용해서 -999 <= x, y <= 999 다 돌려보기
# 방법 2: y를 x에 대한 식으로 치환

x = (c * e - b * f) // (a * e - b * d)
y = (c * d - a * f) // (b * d - a * e)

print(int(x), int(y))