# 시험 감독
if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    b, c = list(map(int, input().split()))

    main_d = 0
    sub_d = 0

    for i in range(n):
        # 1. 총감독관
        s[i] = s[i] - b
        main_d += 1
        # 2. 부감독관
        if s[i] >= 0:
            if s[i] % c == 0:
                sub_d += s[i] // c 
            else:
                sub_d += s[i] // c + 1

    print(main_d + sub_d)
