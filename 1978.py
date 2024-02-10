# 소수 찾기
n = int(input())
num = input().split()
# cnt = 0
all_cnt = 0
for i in range(n):
    num[i] = int(num[i])

for i in range(len(num)):
    if num[i] == 1:
        pass
    else:    
        divisor = []
        # 약수 찾기
        for j in range(1, num[i] + 1):
            if num[i] % j == 0:
                divisor.append(j)
        
        # 소수 찾기
        cnt = 0
        for j in range(len(divisor)):
            # 소수가 아니면
            if divisor[j] != 1 and divisor[j] != num[i]:
                cnt += 1
            # 소수면 cnt는 항상 0
            else:
                cnt += 0
        # cnt가 0이면 num[i]는 소수
        if cnt == 0:
            all_cnt += 1

print(all_cnt)