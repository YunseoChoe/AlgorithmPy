# 삼각형과 세 변
while True:
    a, b, c = map(int, input().split())
    # 0, 0, 0이면 break
    if a == b == c == 0:
        break

    # 가장 긴 변 찾기 (s, m, l)
    # a일 때
    if a >= b and a >= c:
        l = a
        m = b # 무작위
        s = c # 무작위
    # b일 때
    elif b >= a and b >= c:
        l = b
        m = c
        s = a
    # c일 때
    elif c>= a and c >= b:
        l = c
        m = a
        s = b
    
    # 세 변이 모두 같을 경우
    if l == m == s:
        print("Equilateral")
    # 삼각형의 조건 만족하는 경우
    elif l < m + s:
        # 두 변의 길이만 같은 경우
        # l, m만 같은 경우
        if l == m and l != s and m != s:
            print("Isosceles")
        # l, s 같은 경우
        elif l == s and l != m and s != m:
            print("Isosceles")
        # b, c만 같은 경우
        elif m == s and l != m and l != s:
            print("Isosceles")
        # 세 변의 길이가 모두 다른 경우
        elif l != m != s:
            print("Scalene")
    # 삼각형의 조건 만족 안 하는 경우
    else:
        print("Invalid")