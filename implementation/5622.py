# 다이얼
# 문자열 입력받기
s = input() 

# list로 변환
s = list(s)

# for문 돌면서 계산
num = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
        num = num + 3
    elif s[i] == 'D' or s[i] == 'E' or s[i] == 'F':
        num = num + 4
    elif s[i] == 'G' or s[i] == 'H' or s[i] == 'I':
        num = num + 5
    elif s[i] == 'J' or s[i] == 'K' or s[i] == 'L':
        num = num + 6
    elif s[i] == 'M' or s[i] == 'N' or s[i] == 'O':
        num = num + 7
    elif s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S':
        num = num + 8
    elif s[i] == 'T' or s[i] == 'U' or s[i] == 'V':
        num = num + 9
    elif s[i] == 'W' or s[i] == 'X' or s[i] == 'Y' or s[i] == 'Z':
        num = num + 10
    # else:
    #     num = num + 11

# 출력
print(num)