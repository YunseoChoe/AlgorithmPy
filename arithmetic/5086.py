# 배수와 약수
while True:
    # 입력
    a, b = map(int, input().split())
    # 둘 다 0이면 멈춤
    if a == 0 and b == 0:
        exit()
    else:
        # 1. 약수
        if b % a == 0:
            print("factor")
        # 2. 배수
        elif a % b == 0:
            print("multiple")
        # 3. 둘 다 아니라면
        else:
            print("neither")