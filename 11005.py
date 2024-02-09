# 진법 변환2

# 입력 받기
n, b = map(int, input().split())

namuji = []
while n != 0:
    namuji.append(n % b)
    n = n // b

# namuji 역순
reverse_namuji = []
for i in range(len(namuji) - 1, -1, -1):
    reverse_namuji.append(namuji[i])

# print(reverse_namuji)

# 10진법이 넘어가는 수 진법 변환
for i in range(len(reverse_namuji)):
    if reverse_namuji[i] == 10:
        reverse_namuji[i] = 'A'
    elif reverse_namuji[i] == 11:
        reverse_namuji[i] = 'B'
    elif reverse_namuji[i] == 12:
        reverse_namuji[i] = 'C'
    elif reverse_namuji[i] == 13:
        reverse_namuji[i] = 'D'
    elif reverse_namuji[i] == 14:
        reverse_namuji[i] = 'E'
    elif reverse_namuji[i] == 15:
        reverse_namuji[i] = 'F'
    elif reverse_namuji[i] == 16:
        reverse_namuji[i] = 'G'
    elif reverse_namuji[i] == 17:
        reverse_namuji[i] = 'H'
    elif reverse_namuji[i] == 18:
        reverse_namuji[i] = 'I'
    elif reverse_namuji[i] == 19:
        reverse_namuji[i] = 'J'
    elif reverse_namuji[i] == 20:
        reverse_namuji[i] = 'K'
    elif reverse_namuji[i] == 21:
        reverse_namuji[i] = 'L'
    elif reverse_namuji[i] == 22:
        reverse_namuji[i] = 'M'
    elif reverse_namuji[i] == 23:
        reverse_namuji[i] = 'N'
    elif reverse_namuji[i] == 24:
        reverse_namuji[i] = 'O'
    elif reverse_namuji[i] == 25:
        reverse_namuji[i] = 'P'
    elif reverse_namuji[i] == 26:
        reverse_namuji[i] = 'Q'
    elif reverse_namuji[i] == 27:
        reverse_namuji[i] = 'R'
    elif reverse_namuji[i] == 28:
        reverse_namuji[i] = 'S'
    elif reverse_namuji[i] == 29:
        reverse_namuji[i] = 'T'
    elif reverse_namuji[i] == 30:
        reverse_namuji[i] = 'U'
    elif reverse_namuji[i] == 31:
        reverse_namuji[i] = 'V'
    elif reverse_namuji[i] == 32:
        reverse_namuji[i] = 'W'
    elif reverse_namuji[i] == 33:
        reverse_namuji[i] = 'X'
    elif reverse_namuji[i] == 34:
        reverse_namuji[i] = 'Y'
    elif reverse_namuji[i] == 35:
        reverse_namuji[i] = 'Z'

# reverse_namuji 출력
for i in range(len(reverse_namuji)):
    print(reverse_namuji[i], end = "")