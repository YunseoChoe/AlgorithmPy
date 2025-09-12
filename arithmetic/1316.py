# 그룹 단어 체커
# 알파벳 리스트
alphabet = []

# 입력받기
t = int(input())
all_cnt = 0
for i in range(t):
    # 알파벳 리스트 초기화
    alphabet = [0] * 26
    s = input()
    cnt = 0
    # for문 돌면서 그룹 단어 체크
    for j in range(len(s)):
        if (j < len(s) - 1 and s[j] != s[j + 1]):
            if alphabet[ord(s[j]) - 97] == 0:
                alphabet[ord(s[j]) - 97] = 1
                cnt += 0
            else:
                cnt += 1

        if (j < len(s) - 1 and s[j] == s[j + 1]):
            pass

        # 맨 끝 알파벳
        elif (j == len(s) - 1):
            if alphabet[ord(s[j]) - 97] == 0:
                alphabet[ord(s[j]) - 97] = 1
                cnt += 0
            else:
                cnt += 1

    if cnt == 0:
        all_cnt += 1

# 출력하기
print(all_cnt)