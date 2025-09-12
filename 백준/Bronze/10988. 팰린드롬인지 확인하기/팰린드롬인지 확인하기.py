# 팰린드롬인지 확인하기
# 입력받기 
s = input() # 1 <= s <= 100
cnt = 0

# 확인
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        cnt += 1

# 출력하기
if cnt != 0:
    print(0)
else:
    print(1)