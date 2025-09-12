# 개수 세기
n = int(input())

# 입력 받기
num = input().split() # num에 리스트로 저장됨
# 정수로 변환
for i in range(n):
    num[i] = int(num[i])

find = int(input())
# 몇 개가 있는지 세기
cnt = 0
for i in range(len(num)):
    if num[i] == find:
        cnt += 1

print(cnt)