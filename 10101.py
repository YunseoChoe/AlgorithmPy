# 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())

# 세 각의 크기가 모두 60일 때
if a == b == c == 60:
    print("Equilateral")

# 세 각의 합이 180도 이고, 두 각이 같은 경우
# a, b가 같은 경우
elif a + b + c == 180 and a == b and a != c and b != c:
    print("Isosceles")
# a, c가 같은 경우
elif a + b + c == 180 and a == c and a != b and c != b:
    print("Isosceles")
# b, c가 같은 경우
elif a + b + c == 180 and b == c and b != a and c != a:
    print("Isosceles")
# 같은 각이 없는 경우
elif a + b + c == 180 and a != b != c:
    print("Scalene")

# 세 각의 합이 180도 아닌 경우
else:
    print("Error")