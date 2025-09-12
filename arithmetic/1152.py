# 단어의 개수
s = input()

# 공백을 기준으로 list로 변환
s_list = s.split() 

cnt = 0
for i in range(len(s_list)):
    cnt += 1

print(cnt)