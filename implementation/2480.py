# 주사위 세개
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 입력받기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print(10000 + a * 1000)
elif a == b != c:
    print(1000 + a * 100)
elif a == c != b:
    print(1000 + a * 100)
elif b == c != a:
    print(1000 + b * 100)
else:
    # a가 가장 클 때
    if a > b > c or a > c > b:
        print(a * 100)
    # b가 가장 클 때
    elif b > a > c or b > c > a:
        print(b * 100)
    # c가 가장 클 때
    else:
        print(c * 100)