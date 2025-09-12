# 단어 공부
s = input()

# 문자열 -> list
s_list = []
for i in range(len(s)):
    s_list.append(s[i])

# 소문자로 변환
for i in range(len(s)):
    s_list[i] = s_list[i].lower()

# 알파벳 리스트
alphabet = []
for i in range(26):
    alphabet.append(0)

for i in range(len(s_list)):
    alphabet[ord(s_list[i]) - 97] += 1

# 제일 빈도수 높은 알파벳 찾기
max = -1
cnt = 0
for i in range(len(alphabet)):
    if max < alphabet[i]:
        max = alphabet[i]
        max_index = i

# 중복 처리
re_max = 0
for i in range(len(alphabet)):
    if alphabet[i] == max:
        re_max += 1

# 출력하기
if re_max >= 2:
    print("?")
else:
    s = chr(max_index + 97)
    s = s.upper()
    print(s)