# 날짜 계산
e_input, s_input, m_input = map(int, input().split())

e = 1
s = 1
m = 1

for year in range(1, (15 * 28 * 19) + 1):
    if e_input == e and s_input == s and m_input == m:
        print(year)
        break
    # year + 1의 e, s, m 계산
    else:
        if 1 <= e <= 14:
            e += 1
        elif e == 15:
            e = 1
        if 1 <= s <= 27:
            s += 1
        elif s == 28:
            s = 1
        if 1 <= m <= 18:
            m += 1
        elif m == 19:
            m = 1