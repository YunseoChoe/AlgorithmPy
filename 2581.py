# 소수
m = int(input())
n = int(input())
prime_number = [] # 소수 리스트

for i in range(m, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            # j가 1과 나 자신이면 소수.
            if j == 1 or j == i:
                cnt += 1
            else:
                cnt = 0 # cnt를 0으로 초기화
    # cnt가 2이면 소수
    if cnt == 2:
        prime_number.append(i)

# 소수가 없으면
if not prime_number:
    print(-1)
# 소수가 있으면
else:
    # 합 
    sum = 0
    for i in range(len(prime_number)):
        sum += prime_number[i]
    print(sum)
    # 최솟값
    print(prime_number[0])