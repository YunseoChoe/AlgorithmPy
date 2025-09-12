# 알파벳 찾기
s = input()

alphabet_list = []
for i in range(26):
    alphabet_list.append(-1)

for i in range(len(s)):
    if s[i] == 'a' and alphabet_list[0] == -1:
        alphabet_list[0] = i
    elif s[i] == 'b' and alphabet_list[1] == -1:
        alphabet_list[1] = i
    elif s[i] == 'c' and alphabet_list[2] == -1:
        alphabet_list[2] = i
    elif s[i] == 'd' and alphabet_list[3] == -1:
        alphabet_list[3] = i
    elif s[i] == 'e' and alphabet_list[4] == -1:
        alphabet_list[4] = i
    elif s[i] == 'f' and alphabet_list[5] == -1:
        alphabet_list[5] = i
    elif s[i] == 'g' and alphabet_list[6] == -1:
        alphabet_list[6] = i
    elif s[i] == 'h' and alphabet_list[7] == -1:
        alphabet_list[7] = i
    elif s[i] == 'i' and alphabet_list[8] == -1:
        alphabet_list[8] = i
    elif s[i] == 'j' and alphabet_list[9] == -1:
        alphabet_list[9] = i
    elif s[i] == 'k' and alphabet_list[10] == -1:
        alphabet_list[10] = i
    elif s[i] == 'l' and alphabet_list[11] == -1:
        alphabet_list[11] = i
    elif s[i] == 'm' and alphabet_list[12] == -1:
        alphabet_list[12] = i
    elif s[i] == 'n' and alphabet_list[13] == -1:
        alphabet_list[13] = i
    elif s[i] == 'o' and alphabet_list[14] == -1:
        alphabet_list[14] = i
    elif s[i] == 'p' and alphabet_list[15] == -1:
        alphabet_list[15] = i
    elif s[i] == 'q' and alphabet_list[16] == -1:
        alphabet_list[16] = i
    elif s[i] == 'r' and alphabet_list[17] == -1:
        alphabet_list[17] = i
    elif s[i] == 's' and alphabet_list[18] == -1:
        alphabet_list[18] = i
    elif s[i] == 't' and alphabet_list[19] == -1:
        alphabet_list[19] = i
    elif s[i] == 'u' and alphabet_list[20] == -1:
        alphabet_list[20] = i
    elif s[i] == 'v' and alphabet_list[21] == -1:
        alphabet_list[21] = i
    elif s[i] == 'w' and alphabet_list[22] == -1:
        alphabet_list[22] = i
    elif s[i] == 'x' and alphabet_list[23] == -1:
        alphabet_list[23] = i
    elif s[i] == 'y' and alphabet_list[24] == -1:
        alphabet_list[24] = i
    elif s[i] == 'z' and alphabet_list[25] == -1:
        alphabet_list[25] = i

for i in range(26):
    print(alphabet_list[i], end = " ")

# s = input()

# li=[]  #빈 리스트 생성

# for i in range(26):  #리스트에 26개의 -1추가
#     li.append(-1)

# for j in range(len(s)):  
#     b = ord(s[j]) - ord('a')
#     print(f'b: {b}')
#     if li[b] == -1:
#         li[b] = j # 문자열 자리 번호 

# for k in range(26):
#     print(li[k],end=" ")